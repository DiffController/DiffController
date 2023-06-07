from MininetControl import MininetRunner
import time 
import threading

class MininetControl(threading.Thread):
    def __init__(self,ip,port,topology):
        super(MininetControl,self).__init__()
        self.ip = ip
        self.port = port
        self.topology = topology
        
    def run(self): 
        self.mininetrunner = MininetRunner(self.ip,self.port,self.topology)
        self.mininetrunner.mininet_control()

    def restart(self):
        self.mininetrunner = MininetRunner(self.ip,self.port,self.topology)
        self.mininetrunner.mininet_control()

    def stop(self):
        self.mininetrunner.set_finish_flag()

def MNControl(ip,port,topology):
    mininetrunner = MininetRunner(ip,port,topology)
    mininetrunner.mininet_control()
    time.sleep(20)
    mininetrunner.set_finish_flag()

def mncontrol(ip,port,topology):
    mininetrunner = MininetRunner(ip,port,topology)
    mininetrunner.mininet_control()
    time.sleep(20)
