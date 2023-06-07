import argparse
import datetime
import asyncio
from logging import getLogger, DEBUG, StreamHandler, Formatter, handlers, INFO
import queue
import subprocess
import threading
from threading import Lock,Thread
import time,os,sys

sys.path.append(os.getcwd()+"/generation")
sys.path.append(os.getcwd()+"/networkcontrol")
sys.path.append(os.getcwd()+"/DifferenceAnalyzer")
sys.path.append(os.getcwd()+"/DifferenceStrategies")
import socket
from StrategyQueue import StrategyQueue

from OpenFlowProxy.proxy import ChannelManager,SwitchHandler, come_back_to_init_state
from OpenFlowProxy.observable import ObservableData
from capture.capture import CaptureBase, SimpleCapture
from DifferenceAnalyzer.ControllerResQueue import ControllerResQueue
from networkcontrol.mininet_runner import MininetControl
from DifferenceAnalyzer.DifferenceAnalyzer import DifferenceAnalyzer
import faulthandler;faulthandler.enable()


# logger = getLogger("ofcapture")
default_logfile = "log/" + "ofcapture-" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') + ".log" 

# global var
wait_exec_controller_strategy = StrategyQueue()
finished_controller_strategy = StrategyQueue()

# global fisish flag
global test_finish_flag

def set_logger(log_level=DEBUG, filename=default_logfile, logger_name="of"):
	logger = getLogger(logger_name)
	logger.setLevel(log_level)
	formatter = Formatter(
		"%(asctime)s | %(process)d | %(name)s, %(funcName)s, %(lineno)d | %(levelname)s | %(message)s")
	handler = handlers.RotatingFileHandler(filename=filename,
										   maxBytes=16777216,
										   backupCount=2)
	handler.setLevel(log_level)
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	return logger

class OFCaptureBase:
	"""OpenFlow proxy to capture

	Attributes:
		channel_manager (ChannelManager) :
		observable (Observable) : observable instance
		switch_handler (SwitchHandler) : local server
		event_loop (asyncio.EventLoop) : event loop
	"""
	def __init__(self, local_ip='127.0.0.1', local_port=3456, controller_ip='127.0.0.1', controller_port=6653,
				 event_loop=None, log_file=None, log_level=INFO,logger_name="",controller_type ="",
				 strategy_queue="",controller_result=[]):
		self.event_loop = event_loop if event_loop else asyncio.get_event_loop()
		# TCP client
		self.channel_manager = ChannelManager(loop=self.event_loop,
												controller_ip=controller_ip,
												controller_port=controller_port,
												logger_name=logger_name)
		# observable OpenFlow message
		self.observable = ObservableData(self.channel_manager.q_all,logger_name=logger_name)

		# local server
		self.switch_handler = SwitchHandler(host=local_ip,
											port=local_port,
											loop=self.event_loop,
											channel_manager=self.channel_manager,
											logger_name=logger_name,
											controller_type = controller_type,
											strategy_queue=strategy_queue,
											result_queue=controller_result
											)

		# capture
		self.capture:CaptureBase = SimpleCapture(observable=self.observable,logger_name=logger_name)

		if log_file:
			self.logger = set_logger(log_level=log_level, filename=log_file,logger_name=logger_name)
			self.logger.info("OFCapture ready (lip={}, lport={}, cip={}, cport={}, async_queue={})".format(
			local_ip, local_port, controller_ip, controller_port, self.channel_manager.q_all
		))
	
	def start_server(self,coro:list = None):
		self.event_loop.run_until_complete(self.start_server_coro(coro))

	async def start_server_coro(self, coro: list = None):
		coro = coro if coro is not None else []
		await asyncio.gather(*[
			self.switch_handler.start_server(),
			self.observable.start_search(),
			*coro
		], loop=self.event_loop)

	def stop_server(self):
		self.event_loop.stop()
		self.event_loop.close()

	def on(self, msg_type, handler=None):
		"""
		Examples:
			# 10 represent type packet in 
			# get only packet in message
			@ofcapture.on(10)
			def packetin_handler(msg):
				print(msg)

			# get all message
			@ofcapture.on("*")
			def all_msg_handler(msg):
				print(msg)
		"""
		def set_handler(handler):
			self.capture.handlers[msg_type] = handler
			return handler
		if handler is None:
			return set_handler
		set_handler(handler)

	def proxy_reset(self):
		come_back_to_init_state()


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--verbose', action='store_true')
	parser.add_argument('--log_file', help="log file path", default=None)

	args = parser.parse_args()
	return args

class OFCaptureThread(threading.Thread):
	def __init__(self,local_ip,local_port,controller_ip,controller_port,log_file,logger_name,controller_type,strategy_queue,result_queue=[]):
		super(OFCaptureThread,self).__init__()
		self.local_ip = local_ip
		self.local_port = local_port
		self.controller_ip = controller_ip
		self.controller_port = controller_port
		self.log_file = log_file
		self.logger_name = logger_name
		self.controller_type = controller_type
		self._strategy_queue = strategy_queue
		self.result_queue = result_queue
		self.lock = threading.Lock()

	def run(self):
		event_loop = asyncio.new_event_loop()
		self.ofcapture = OFCaptureBase(local_ip=self.local_ip,local_port=self.local_port,controller_ip=self.controller_ip,
			controller_port=self.controller_port,log_file=self.log_file,event_loop=event_loop,logger_name=self.logger_name,
			controller_type=self.controller_type,strategy_queue=self._strategy_queue,controller_result=self.result_queue)
		try:
			self.ofcapture.start_server()
		except KeyboardInterrupt as e:
			self.ofcapture.logger.info("keyboardInterrupt : {}".format(str(e)))
		exit()

	def proxy_reset(self):
		self.ofcapture.proxy_reset()
	
	def restart(self):
		event_loop = asyncio.new_event_loop()
		self.ofcapture = OFCaptureBase(local_ip=self.local_ip,local_port=self.local_port,controller_ip=self.controller_ip,
			controller_port=self.controller_port,log_file=self.log_file,event_loop=event_loop,logger_name=self.logger_name,
			controller_type=self.controller_type,strategy_queue=self._strategy_queue,controller_result=self.result_queue)

def reconnect(addr):
	sock = 0
	while True:
		try:
			sock = socket.create_connection(addr)
			break
		except Exception as e:
			print("[%s] Failed to connect to strategy generator (%s:%d): %s...retrying" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),addr[0], addr[1], e))
			time.sleep(5)
			continue
	return sock

def connect_to_strategy_generator(instance,addr,num,sock,rf,pause_flag): #(tester, instance, log, addr=("127.0.0.1",3333)):
	ready_flag = True
	while True:
		print("****************")
		#Ask for Next Strategy
		print("[%s] Asking for Next Strategy..." % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
		# todo : write log file
		try:
			if ready_flag:
				msg = {'msg':'READY','instance':"%s:%d"%(socket.gethostname(),instance)}
				send_str = "%s\n" %(repr(msg))
				sock.send(send_str.encode())
				ready_flag = False
		except Exception as e:
			print("Failed to send on socket...")
			print("e:",e.with_traceback())
			time.sleep(10)
			rf.close()
			sock.close()
			sock = reconnect(addr)
			rf = sock.makefile()

		#Get Reply
		try:
			line = rf.readline()
		except Exception as e:
			print("Failed to send on socket...")
			rf.close()
			sock.close()
			sock = reconnect(addr)
			rf = sock.makefile()

		if line=="":
			rf.close()
			sock.close()
			sock = reconnect(addr)
			rf = sock.makefile()
		try:
			msg = eval(line)
		except Exception as e:
			pass

		if msg['msg']=="DONE":
			# Done, shutdown
			print("[%s] Finished... Shutting down..." % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
			global test_finish_flag 
			test_finish_flag = False
			# todo : write log file
		elif msg['msg']=="STRATEGY":
			#Test Strategy
			strategy = msg['data']
			global wait_exec_controller_strategy
			global finished_controller_strategy
			wait_exec_controller_strategy.enqueue(strategy)
			print ("[%s] Test %d: %s" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
				finished_controller_strategy.size(), str(strategy)))
			
			# todo : write log file
			old_size = finished_controller_strategy.size()
			while old_size == finished_controller_strategy.size():
				pass
			res = finished_controller_strategy.get_strategy_result(strategy)
			num+=1
			controller_result_str = ""
			for item in res[2]:
				controller_result_str = controller_result_str + "# Controller: " + item.controller_type+ "\n"
				controller_result_str = controller_result_str + item.to_file()
			

			write_to_file("./DifferenceStrategies/strategy_trace.txt",strategy,finished_controller_strategy.size(),res[0],res[1],controller_result_str)
			if res[0] == True:
				write_to_difference_file("./DifferenceStrategies/differences_strategy.txt",strategy,finished_controller_strategy.size(),res[1])

			#Return Result and Feedback
			print ("[%s] Test Result: %s, Reason: %s" %(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),str(res[0]), res[1]))
			
			feedback = "of_hello"

			# todo : write log file

	
			try:
				msg = {'msg':'RESULT','instance':"%s:%d"%(socket.gethostname(),instance), 'value':res[0], 'reason':res[1],'feedback':feedback,'casenumber':finished_controller_strategy.size()}
				send_str = "%s\n" %(repr(msg))
				sock.send(send_str.encode())
			except Exception as e:
				print("Failed to send on socket...")
				sock = reconnect(addr)
			ready_flag = True
		elif msg['msg'] == 'WAIT':
			time.sleep(3)
			continue

class OFGenerationHandler(threading.Thread):

	def __init__(self,instance,addr):
		super( OFGenerationHandler,self).__init__()
		self.__flag = threading.Event() # the flag to pause thread
		self.__flag.set() # the flag set True
		self.__running = threading.Event()  # the flag to stop thread
		self.__running.set() # the flag set True
		self.instance = instance
		self.addr = addr

	def run(self):
		num = 1
		
		#Connect
		try:
			sock = socket.create_connection(self.addr)
		except Exception as e:
			print("[%s] Failed to connect to strategy generator(%s:%d): %s" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),self.addr[0], self.addr[1], e))
			return
		rf = sock.makefile()

		if self.__running.isSet():
			connect_to_strategy_generator(0,("127.0.0.1",3333),num,sock,rf,self.__flag)
			

	def pause(self):
		self.__flag.clear()

	def resume(self):
		self.__flag.set()

	def stop(self):
		self.__flag.set() # restore from block state , if thread is paused
		self.__running.clear() 

"""
	queue put according to controller type , 
"""
def exec_strategy_queue_put(strategy_queue_list,item):
	for strategy_queue in strategy_queue_list: 
		strategy_queue.enqueue(item)

# ryu will be Terminated by "sudo mn -c" command
def restartRyu():
	command = 'exec sudo ./automaticcontrol/run_ryu.sh'
	process = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                                        ,preexec_fn=os.setpgrp,close_fds=True)

def runMultiReqForController():
	command = 'exec sudo python ./RestAPP/MulReqForController.py'
	process = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                                        ,preexec_fn=os.setpgrp,close_fds=True)


def write_to_file(f,strategy,case_number,res,reason,controller_result_str):
	result_file = open( file = f,mode = 'a+', encoding = "utf-8")
	result_file.write("# test case {} \t result : {}\n".format(case_number,res))
	result_file.write("# excution situation : {}\n".format(reason))
	result_file.write(controller_result_str)
	result_file.write(strategy+"\n")
	result_file.write("\n")

def write_to_difference_file(f,strategy,case_number,reason):
	result_file = open( file = f,mode = 'a+', encoding = "utf-8")
	result_file.write("# test case {} \n".format(case_number))
	result_file.write("# excution situation : {}\n".format(reason))
	result_file.write(strategy+"\n")
	result_file.write("\n")

def mininetStart(mininet_thread):
	for mn_thread in mininet_thread:
		mn_thread.start()

def mininetStop(mininet_thread):
	for mn_thread in mininet_thread:
		mn_thread.stop()

def mininetRestart(mininet_thread):
	for mn_thread in mininet_thread:
		mn_thread.restart()

def proxyStart(proxy_threads):
	for proxy_thread in proxy_threads:
		proxy_thread.start()

def proxyStop(proxy_threads):
	for proxy_thread in proxy_threads:
		proxy_thread.stop()

def proxyReset(proxy_threads):
	for proxy_thread in proxy_threads:
		proxy_thread.proxy_reset()

def main():
	args = get_args()
	loglevel = DEBUG if args.verbose else INFO
	exec_strategy_queue = []
	ryu_exec_strategy_queue = StrategyQueue()
	fl_exec_strategy_queue = StrategyQueue()
	onos_exec_strategy_queue = StrategyQueue()
	odl_exec_strategy_queue = StrategyQueue()
	exec_strategy_queue.append(ryu_exec_strategy_queue)
	exec_strategy_queue.append(fl_exec_strategy_queue)
	exec_strategy_queue.append(onos_exec_strategy_queue)
	exec_strategy_queue.append(odl_exec_strategy_queue)
	"""queue is not reference passing , while list is"""
	ryu_exec_result_queue = ControllerResQueue("ryu")
	fl_exec_result_queue = ControllerResQueue("fl")
	onos_exec_result_queue = ControllerResQueue("onos")
	odl_exec_result_queue = ControllerResQueue("odl")
	
	controller_result_queues = []
	controller_result_queues.append(ryu_exec_result_queue)
	controller_result_queues.append(fl_exec_result_queue)
	controller_result_queues.append(onos_exec_result_queue)
	controller_result_queues.append(odl_exec_result_queue)
	diff_analyzer = DifferenceAnalyzer(controller_result_queues)

	proxy_thread = []
	mininet_thread = []
	single_strategy = ""
	exec_strategy_queue_put(exec_strategy_queue,single_strategy)
	ryu_thread = OFCaptureThread(local_ip='192.168.239.128',local_port=3456, controller_ip='172.17.0.2',
								controller_port=6653,log_file=args.log_file+"1",logger_name="ryu_ofcapture",
								controller_type="ryu",strategy_queue=ryu_exec_strategy_queue,result_queue=ryu_exec_result_queue)
	fl_thread = OFCaptureThread(local_ip='192.168.239.128',local_port=3457, controller_ip='172.17.0.3',
								controller_port=6653,log_file=args.log_file+"2",logger_name="fl_ofcapture",
								controller_type="floodlight",strategy_queue=fl_exec_strategy_queue,result_queue=fl_exec_result_queue)
	onos_thread = OFCaptureThread(local_ip='192.168.239.128',local_port=3458, controller_ip='172.17.0.4',
							controller_port=6653,log_file=args.log_file+"3",logger_name="fl_ofcapture",
							controller_type="onos",strategy_queue=onos_exec_strategy_queue,result_queue=onos_exec_result_queue)
	odl_thread = OFCaptureThread(local_ip='192.168.239.128',local_port=3459, controller_ip='172.17.0.5',
								controller_port=6653,log_file=args.log_file+"4",logger_name="onos_ofcapture",
								controller_type="odl",strategy_queue=odl_exec_strategy_queue,result_queue=odl_exec_result_queue)
	ofgenhandler = OFGenerationHandler(0,("127.0.0.1",3333))
	proxy_thread.append(ryu_thread)
	proxy_thread.append(fl_thread)
	proxy_thread.append(onos_thread)
	proxy_thread.append(odl_thread)
	proxyStart(proxy_thread)
	ofgenhandler.start()
	
	ryu_mn_thread = MininetControl('192.168.239.128','3456','sametopo1_single2.py')
	fl_mn_thread = MininetControl('192.168.239.128','3457','sametopo2_single2.py')
	onos_mn_thread = MininetControl('192.168.239.128','3458','sametopo3_single2.py')
	odl_mn_thread = MininetControl('192.168.239.128','3459','sametopo4_single2.py')
	mininet_thread.append(ryu_mn_thread)
	mininet_thread.append(fl_mn_thread)
	mininet_thread.append(onos_mn_thread)
	mininet_thread.append(odl_mn_thread)
	mininetStart(mininet_thread)
	start_time = time.time()
	
	# global test_finish_flag
	test_finish_flag = True
	new_strategy = None

	while test_finish_flag:	
		wait_strategy_number = wait_exec_controller_strategy.size()
		
		if wait_strategy_number != 0:
			ofgenhandler.pause()

			new_strategy = wait_exec_controller_strategy.dequeue()
			exec_strategy_queue_put(exec_strategy_queue,new_strategy)
			start_time = time.time()
		consume_time = time.time()-start_time
		if diff_analyzer.allExec():
			diff_analyzer.ControllerResultPrint()
			diff_analyzer.compareListBuild()
			difference = diff_analyzer.diffanalysis()
			finished_controller_strategy.enqueue(new_strategy)
			finished_controller_strategy.set_strategy_result(new_strategy,(difference,"success execution",diff_analyzer.compare_list))
			finished_controller_strategy.mapper_print()
			
			mininetStop(mininet_thread)
			time.sleep(5)
			os.system("sudo mn -c")

			restartRyu()			
			proxyReset(proxy_thread)
			mininetRestart(mininet_thread)
		elif (consume_time > 30) and new_strategy is not None:
			if diff_analyzer.notExec():
				difference = False
				finished_controller_strategy.enqueue(new_strategy)
				finished_controller_strategy.set_strategy_result(new_strategy,(difference,"Not execution at all",[]))
				finished_controller_strategy.mapper_print()
				mininetStop(mininet_thread)
				os.system("sudo mn -c")
				proxyReset(proxy_thread)
				restartRyu()
				mininetRestart(mininet_thread)
			else:
				diff_analyzer.ControllerResultPrint()
				if diff_analyzer.OnlyExec():
					difference = False
				else:
					diff_analyzer.compareListBuild()
					difference = diff_analyzer.diffanalysis()

				finished_controller_strategy.enqueue(new_strategy)
				finished_controller_strategy.set_strategy_result(new_strategy,(difference,"Partial execution",diff_analyzer.compare_list))

				mininetStop(mininet_thread)
				os.system("sudo mn -c")
				restartRyu()
				proxyReset(proxy_thread)
				mininetRestart(mininet_thread)
			new_strategy = None

	mininetStop(mininet_thread)
	os.system("sudo mn -c")
	ofgenhandler.stop()

if __name__ == "__main__":
	main()