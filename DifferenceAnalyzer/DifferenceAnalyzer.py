class DifferenceAnalyzer():
    def __init__(self,controller_result_queues):
        self.controller_result_queues = controller_result_queues
        self.compare_list = []

    def diffanalysis(self):
        difference = False
        i = 1
        print("compare_list",self.compare_list)
        while i < len(self.compare_list):
            compare_result = self.compare_list[0].controller_compare(self.compare_list[i])
            i += 1
            difference = difference or compare_result 
        return difference

    def allExec(self):
        for controller_result_queue in self.controller_result_queues:
            if controller_result_queue.size() == 0:
                return False
        return True
    
    def OnlyExec(self):
        exec_number = sum(controller_result_queue.size() for controller_result_queue in self.controller_result_queues)
        print("exec_number",exec_number)
        if exec_number == 1:
            return True
        else:        
            return False

    def notExec(self):
        for controller_result_queue in self.controller_result_queues:
            if controller_result_queue.size() != 0:
                return False
        return True
    
    def ControllerResultPrint(self):
        ryu_controller_result = None
        fl_controller_result = None
        onos_controller_result = None
        odl_controller_result = None
        for controller_result_queue in self.controller_result_queues:
            if controller_result_queue.controller_type == "ryu":
                ryu_controller_result = controller_result_queue.dequeue()
            elif  controller_result_queue.controller_type == "fl": 
                fl_controller_result = controller_result_queue.dequeue()
            elif  controller_result_queue.controller_type == "onos":
                onos_controller_result = controller_result_queue.dequeue()
            elif  controller_result_queue.controller_type == "odl":
                odl_controller_result = controller_result_queue.dequeue()
        if ryu_controller_result!= None or fl_controller_result != None or onos_controller_result != None or odl_controller_result != None:
            print("*****************OpenFlowCapture Controller Result******************")
        if ryu_controller_result != None:
            print("*****************Ryu Controller Result******************")
            ryu_controller_result.to_str()
        if fl_controller_result != None:
            print("*****************Floodlight Controller Result******************")
            fl_controller_result.to_str()
        if onos_controller_result != None:
            print("*****************ONOS Controller Result******************")
            onos_controller_result.to_str()
        if odl_controller_result != None:
            print("*****************OpenDaylight Controller Result******************")
            odl_controller_result.to_str()
        for controller_result_queue in self.controller_result_queues:
            if controller_result_queue.controller_type == "ryu" and ryu_controller_result!= None:
                controller_result_queue.enqueue(ryu_controller_result)
            elif  controller_result_queue.controller_type == "fl"and fl_controller_result!= None: 
                controller_result_queue.enqueue(fl_controller_result)
            elif  controller_result_queue.controller_type == "onos" and onos_controller_result!= None:
                controller_result_queue.enqueue(onos_controller_result )
            elif  controller_result_queue.controller_type == "odl" and odl_controller_result!= None:
                controller_result_queue.enqueue(odl_controller_result )

    def compareListBuild(self):
        self.compare_list = []
        for controller_result_queue in self.controller_result_queues:
            if controller_result_queue.size() != 0:
                controller_result = controller_result_queue.dequeue()
                self.compare_list.append(controller_result)

 