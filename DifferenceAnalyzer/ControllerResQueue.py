import os
import sys
import copy

class ControllerResQueue(object):
    def __init__(self,controller_type):
        self.__items = []
        self.controller_type = controller_type
       
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