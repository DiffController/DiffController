import argparse
import datetime
import sys

from socketserver import StreamRequestHandler,ThreadingTCPServer
from unittest import result
import StrategyGenerator
import threading
from StrategyQueue import StrategyQueue
from evolve import genetic_solve_one_generation,comment_reomved, genetic_solve_one_generation_without_decoder

#Global Strategy Generator
strategy_generator = 0
strategy_lock = threading.Lock()

#Global Strategy Queue
strategy_queue = StrategyQueue()

#Global Logger
log_lock = threading.Lock()
strategy_handler_log = 0
result_log = 0

#Executor List
exec_dict = {}
exec_dict_lock = threading.Lock()

result_file = ""

init_population = []

class ProxyHandler(StreamRequestHandler):
	#Called on every new TCP connection
	def handle(self):
		instance = ""
		strategy = None
		gen = 1 
		exec_list = []
		before_hash  = []
		global init_population
		population = init_population

		# start from break point
		global strategy_queue
		i = 0
		while i > 0:
			strategy_queue.dequeue()
			i = i-1

		while True:
			# produce new strategy by genetic solve
			if strategy_queue.size() == 0:
				before_hash = []
				for ind in exec_list:
					before_hash.append(hash(ind+"\n"))
				population,offspring,priority_population = genetic_solve_one_generation_without_decoder(population=population,gen=gen,before_hash=before_hash)
				for ind in offspring:
					strategy_queue.enqueue(ind.to_file())
				gen += 1
			
			#Get Message
			msg = ""
			try:
				msg = self.rfile.readline()
			except Exception as e:
				print(e)
			if msg == "":
				#Connection Error!
				if strategy is not None:
					strategy_lock.acquire()
					strategy_lock.release()
				exec_dict_lock.acquire()
				if len(instance) > 0 and instance in exec_dict:
					del exec_dict[instance]
				exec_dict_lock.release()
				strategy_lock.acquire()
				strategy_handler_log.write("[%s] Executor (%s) failed\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
				print("[%s] Executor (%s) failed" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
				strategy_lock.release()
				break
			
			#Parse Message
			try:
				msg = eval(msg)
			except Exception as e:
				continue

			if msg['msg'] == 'READY':
				#New Strategy Request
				instance = msg['instance']
				#Check if Executor is new
				exec_dict_lock.acquire()
				if instance not in exec_dict:
					#New executor
					log_lock.acquire()
					strategy_handler_log.write("[%s] New Executor: %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
					print("[%s] New Executor: %s" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
					log_lock.release()
					exec_dict[instance] = []
				exec_dict_lock.release()
	
				#Get Next Strategy
				if strategy is None:
					strategy_lock.acquire()
					if strategy_queue.size() != 0:
						strategy = strategy_queue.dequeue()
						strategy = strategy.replace("\n","")
					else:
						strategy = None
					strategy_lock.release()
				else:
					pass

				#Check if Finished
				if strategy is None:
					log_lock.acquire()
					strategy_handler_log.write("[%s] Finished Testing\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
					print("[%s] Finished Testing" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
					log_lock.release()
					
					# wait strategy to produce
					msg = {'msg':'WAIT'}
					send_str = "%s\n"%(repr(msg))
					try:
						self.request.send(send_str.encode())
					except Exception as e:
						pass

					continue

				#Send strategy
				log_lock.acquire()
				strategy_handler_log.write("[%s] Executor (%s) testing strategy: %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, strategy))
				
				
				print("\n[%s] Executor (%s) testing strategy: %s" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, strategy))
				log_lock.release()
				msg = {'msg':'STRATEGY', 'data':strategy}
				send_str = "%s\n"%(repr(msg))
				try:
					self.request.send(send_str.encode())
				except Exception as e:
					#Connection Error!
					if strategy is not None:
						strategy_lock.acquire()
						# Strategy didn't exec
						strategy_queue.enqueue(strategy)
						strategy_lock.release()
					exec_dict_lock.acquire()
					del exec_dict[instance]
					exec_dict_lock.release()
					log_lock.acquire()
					strategy_handler_log.write("[%s] Executor (%s) failed\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
					print("[%s] Executor (%s) failed" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
					log_lock.release()
					break
			
			elif msg['msg']=="RESULT":
				#Testing Results
				res = msg['value']
				reason = msg['reason']
				feedback = msg['feedback']
				case_number = msg['casenumber']

				#Print Result
				log_lock.acquire()
				strategy_handler_log.write("[%s] Executor (%s) Result: %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, str(res)))
				strategy_handler_log.write("[%s] Executor (%s) Reason: %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, str(reason)))
				print("[%s] Executor (%s) Result: %s" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, str(res)))
				print("[%s] Executor (%s) Reason: %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance, str(reason)))
				
				# global result_file
				
				exec_list.append(strategy)
				log_lock.release()

				#Process Result
				strategy_lock.acquire()
				strategy_queue.strategy_feedback(strategy, feedback, res)
				strategy_queue.set_strategy_result(strategy,(res,reason))
				strategy_lock.release()

				#Clear Current Strategy
				strategy = None
			
			
			elif msg['msg'] == "FEEDBACK":
				#Testing Feedback
				data = msg['data']

				#Print Result
				log_lock.acquire()
				strategy_handler_log.write("[%s] Executor (%s) sent feedback...\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
				print("[%s] Executor (%s) sent feedback..." % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),instance))
				log_lock.release()

				#Process Result
				strategy_lock.acquire()
				# strategy_generator.strategy_feedback(strategy, data)
				strategy_lock.release()

			else:
				print("Unknown Message: %s" % msg)
			log_lock.acquire()
			strategy_handler_log.flush()
			log_lock.release()

	def write_to_file(self,f,strategy,case_number,res,reason):
		result_file = open( file = f,mode = 'a+', encoding = "utf-8")
		result_file.write("# test case {} \t result : {}\n".format(case_number,res))
		result_file.write("# excution situation : {}\n".format(reason))
		result_file.write(strategy+"\n")
		result_file.write("\n")

	def write_to_difference_file(self,f,strategy,case_number,reason):
		result_file = open( file = f,mode = 'a+', encoding = "utf-8")
		result_file.write("# test case {} \n".format(case_number))
		result_file.write("# excution situation : {}\n".format(reason))
		result_file.write(strategy+"\n")

		result_file.write("\n")


def main(args):
	global strategy_handler_log, result_lg, strategy_generator

    #Parse Args
	argp = argparse.ArgumentParser(description='Testing OFProxy Strategy Handler')

	argp.add_argument('-p','--port', type=int, default=3333)
	argp.add_argument('-c','--checkpoint', default="../log/checkpoint.ck")
	argp.add_argument('-r','--restore', action='store_true')
	argp.add_argument('-l','--load', default="")
	argp.add_argument('-o','--output',default="differences_strategy.txt")
	args = vars(argp.parse_args(args[1:]))
	if args['restore'] == True:
		mode = "a"
	else:
		mode = "w"
	print("Starting OFProxy Strategy Handler...")

	#Open Log file
	strategy_handler_log = open("../log/strategy.log", mode)
	strategy_handler_log.write("[%s] Starting Strategy Handler\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
	strategy_handler_log.flush()

	#Open Results File
	result_log = open("../log/results.log", mode)
	result_log.write("#Started %s\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
	result_log.flush()

	#Create Strategy Generator
	global strategy_queue
	global result_file
	strategy_generator = StrategyGenerator.StrategyGenerator()
	global init_population
	if len(args['load']) > 0:

		result_file = args['output']
		#Load fixed list of strategies
		print("Loading Strategies from File...")
		strategy_handler_log.write("[%s] Loading Strategies from File\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
		f = open(args['load'],"r")
		strategy_generator.load_from_file(f)
		strategy_queue = strategy_generator.strategy_queue
		init_population = comment_reomved(strategy_generator.strategy_list)
		f.close()
	else:
		#Generate Strategies
		print("Generating Strategies...")
		result_file = args['output']
		strategy_handler_log.write("[%s] Generating Strategies\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
		strategy_generator.build_strategies()
		
		strategy_queue = strategy_generator.strategy_queue
		strategy_file = open( file = "strategy.txt",mode = 'w', encoding = "utf-8")
		strategy_generator.write_to_file(strategy_file)
		init_population = comment_reomved(strategy_generator.strategy_list[200:210])

	#Restore, if needed
	if args['restore'] == True:
		ck = open(args['checkpoint'], "r")
		if strategy_generator.restore(ck) == False:
			return

	ThreadingTCPServer.allow_reuse_address = True
	server = ThreadingTCPServer(('',args['port']),ProxyHandler)
	server.serve_forever()

	#Close log
	strategy_handler_log.write("[%s] Close Strategy Handler\n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) + "\n")
	strategy_handler_log.close()
	result_log.close()

if __name__ == "__main__":
	main(sys.argv)