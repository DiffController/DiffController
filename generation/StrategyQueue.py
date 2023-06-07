import os
import sys
import copy
sys.path.append(os.getcwd()+"/generation")

def rreplace(self, old, new, *max):
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0] 
        while count:
            index = self.rfind(old)
            if index >= 0:
                chunk = self.rpartition(old)
                self = chunk[0] + new + chunk[2] 
                count -= 1
    return self

def get_strategy_priority(self):
    new_strategy_str = copy.deepcopy(self)
    new_strategy_str = new_strategy_str.replace('[', '',1) 
    new_strategy_str = rreplace(new_strategy_str,']','',1)
    strategy_slice = new_strategy_str.split(",",maxsplit=4)
    priority = strategy_slice[0]
    return int(priority)

class StrategyQueue(object):
    def __init__(self):
        self.__items = []
        self.__strategy_res_mapper = {}
    
    def if_empty(self):
        return self.__items == []

    def enqueue(self,item):
        self.__items.append(item)

    def dequeue(self):
        if self.__items == []:
            return None
        else:
            # queue is FIFO
            return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def queue_item_print(self):
        for item in self.__items:
            print(item)
    
    def mapper_print(self):
        print("mapper",self.__strategy_res_mapper)

    def queue_item_sort(self):
        self.__items.sort(key=get_strategy_priority,reverse=True)

    def strategy_feedback(self,strategy, feedback, res):
        pass

    def get_strategy_result(self,strategy):
        if strategy in self.__strategy_res_mapper.keys():
            res = self.__strategy_res_mapper[strategy]
            return (res[0],res[1],res[2])
        else:
            return (False,"Not finish test",[])

    def set_strategy_result(self,strategy,res):
        self.__strategy_res_mapper[strategy] = res