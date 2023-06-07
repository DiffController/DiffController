import os
import string
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/generation")

import OpenFlowMessageStruct
import OpenFlowAction
import random
from random import choice
from random import sample
import binascii
from interval3 import Interval
from interval3 import IntervalSet
from ast import literal_eval
from StrategyQueue import StrategyQueue
import json

def is_list(s):
    try:
        s = s.strip()
        if s.startswith("[") and s.endswith("]"):
            literal_eval(s)
            return True
    except ValueError:
        pass
    return False

def sample_list(list):
    return random.choice(list)

def list_to_interval(list_str):
    if is_list(list_str):
        orignal_list = literal_eval(list_str)
    else:
        orignal_list = []
    interval_list = []
    for interval in  orignal_list:
       left =  interval[0]
       right =  interval[1]
       interval_list.append(Interval(left,right))
    return IntervalSet(interval_list)

def duplicate_removal(oraginal_list):
    dup_removal_list = []
    dup_removal_list = list(set(oraginal_list))
    dup_removal_list.sort()
    return dup_removal_list


def process_by_interval(defined_set,undefined_set):
    select_defined_value = 0
    select_undefined_value = 0
    defined_value_list = []
    undefined_value_list = [] 
    endpoint_list = [] 
    for defined_interval in defined_set:
        if defined_interval.lower_closed:
            left = defined_interval.lower_bound
        else:
            left = defined_interval.lower_bound + 1
        if defined_interval.upper_closed:
            right = defined_interval.upper_bound
        else:
            right = defined_interval.upper_bound - 1
        if left <= right:
            ran = random.randint(left,right)
        else:
            ran = right
        defined_value_list.append(ran)
        endpoint_list.append(defined_interval.lower_bound)
        endpoint_list.append(defined_interval.upper_bound)
    select_defined_value = sample_list(defined_value_list)

    for undefined_interval in undefined_set:
        if undefined_interval.lower_closed:
            left = undefined_interval.lower_bound
        else:
            left = undefined_interval.lower_bound + 1
        if undefined_interval.upper_closed:
            right = undefined_interval.upper_bound
        else:
            right = undefined_interval.upper_bound - 1
        if left <= right:
            ran = random.randint(left,right)
        else:
            ran = right
        undefined_value_list.append(ran)
        endpoint_list.append(undefined_interval.lower_bound)
        endpoint_list.append(undefined_interval.upper_bound)
    select_undefined_value = sample_list(undefined_value_list)
    dup_removal_endpoint = duplicate_removal(endpoint_list)
    select_end_point = sample_list(dup_removal_endpoint)

    return sample_list([hex(select_defined_value)])

# reverse replace
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

class Strategy:
    def __init__(self):
        self.pkt_type:str or None = None
        self.field:str or None = None 
        self.action:str or None = None 
        self.priority:int = 0

        self.was_fuzzed = False
        self.perf_score = 2000
        self.source_dict = {"priority":0,"population":0}
        self.no_good_count = 0 # no good count > 5 , strategy drop from population
        self.has_child = False
        self.saved_reason = '0'
        self.first_added_time = 0 # which gen
        self.hash = 0
        self.depth = 0
        self.mutate_weight = 2

    def to_str(self):
        strategy = "strategy:pkt_type={},field={},action={},priority={}".format(
            self.pkt_type,self.field,self.action,self.priority
        )
        return strategy 
    

    def to_file(self):
        strategy = "[{},{},{},{}]\n".format(
            self.priority,self.pkt_type,self.field,self.action
        )
        return strategy
    
    def get_action_list_len(self):
        action_list = self.action.split("|")
        return len(action_list)

    def mutate(self): 
        action_list = self.action.split("|")
        new_action_list = []
        for item in action_list:
            if item == "":
                continue
            action_type = item.split(",",1)[0]
            action_parmeter = item.split(",",1)[1]
            if action_type == "DELAY":
                new_action_list.append(action_type+",s={}".format(str(random.randint(1,20))))
            elif action_type == "DUP":
                new_action_list.append(action_type+",n={}".format(str(random.randint(1,20))))
            elif action_type == "MOD":
                msg_type = self.pkt_type
                field = re.findall('field=\(.*?\)',action_parmeter)[0]
                field = field.split("=")[1]
                field = field.replace('(', '')
                field = field.replace(')', '')
                value = re.findall('val=\(.*?\)',action_parmeter)[0]
                value = value.split("=")[1]
                value = value.replace('(', '')
                value = value.replace(')', '')
                (field_type,field_range) = self.find_msg_field_struct(msg_type,field)
                stra_gen = StrategyGenerator()
                if field_range == None:
                    new_value = stra_gen.process_by_type_range(field_type,"")
                else:
                    new_value = stra_gen.process_by_type_range(field_type,field_range)
                new_action_par = action_parmeter.replace(value,new_value,1)
                new_action_list.append(action_type+","+new_action_par)
            elif action_type == "ADD":
                stra_gen = StrategyGenerator()
                msg_type = self.pkt_type
                block = re.findall('field=\(.*?\)',action_parmeter)[0]
                block = block.split("=")[1]
                block = block.replace('(', '')
                block = block.replace(')', '')
                dict_value = self.get_add_para(action_parmeter)
                block_struct = self.find_msg_block_strcut(self.pkt_type,block)
                mutate_sites = self.choose_random_list(dict_value.keys())
                for mutate_key in mutate_sites:
                    (field_type,field_range) = self.find_field_type_range(block_struct,mutate_key)
                    if field_range == None:
                        new_value = stra_gen.process_by_type_range(field_type,"")
                    else:
                        new_value = stra_gen.process_by_type_range(field_type,field_range)
                    value = dict_value.get(mutate_key)
                    if value == 0 or type(value) == list:
                        old_k_v = "\'"+mutate_key+"\': "+str(value)
                    else:
                        old_k_v = "\'"+mutate_key+"\': \'"+str(value)+'\''
                    if new_value == 0 or type(new_value) == list:    
                        new_k_v = "\'"+mutate_key+"\': "+str(new_value)
                    else:
                        new_k_v = "\'"+mutate_key+"\': \'"+str(new_value)+'\''
                    action_parmeter = action_parmeter.replace(old_k_v,new_k_v,1)
        
                # drop some of fields in ADD action parameter
                drop_sites = []
                drop_pending_sites = self.choose_random_list(dict_value.keys())
                for item in drop_pending_sites:
                    if "match" in item or "action" in item or "instruction" in item:
                        drop_sites.append(item)
                
                for drop_key in drop_sites:
                    value = dict_value.get(drop_key)
                    if len(dict_value.keys())==1 and value == 0 or type(value) == list:
                        old_k_v = "\'"+drop_key+"\': \'"+str(value) 
                    elif len(dict_value.keys())==1:
                        old_k_v = "\'"+drop_key+"\': \'"+str(value) +'\''
                    elif value == 0 or type(value) == list:
                        old_k_v = "\'"+drop_key+"\': "+str(value) +", " 
                    else:
                        old_k_v = "\'"+drop_key+"\': \'"+str(value) +'\''+", "
                    
                    action_parmeter = action_parmeter.replace(old_k_v,"",1)

                # add some of fields in ADD action parameter            
                new_block_value = stra_gen.construct_block(msg_type)
                add_dict = {}
                for key,value in new_block_value.items():
                    if key not in dict_value.keys():
                        add_dict[key] = value
                
                add_sites =  add_dict.keys()
                
                for new_key,new_value in add_dict.items():
                    if new_value == 0 or type(new_value) == list:    
                        new_k_v = "{\'"+new_key+"\': "+str(new_value)+", "
                    else:
                        new_k_v = "{\'"+new_key+"\': \'"+str(new_value)+'\', '
                    action_parmeter = action_parmeter.replace("{",new_k_v,1)
                new_action_list.append(action_type+","+action_parmeter)

            elif action_type == "BUILD":
                stra_gen = StrategyGenerator()
                build_type = re.findall('type=\(.*?\)',action_parmeter)[0]
                build_type = build_type.split("=")[1]
                build_type = build_type.replace('(', '')
                build_type = build_type.replace(')', '')
                build_type = build_type.split("_",1)[1]
                build_type = "of_"+ build_type
                dict_value = self.get_build_para(action_parmeter)
                msg_struct = self.find_msg_struct(build_type)
                """ get unfold msg struct """
                msg_field_struct = self.build_field_list(msg_struct)

                """ get unfold strategy (k,v) """
                msg_field_value_list = self.build_field_value_list(dict_value)

                """ get mutation strategy (k,v) """
                mutate_sites = self.choose_random_field(msg_field_value_list)

                # mutate some of fields in BUILD action parameter
                for mutate_key in mutate_sites:
                    (field_type,field_range) = self.find_entire_field_type_range(msg_field_struct,mutate_key)
                    
                    if field_range == None:
                        new_value = stra_gen.process_by_type_range(field_type,"")
                    else:
                        new_value = stra_gen.process_by_type_range(field_type,field_range)
                    value = self.field_value_get(msg_field_value_list,mutate_key)
                    if value == 0 or type(value) == list:
                        old_k_v = "\'"+mutate_key.split(".")[-1]+"\': "+str(value)
                    else:
                        old_k_v = "\'"+mutate_key.split(".")[-1]+"\': \'"+str(value)+'\''
                    if new_value == 0 or type(new_value) == list:    
                        new_k_v = "\'"+mutate_key.split(".")[-1]+"\': "+str(new_value)
                    else:
                        new_k_v = "\'"+mutate_key.split(".")[-1]+"\': \'"+str(new_value)+'\''
                    action_parmeter = action_parmeter.replace(old_k_v,new_k_v,1)
            
                # drop some of fields in BUILD action parameter
                drop_pending_sites = self.choose_random_field(msg_field_value_list)
                drop_sites = []
                
                """reacquire msg field value list"""
                dict_value = self.get_build_para(action_parmeter)
                msg_field_value_list = self.build_field_value_list(dict_value)

                for item in drop_pending_sites:
                    if "match" in item or "action" in item or "instruction" in item:
                        drop_sites.append(item)
                for drop_key in drop_sites:
                    value = self.field_value_get(msg_field_value_list,drop_key)
                    if value == 0 or type(value) == list:
                        old_k_v = "\'"+drop_key.split(".")[-1]+"\': "+str(value) 
                    else:
                        old_k_v = "\'"+drop_key.split(".")[-1]+"\': \'"+str(value) +'\''
                    
                    if old_k_v+", " in self.action[1]:
                        action_parmeter = action_parmeter.replace(old_k_v+", ","",1)
                    elif old_k_v in self.action[1]:
                        action_parmeter = action_parmeter.replace(", "+old_k_v,"",1)
                    
                # add some of fields in BUILD action parameter
                """reacquire msg field value list"""
                dict_value = self.get_build_para(action_parmeter)
                msg_field_value_list = self.build_field_value_list(dict_value)
                new_build_value = stra_gen.process_by_msg_type(build_type)
                new_msg_field_value_list = self.build_field_value_list(new_build_value)
                add_dict = {}
                add_dict = self.diff_list(msg_field_value_list,new_msg_field_value_list)

                for new_key,new_value in add_dict.items():
                    if new_value == 0 or type(new_value) == list:
                        new_k_v = "\'"+new_key.split(".")[-2]+"\': [{\'"+new_key.split(".")[-1]+"\': "+str(new_value)+", "
                    else:
                        new_k_v = "\'"+new_key.split(".")[-2]+"\': [{\'"+new_key.split(".")[-1]+"\': \'"+str(new_value)+'\', '
                    old_k_v = "\'"+new_key.split(".")[-2]+"\': [{"
                    action_parmeter = action_parmeter.replace(old_k_v,new_k_v,1)
                new_action_list.append(action_type+","+action_parmeter)
        new_action_str = ""
        new_action_str = "|".join(new_action_list)
        self.action = new_action_str

    def mutate_action_list(self):
        add_probality   = 0.5
        del_probality   = 0.4
        keep_probality   = 0.1
        strategy_Gen = StrategyGenerator()

        random_float = random.random()
        action_list = self.action.split("|")
        new_action_list = []

        if 0 < random_float and random_float <= 0.5:
            for item in action_list:
                new_action_list.append(item)
            action_str_list = strategy_Gen.build_action_by_type(self.pkt_type)
            chosed_action_str_list = sample(action_str_list,1)
            for item in chosed_action_str_list:
                new_action_list.append(item)
            new_action_str = "|".join(new_action_list)
            self.action = new_action_str
        elif 0.5 < random_float and random_float <= 0.9:
            
            random_index  = random.randint(0,len(action_list)-1)
            
            del action_list[random_index]
            for item in action_list:
                new_action_list.append(item)

            new_action_str = "|".join(new_action_list)
            self.action = new_action_str
        else:
            pass

    def find_msg_struct(self,msg_type):
        msg_struct = []
        for msg in OpenFlowMessageStruct.openflow_13:
            if msg[0] == msg_type:
                msg_struct = msg[1]
                break
        return msg_struct

    def find_field_type_range(self,query_msg_struct,name):
        for f in query_msg_struct:
            if f.get("name") == name:
                field_type = f.get("type")
                field_range = f.get("range")
                break
            else:
                field_type = ""
                field_range = ""
        return (field_type,field_range)

    def find_entire_field_type_range(self,query_msg_struct,query_field):
        for f in query_msg_struct:
            if f.get("field") == query_field:
                field_type = f.get("type")
                field_range = f.get("range")
                break
            else:   
                field_type = ""
                field_range = ""
        return (field_type,field_range)

    def find_msg_field_struct(self,msg_type,field):
        msg_struct = self.find_msg_struct(msg_type)
        fields = self.build_field_list(msg_struct)
        result = ("","")
        for f in fields:
            if field == f.get("field"):
                result = (f.get("type"),f.get("range"))
        return result

    def find_msg_block_strcut(self,msg_type,block):
        msg_struct = self.find_msg_struct(msg_type)
        if "." in block:
            block_key = block.split(".")
            if block == "match.match":
                block_key.append("oxm_list")
        else:
            block_key = block
        if len(block_key) == 1 :
            for field in msg_struct:
                if field.get("name") == block_key:
                    block_struct = field.get("fields")
        elif len(block_key) == 2:
            for field_one in msg_struct:
                if field_one.get("name") == block_key[0]:
                    msg_struct_nest1 = field_one.get("fields")
                    for field_two in msg_struct_nest1:
                        if field_two.get("name") == block_key[1]:
                            block_struct = field_two.get("fields")
        elif len(block_key) == 3:
            for field_one in msg_struct:
                if field_one.get("name") == block_key[0]:
                    msg_struct_nest1 = field_one.get("fields")
                    
                    for field_two in msg_struct_nest1:
                        if field_two.get("name") == block_key[1]:
                            msg_struct_nest2 = field_two.get("fields")
                            for field_three in msg_struct_nest2:
                                if field_three.get("name") == block_key[2]:
                                    block_struct = field_three.get("fields")
        elif len(block_key) == 4:
            for field_one in msg_struct:
                if field_one.get("name") == block_key[0]:
                    msg_struct_nest1 = field_one.get("fields")
                    for field_two in msg_struct_nest1:
                        if field_two.get("name") == block_key[1]:
                            msg_struct_nest2 = field_one.get("fields")
                            for field_three in msg_struct_nest2:
                                if field_three.get("name") == block_key[2]:
                                    msg_struct_nest3 = field_three.get("fields")
                                    for field_four in msg_struct_nest3:
                                        if field_four.get("name") == block_key[3]:
                                            block_struct = field_four.get("fields")
        else:
            block_struct = []
        
        return block_struct
    

    def build_field_value_list(self,strategy_para_dict):
        field_value_list = []
        for key,value in strategy_para_dict.items():
            field_value = {}
            if type(value) == dict:
                return_list = self.build_field_value_list(value)
                for item in return_list:
                    field_value = {}
                    field_value["field"] = key+ "." + item['field']
                    field_value["value"] = item["value"]
                    field_value_list.append(field_value)
                return field_value_list
            elif type(value) == list:
                return_list = self.build_field_value_list(value[0])
                for item in return_list:
                    field_value = {}
                    field_value["field"] = key+ "." + item['field']
                    field_value["value"] = item["value"]
                    field_value_list.append(field_value)
                return field_value_list
            else:
                field_value["field"] = key
                field_value["value"] = value
                field_value_list.append(field_value)
        return field_value_list

    def field_value_get(self,msg_field_value_list,mutate_key):
        for item in msg_field_value_list:
            if item["field"] == mutate_key:
                return item["value"]
        return None


    def build_field_list(self,message_body):
        filed_list = []
        if len(message_body)==1 and 'type' in message_body[0] and (message_body[0]['type']=='list' or message_body[0]['type']=='TLV'):
            #Lists
            l = self.build_field_list(message_body[0]['fields'])
            iterations = 3
            if('max' in message_body[0]):
                iterations = message_body[0]['max']
            for i in range(1,iterations + 1):
                for elm in l:
                    filed_list.append({'field':message_body[0]['name'] + "." + elm['field'], 'type':elm['type']})
        else:
            # Normal structures
            for i,f in enumerate(message_body):
                string = str(i + 1)
                # Ignore fields we can't change
                if 'impl' in f and f['impl'] is False:
                    continue
                # Subfields
                if 'fields' in f:
                    l = self.build_field_list(f['fields'])
                    for i in l:
                        filed_list.append({'field': f['name']+ "." + i['field'], 'type':i['type']})
                else:
                    if 'range' in f:
                        filed_list.append({'field':f['name'], 'type':f['type'],'range':f['range']})
                    else:
                        filed_list.append({'field':f['name'], 'type':f['type']})
        return filed_list
    
    def choose_random_list(self,old_list):
        new_list = []
        ran_num = random.randint(0,len(old_list))
        for item in sample(old_list,ran_num):
            new_list.append(item)
        return new_list

    def choose_random_field(self,msg_field_value_struct):
        new_list = []
        mutatation_list = []
        ran_num = random.randint(0,len(msg_field_value_struct))
        for item in sample(msg_field_value_struct,ran_num):
            new_list.append(item)
        for item in new_list:
            mutatation_list.append(item.get("field"))
        return mutatation_list

    def get_add_para(self,action_para):
        value = re.findall('val=\(.*?\)',action_para)[0]
        value = value.split("=")[1]
        value = value.replace('(', '')
        value = value.replace(')', '')
        """convert quotes to double quotes"""
        str_value = value.replace("'", '"')
        dict_value = json.loads(str_value)
        return dict_value

    def get_build_para(self,action_para):
        value = re.findall('val=\(.*?\)',action_para)[0]
        value = value.split("=")[1]
        value = value.replace('(', '')
        value = value.replace(')', '')
        """convert quotes to double quotes"""
        value = value.replace("'", '"')
        """load can not convert 16 list"""
        dict_value = json.loads(value)
        return dict_value

    def diff_list(self,list1,list2):
        old_key_list = []
        diff_value = {}
        for item in list1: 
            old_key_list.append(item.get("field"))
        for item in list2: 
            if item.get("field") not in old_key_list:
                if "match" in item.get("field") or "action" in item.get("field") or "instruction" in item.get("field"):
                    diff_value[item.get("field")] = item.get('value')
        return diff_value

class StrategyGenerator:
    
    #Constructor
    def __init__(self):
        self.strategy_list = []
        self.strat_ptr = 0
        self.strategy_queue = StrategyQueue()
    
    def strategy_process(self,strategy_str):
        strategy = Strategy()
        strategy_str = strategy_str.replace('[', '',1) 
        strategy_str = rreplace(strategy_str,']','',1)
        strategy_slice = strategy_str.split(",",maxsplit=3)
        strategy.priority = strategy_slice[0]
        strategy.pkt_type = strategy_slice[1]
        strategy.field = strategy_slice[2]
        action_list_str = strategy_slice[3]
        strategy.action = action_list_str
        return strategy

    def build_strategies(self):
        for pkt in OpenFlowMessageStruct.openflow_13_occur:
            print("create strategies for {} OpenFlow Message".format(pkt[0]))
            msg_type = pkt[0]
            message_body = pkt[1]
            
            self.strategy_list.append("# {}".format(msg_type))

            #Transmission Strategies
            for action in OpenFlowAction.message_transmission_actions:
                if action[0] == "BUILD":
                    strategy = Strategy()
                    strategy.pkt_type = msg_type
                    strategy.field  = "*"
                    strategy.action = action[1].format(msg_type)
                    strategy.priority = 0
                    self.strategy_list.append(strategy)
                    self.strategy_queue.enqueue(strategy.to_file())
                else:
                    for par in action[2]:
                        strategy = Strategy()
                        strategy.pkt_type = msg_type
                        strategy.field  = "*"
                        strategy.action = action[1].format(par)
                        strategy.priority = 0
                        self.strategy_list.append(strategy)
                        self.strategy_queue.enqueue(strategy.to_file())
            
            # Modification Strategies
            fields = self.build_field_list(message_body)
            for field in fields:
                for action in OpenFlowAction.message_modify_actions:
                    for operation in OpenFlowAction.field_operation:
                        
                        strategy = Strategy()
                        strategy.pkt_type = msg_type
                        strategy.field  = "*"
                        field_type = field['type']
                        select_value = self.process_by_type_range(field_type,"")
                        strategy.action = action[1].format(field['field'],select_value)
                        strategy.priority = 0
                        self.strategy_list.append(strategy)
                        self.strategy_queue.enqueue(strategy.to_file())
        
        # block Strategies
        for pkt in OpenFlowMessageStruct.openflow_13_block:
            print("create block strategies for {} OpenFlow Message".format(pkt[0]))
            msg_type = pkt[0]
            message_body = pkt[1]
           
            self.strategy_list.append("# {}".format(msg_type)) 

            
            # Block Strategies 
            fields = self.build_field_list(message_body)
            block_list = self.build_block_list(fields)      
            if len(block_list) != 0:
                for block in block_list:
                    for action in OpenFlowAction.message_block_actions:
                        if action[0] == "DEL":
                            strategy = Strategy()
                            strategy.pkt_type = msg_type
                            strategy.field  = "*"
                            strategy.action = action[1].format(block)
                            strategy.priority = 0
                            self.strategy_list.append(strategy)
                            self.strategy_queue.enqueue(strategy.to_file())
                        else:
                            strategy = Strategy()
                            strategy.pkt_type = msg_type
                            strategy.field  = "*"
                            block_value = self.construct_block(msg_type)
                            strategy.action = action[1].format(block,block_value)
                            strategy.priority = 0
                            self.strategy_list.append(strategy)
                            self.strategy_queue.enqueue(strategy.to_file())

        # build Strategies
        for pkt in OpenFlowMessageStruct.openflow_13_occur:
            print("create build strategies for {} OpenFlow Message".format(pkt[0]))
            msg_type = pkt[0]
            message_body = pkt[1]
            
            self.strategy_list.append("# {}".format(msg_type)) 
            for action in OpenFlowAction.message_build_actions:
                for build_pkt in OpenFlowMessageStruct.openflow_13:
                    build_msg_type = build_pkt[0]
                    build_value = self.process_by_msg_type(build_msg_type)
                    strategy = Strategy()
                    strategy.pkt_type = msg_type
                    strategy.field  = "*"
                    strategy_action_str = action[1].format(build_msg_type,build_value)
                    strategy.action = strategy_action_str
                    self.strategy_list.append(strategy)
                    self.strategy_queue.enqueue(strategy.to_file())


    def build_field_list(self,message_body):
        filed_list = []
        if len(message_body)==1 and 'type' in message_body[0] and (message_body[0]['type']=='list' or message_body[0]['type']=='TLV'):
            #Lists
            l = self.build_field_list(message_body[0]['fields'])
            iterations = 3
            if('max' in message_body[0]):
                iterations = message_body[0]['max']
            for i in range(1,iterations + 1):
                for elm in l:
                    filed_list.append({'field':message_body[0]['name'] + "." + elm['field'], 'type':elm['type']})
        else:
            #Normal structures
            for i,f in enumerate(message_body):
                string = str(i + 1)
                #Ignore fields we can't change
                if 'impl' in f and f['impl'] is False:
                    continue
                #Subfields
                if 'fields' in f:
                    l = self.build_field_list(f['fields'])
                    for i in l:
                        filed_list.append({'field': f['name']+ "." + i['field'], 'type':i['type']})
                else:
                    if 'range' in f:
                        filed_list.append({'field':f['name'], 'type':f['type'],'range':f['range']})
                    else:
                        filed_list.append({'field':f['name'], 'type':f['type']})
        return filed_list

    def build_block_list(self,filed_list):
        block_list = []
        for item in filed_list:
            if len(item['field'].split('.')) == 3 :
                item_slice = item['field'].split('.')
                block_list.append(item_slice[0]+"."+item_slice[1])
            elif len(item['field'].split('.')) == 4 :
                item_slice = item['field'].split('.')
                block_list.append(item_slice[0]+"."+item_slice[1])
        block_list = list(set(block_list))
        return block_list

    def construct_block(self,msg_type):

        block_value = dict()

        block = OpenFlowMessageStruct.block_field[msg_type]['add_value']
        
        for item in block:
            if 'value' in item.keys():
                block_value[item['name']] = item['value']
            elif item['type'] == 'list':
                if item['name'] == 'hw_addr':
                    value = OpenFlowMessageStruct.hw_addr_list
                    block_value[item['name']] = value
                elif item['name'] == 'match':
                    value = []
                    match_list = OpenFlowMessageStruct.ofp_match
                    select_num = random.randint(0,len(match_list))
                    selected_match = random.sample(match_list,select_num)
                    for match_field in selected_match:
                        if 'value' in match_field.keys():
                            value.append({match_field['name']:match_field['value']})
                        else:
                            value.append({match_field['name']:self.process_by_type(match_field['type'])})
                    block_value['match'] = value
                else:                        
                    value = []
                    block_value[item['name']] = value
            elif item['type'] != 'list':
                value = self.process_by_type(item['type'])
                block_value[item['name']] = value
        return block_value

    def process_by_msg_type(self,msg_type):
        msg_value = {}
        for pkt in OpenFlowMessageStruct.openflow:
            if pkt[0] == msg_type:
                msg_value = self.build_msg_choice_dict(pkt[1])
        return msg_value

    def build_msg_choice_dict(self,message_body):
        field_vlaue_mapper = {} 
        for field_dict in message_body:
            range = ""
            if 'range' in field_dict.keys():
                range = field_dict['range']
            if 'impl' in field_dict.keys() and field_dict['impl'] == False:
                continue
            elif 'name' in field_dict.keys() and field_dict['name'] == "version":
                continue
            elif 'name' in field_dict.keys() and field_dict['name'] == "type":
                continue
            elif 'name' in field_dict.keys() and field_dict['name'] == "length":
                continue

            # in pyloxi , xid must be required 
            else:
                if 'type' in field_dict.keys() and field_dict['type'] == "list":
                    nest_list = field_dict['fields']
                    chose_list = self.choose_random_list(nest_list)
                    if 'name' in field_dict.keys():
                        return_list = []
                        ran_value = self.build_msg_choice_dict(chose_list)
                        if ran_value != None:
                            return_list.append(ran_value)
                        field_vlaue_mapper[field_dict['name']] = return_list
                    else:
                        return_list = []
                        ran_value = self.process_by_type_range(field_dict['type'],range)
                        # deal with list is null
                        if ran_value != None:
                            return_list.append(ran_value)
                        return return_list
                    
                # non-nested structure
                elif 'type' in field_dict.keys() and field_dict['type'] != "list":
                    # normal condition , finish the mapper until the end of structure
                    if 'name' in field_dict.keys():
                        field_vlaue_mapper[field_dict['name']] = self.process_by_type_range(field_dict['type'],range)
                    # this field is a list but in pyloxi , for example , port hwaddr or bitmap
                    else:
                        return self.process_by_type_range(field_dict['type'],range)
                else:
                    # constructor
                    if 'fields' in field_dict.keys():
                        field_vlaue_mapper[field_dict['name']] = self.build_msg_choice_dict(field_dict['fields'])
                    # fields not in and type not in, seldom to appear
                    else:
                        field_vlaue_mapper[field_dict['name']] = self.process_by_type_range(field_dict['type'],range)
        return field_vlaue_mapper
                
    def choose_random_list(self,old_list):
        new_list = []
        ran_num = random.randint(0,len(old_list))
        for item in sample(old_list,ran_num):
            new_list.append(item)
        return new_list

    def process_by_type(self,field_type):
        ranuint8 = hex(random.randint(0,0xff))
        ranuint16 = hex(random.randint(0,0xffff))
        ranuint24 = hex(random.randint(0,0xffffff))
        ranuint32 = hex(random.randint(0,0xffffffff))
        ranuint48 = []
        for i in range(0,6):
            one_byte = hex(random.randint(0,0xff))
            ranuint48.append(int(hex(random.randint(0,0xff)),16))
        ranuint48 = '{}'.format(ranuint48)
        
        ranuint64 = hex(random.randint(0,0xffffffffffffffff))
        ranuint128_byte = binascii.hexlify(os.urandom(16))
        ranuint128 = ranuint128_byte.decode("utf8")
        ranport = hex(random.randint(0,0xffffffff))
        ranlen = random.randint(0,20)
        ranstring = ''.join(random.sample(string.ascii_letters + string.digits,ranlen))
        if field_type == '':
            return ''
        if field_type == 'uint8':
            return ranuint8
        elif field_type == 'uint16':
            return ranuint16
        elif field_type == 'uint24':
            return ranuint24
        elif field_type == 'uint32':
            return ranuint32
        elif field_type == 'uint48':
            return ranuint48
        elif field_type == 'uint64':
            return ranuint64
        elif field_type == 'uint128':
            return ranuint128
        elif field_type == 'port':
            return ranport
        elif field_type == 'string':
            return ranstring

    def process_by_type_range(self,field_type,range_set):
        if range_set == "":
            ranuint8 = hex(random.randint(0,0xff))
            ranuint16 = hex(random.randint(0,0xffff))
            ranuint24 = hex(random.randint(0,0xffffff))
            ranuint32 = hex(random.randint(0,0xffffffff))
            ranuint48 = []
            for i in range(0,6):
                one_byte = hex(random.randint(0,0xff))
                ranuint48.append(int(hex(random.randint(0,0xff)),16))
            ranuint48 = '{}'.format(ranuint48)
            
            ranuint64 = hex(random.randint(0,0xffffffffffffffff))
            ranuint128_byte = binascii.hexlify(os.urandom(16))
            ranuint128 = ranuint128_byte.decode("utf8")
            ranport = hex(random.randint(0,0xffffffff))
            ranlen = random.randint(0,20)
            # to avoid data is int
            ranstring = ''.join(random.sample(string.ascii_letters ,ranlen))
            if field_type == '':
                return ''
            if field_type == 'uint8':
                return ranuint8
            elif field_type == 'uint16':
                return ranuint16
            elif field_type == 'uint24':
                return ranuint24
            elif field_type == 'uint32':
                return ranuint32
            elif field_type == 'uint48':
                return ranuint48
            elif field_type == 'uint64':
                return ranuint64
            elif field_type == 'uint128':
                return ranuint128
            elif field_type == 'port':
                return ranport
            elif field_type == 'string':
                return ranstring
        else:
            defined_range = list_to_interval(range_set)
            max_vlaue = self.get_max_value(field_type)
            all_range = IntervalSet([Interval(0x0,max_vlaue)])
            undefined_range = all_range - defined_range
            select_value = process_by_interval(defined_range,undefined_range)
            return select_value

    def get_max_value(self,field_type):
        if field_type == 'uint8':
            return 0xff
        elif field_type == 'uint16':
            return 0xffff
        elif field_type == 'uint24':
            return 0xffffff
        elif field_type == 'uint32':
            return 0xffffffff
        elif field_type == 'uint48':
            return 0xffffffffffff
        elif field_type == 'uint64':
            return 0xffffffffffffffff
        elif field_type == 'uint128':
            return 0xffffffffffffffffffffffffffffffff
        elif field_type == 'port':
            return 0xffffffff


    def load_from_file(self, f):
        strategy = None
        for line in f:
            if line.find("#") >= 0:
                continue
            if line == '\n':
                continue
            strategy = line
            strategy = strategy.replace("\n","")
            self.strategy_queue.enqueue(strategy)
            self.strategy_list.append(self.strategy_process(strategy))

    def write_to_file(self,f):
        for strategy in self.strategy_list:
            if type(strategy) is not str:
                f.write(strategy.to_file())
            else:
                f.write(strategy+"\n")

    def build_action_by_type(self,msg_type):
        action_str_list = []

        #Transmission Strategies
        for pkt in OpenFlowMessageStruct.openflow_13_occur:
            if msg_type == pkt[0]:
                message_body = pkt[1]
                for action in OpenFlowAction.message_transmission_actions:
                    for par in action[2]:
                        action_str = action[1].format(par)
                        action_str_list.append(action_str)

        # Modification Strategies
        fields = self.build_field_list(message_body)
        for field in fields:
            for action in OpenFlowAction.message_modify_actions:
                field_type = field['type']
                select_value = self.process_by_type_range(field_type,"")
                action_str = action[1].format(field['field'],select_value)
                action_str_list.append(action_str)
    
        # block Strategies
        for pkt in OpenFlowMessageStruct.openflow_13_block:
            if msg_type == pkt[0]:
                message_body = pkt[1]
        
                fields = self.build_field_list(message_body)
                block_list = self.build_block_list(fields)      
                if len(block_list) != 0:
                    for block in block_list:
                        for action in OpenFlowAction.message_block_actions:
                            if action[0] == "DEL":

                                action_str = action[1].format(block)
                                action_str_list.append(action_str)
                            else:
                                block_value = self.construct_block(msg_type)
                                action_str = action[1].format(block,block_value)
                                action_str_list.append(action_str)

        # BUILD Strategies
        for pkt in OpenFlowMessageStruct.openflow_13_occur:
            msg_type = pkt[0]
            message_body = pkt[1]
            
            for action in OpenFlowAction.message_build_actions:
                for build_pkt in OpenFlowMessageStruct.openflow_13:
                    build_msg_type = build_pkt[0]
                    build_value = self.process_by_msg_type(build_msg_type)
                    
                    action_str = action[1].format(build_msg_type,build_value)
                    action_str_list.append(action_str)

        return action_str_list

if __name__ == "__main__":
    strategy_file = open( file = "strategy.txt",mode = 'w', encoding = "utf-8")
    strategy_Gen = StrategyGenerator()
    strategy_Gen.build_strategies()
    strategy_Gen.write_to_file(strategy_file)
    
    