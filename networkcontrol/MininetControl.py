import os
import subprocess
import time
import threading
import sys
import queue
import signal

class MininetIn(threading.Thread):
    def __init__(self,traget,process):
        self.process = process
        self.traget = traget
        self.process_alive = True
        super(MininetIn,self).__init__()

    def run(self):
        idleLoops=0 
        while self.process_alive == True:
            self.traget(self.process,idleLoops)
            idleLoops += 1
            if idleLoops > 500:
                idleLoops = 0
                time.sleep(0.01)

    def stop(self):
        self.process_alive = False 

class MininetRunner:
    def __init__(self,ip,port,topo_file):
        self.process = None
        self.q_out = queue.Queue()
        self.q_in = queue.Queue()
        self.finish_flag = False
        self.before_test = False
        self.after_test = False
        self.ip = ip
        self.port = port
        self.topo_file = topo_file


    def enqueue_stream(self, stream, queue, type):
        for line in iter(stream.readline,b''):
            queue.put(str(type) + line.decode('utf-8'))
        stream.close()
    
    def consoleLoop(self,process,idleLoops):
        if not self.q_out.empty():
            line = self.q_out.get()
            sys.stdout.write(line[1:])
            sys.stdout.flush()
        else:
            if idleLoops >= 500:
                inputCmd = "pingall\n"
                self.q_in.put(inputCmd)
                if self.process.poll() == None:
                    process.stdin.write(inputCmd.encode('utf-8'))
                    process.stdin.flush()

    def run_mininet_process(self):
        command = 'exec sudo mn --switch ovs,protocols=OpenFlow13 --mac --controller remote,ip='+self.ip+',port='+self.port+' --custom ./topology/'+self.topo_file+' --topo mytopo'
        self.process = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                                        ,preexec_fn=os.setpgrp,close_fds=True)
        self.mininetin = MininetIn(self.consoleLoop,self.process)
        self.mininetin.setName("set_miminet_in")
        self.mininetin.setDaemon(True)
        self.mininetin.start()

    def operate_mininet_cli_process(self):
        while True:
            time.sleep(0.1)
            if self.before_test == True:
                inputCmd = " dpctl dump-flows -O OpenFlow13"+'\n'
                self.process.stdin.write(inputCmd.encode('utf-8'))
                self.process.stdin.flush()
            if self.after_test == True:
                inputCmd = " dpctl dump-flows -O OpenFlow13"+'\n'
                self.process.stdin.write(inputCmd.encode('utf-8'))
                self.process.stdin.flush()
            if self.before_test == True and self.after_test == True:
                break

    def stop_mininet_process(self):
        while True:
            time.sleep(0.1)
            if self.finish_flag == True:
                self.mininetin.stop()
                if (self.mininetin.is_alive() == False):
                    os.killpg(self.process.pid, signal.SIGTERM)
                    if self.process.poll() == -15:
                        self.finish_flag = False
                        break

    def mininet_control(self):
        self.tstart =  threading.Thread(target=self.run_mininet_process,name="run_mininet")
        self.tstop = threading.Thread(target=self.stop_mininet_process,name="stop_mininet")
        self.tstart.setDaemon(True)
        self.tstart.start()
        self.tstop.start()

    def set_finish_flag(self):
        self.finish_flag = True

    def set_before_test(self):
        self.before_test = True

    def set_after_test(self):
        self.after_test = True
    

q_out = queue.Queue()
q_in = queue.Queue()
global process

""" restore std output & std error output into queue q"""
def enqueue_stream(stream, queue, type):
    for line in iter(stream.readline,b''):
        queue.put(str(type) + line.decode('utf-8'))
    stream.close()

"""show the output of mininet """
def consoleLoop(process):
    idleLoops=0
    while True:
        if not q_out.empty():
            line = q_out.get()
            sys.stdout.write(line[1:])
            sys.stdout.flush()
        else:
            time.sleep(0.01)
            if idleLoops >= 5:
                idleLoops = 0
                inputCmd = input('mininet>')+'\n'
                q_in.put(inputCmd)
                if "exit"+'\n' == inputCmd:
                    break
                process.stdin.write(inputCmd.encode('utf-8'))
                process.stdin.flush()
                continue
            idleLoops += 1

def run_mininet_process():
    command = 'sudo mn --switch ovs,protocols=OpenFlow13 --mac --controller remote,ip=172.17.0.2,port=6653 --custom /home/zc/mininet/custom/sametopo2.py --topo mytopo'
    global process
    process = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    threadout = threading.Thread(target=enqueue_stream,args=(process.stdout,q_out,1))
    threaderr = threading.Thread(target=enqueue_stream,args=(process.stderr,q_out,2))
    threadin = threading.Thread(target=consoleLoop,args=(process,))
    threadout.setDaemon(True)
    threaderr.setDaemon(True)
    threadin.setDaemon(True)

    threadout.start()
    threaderr.start()
    threadin.start()
    threadin.join()

def operate_mininet_cli():
    global process
    time.sleep(10)
    inputCmd = "dpctl dump-flows -O OpenFlow13"
    process.stdin.write(inputCmd.encode('utf-8'))
    process.stdin.flush()
    time.sleep(10)
    inputCmd = "dpctl dump-flows -O OpenFlow13"
    process.stdin.write(inputCmd.encode('utf-8'))
    process.stdin.flush()

def stop_mininet_process():
    time.sleep(30)
    global process
    process.kill()
    process.wait()



if __name__ == "__main__":

    threadstart =  threading.Thread(target=run_mininet_process,name="run_mininet")
    threadoperatecli = threading.Thread(target=operate_mininet_cli)
    threadstop = threading.Thread(target=stop_mininet_process,name="stop_mininet")
    threadstart.setDaemon(True)
    threadoperatecli.setDaemon(True)
    threadstop.setDaemon(True)

    threadstart.start()
    threadoperatecli.start()
    threadstop.start()

    threadstop.join()