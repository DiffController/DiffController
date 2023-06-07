class ControllerResult:
    """the Controller result is represent for switch compare result before & after test"""

    def __init__(self,controller_type):
        self.controller_type = controller_type
        self.switch_change:tuple = ('unchange', '', '')
        self.port_change:tuple  = ('unchange', '', '')
        self.link_change:tuple  = ('unchange', '', '')
        self.host_change:tuple  = ('unchange', '', '')

        self.flow_length_change:tuple = ('unchange', '', '')
        self.group_length_change:tuple = ('unchange', '', '')
        self.meter_length_change:tuple = ('unchange', '', '')
        self.flow_length_in_storage_change:tuple = ('unchange', '', '')
        self.group_length_in_storage_change:tuple = ('unchange', '', '')
        self.meter_length_in_storage_change:tuple = ('unchange', '', '')
        self.switches_change:tuple = ('unchange', '', '')
    
    def to_str(self):
        print("1.switch change: {}".format(self.switch_change))
        print("2.port change: {}".format(self.port_change))
        print("3.link change: {}".format(self.link_change))
        print("4.host change: {}".format(self.host_change))
        print("5.flow length change: {}".format(self.flow_length_change))
        print("6.group length change: {}".format(self.group_length_change))
        print("7.meter length change: {}".format(self.meter_length_change))
        print("8.flow length in storage change: {}".format(self.flow_length_in_storage_change))
        print("9.group length in storage change: {}".format(self.group_length_in_storage_change))
        print("10.meter length in storage change: {}".format(self.meter_length_in_storage_change))
        print("11.switches ip and port change: {}".format(self.switches_change))

    def to_file(self):
        controller_result = ""
        controller_result = controller_result + "#####################################################\n"
        controller_result = controller_result + "# switch change : {}\n".format(self.switch_change)
        controller_result = controller_result + "# port change: : {}\n".format(self.port_change)
        controller_result = controller_result + "# list change: : {}\n".format(self.link_change)
        controller_result = controller_result + "# host change: : {}\n".format(self.host_change)
        controller_result = controller_result + "# flow change: : {}\n".format(self.flow_length_change)
        controller_result = controller_result + "# group change: : {}\n".format(self.group_length_change)
        controller_result = controller_result + "# meter change: : {}\n".format(self.meter_length_change)
        controller_result = controller_result + "# switches pairs change: : {}\n".format(self.switches_change)
        controller_result = controller_result + "#####################################################\n"
        return controller_result

    def controller_compare(self,other):
        if self.switch_change == None or other.switch_change == None:
            return False
        elif self.port_change == None or other.port_change  == None:
            return False
        elif self.link_change == None or other.link_change  == None:
            return False
        elif self.flow_length_change == None or other.flow_length_change  == None:
            return False
        elif self.group_length_change == None or other.group_length_change  == None:
            return False
        elif self.meter_length_change == None or other.meter_length_change  == None:
            return False
        elif self.flow_length_in_storage_change == None or other.flow_length_in_storage_change  == None:
            return False
        elif self.group_length_in_storage_change == None or other.group_length_in_storage_change  == None:
            return False
        elif self.meter_length_in_storage_change == None or other.meter_length_in_storage_change  == None:
            return False
        elif self.switches_change == None or other.switches_change  == None:
            return False


        if self.switch_change[0] != other.switch_change[0]:
            return True
        elif self.port_change != other.port_change:
            return True
        elif self.link_change != other.link_change:
            return True
        # elif self.host_change != other.host_change:
        #     return True 
        elif self.flow_length_change[0] != other.flow_length_change[0] or self.flow_length_change[1] != other.flow_length_change[1]:
            return True
        elif self.group_length_change[0] != other.group_length_change[0] or self.group_length_change[1] != other.group_length_change[1]:
            return True
        elif self.meter_length_change[0] != other.meter_length_change[0] or self.meter_length_change[1] != other.meter_length_change[1]:
            return True
        elif self.flow_length_in_storage_change[0] != other.flow_length_in_storage_change[0] or self.flow_length_in_storage_change[1] != other.flow_length_in_storage_change[1]:
            return True
        elif self.group_length_in_storage_change[0] != other.group_length_in_storage_change[0] or self.group_length_in_storage_change[1] != other.group_length_in_storage_change[1]:
            return True
        elif self.meter_length_in_storage_change[0] != other.meter_length_in_storage_change[0] or self.meter_length_in_storage_change[1] != other.meter_length_in_storage_change[1]:
            return True
        elif self.switches_change[0] != other.switches_change[0]:
            return True
        else:
            return False