import string
import sys
import os

pyloxi_project = 'pyloxi3'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "/"+ pyloxi_project)
from loxi import of13 as ofp
from loxi.of13.oxm import *
from loxi.of13.common import *
from loxi.of13.message import *
from loxi.of13.action import *
from loxi.of13.instruction import *
from loxi.of13.meter_band import *
from scapy.all import *
from scapy.contrib import lldp,openflow3
from ast import literal_eval

def build_msg(build_type,value):
    built_msg = b''
    eval_mapper = {}
    for parameter_name in value.keys():
        parameter_value = value[parameter_name]
        para_name,para_value = parameter_recursion(parameter_name,parameter_value)
        eval_mapper[para_name] = para_value
    build_of_msg = constuctor_merge(eval_mapper,build_type)
    built_msg = build_of_msg.pack()
    return built_msg

def constuctor_merge(mapper,build_type):
    val_mapper = {}
    if build_type in mapper.keys():
        return mapper[build_type]
    for k,v in mapper.items():
        if type(v) == str:
            if is_number(v) == True:
                val_mapper[k+"_val"] = int(v,16)
            elif is_list(v) == True:
                val_mapper[k+"_val"] = hw_str_to_hw_list(v)
            else:
                val_mapper[k+"_val"] = v
        elif type(v) == list:
            return_name,return_value = parameter_recursion(k,v)
            val_mapper[return_name+"_val"] = return_value
        elif type(v) == dict:
            return_name,return_value = parameter_recursion(k,v)
            val_mapper[return_name+"_val"] = return_value
        # seems to deal with str problem?
        elif type(v) == bytes:
            if k != "data":
                val_mapper[k+"_val"] = (bytes.decode(v))
            else:
                 val_mapper[k+"_val"] = v
        else:
            val_mapper[k+"_val"] = v
    par_list = [str(k)+ "=" +str(k)+"_val" for k,v in mapper.items()]
    par_str = ",".join(par_list)
    build_msg_str = ""+build_type+"("+par_str+")"
    return eval(build_msg_str,globals(),val_mapper)


def parameter_recursion(parameter_name,parameter_value):
    if type(parameter_value) == str:
        if is_number(parameter_value):
            return parameter_name,int(parameter_value,16)
        elif is_list(parameter_value):
            return parameter_name,hw_str_to_hw_list(parameter_value)
        elif is_bytes(parameter_value):
            return parameter_name,string_to_bytes(parameter_value)
        else:
            return parameter_name,parameter_value
    else:
        if type(parameter_value) == list:
            new_list = []
            for nest_parameter in parameter_value:
                construct_result = None
                if type(nest_parameter) == dict:
                    # [{},{},{}]
                    if nest_parameter == {}:
                        return parameter_name,[]
                    str_list = []
                    for constructor_name in nest_parameter.keys():
                        constructor_parameter = nest_parameter[constructor_name]
                        new_mapper = {}
                        if type(constructor_parameter) == dict:
                            for con_par in constructor_parameter.keys():
                                con_value = constructor_parameter[con_par]
                                return_par,return_value = parameter_recursion(con_par,con_value)
                                if type(return_value) == str: 
                                    str_list.append(constuctor_merge(constructor_parameter,constructor_name))
                                    break
                                elif type(return_value) == int: 
                                    str_list.append(constuctor_merge(constructor_parameter,constructor_name))
                                    break
                                elif type(return_value) == list:
                                    return_mapper = {}
                                    return_mapper[return_par] = return_value
                                    str_list.append(constuctor_merge(return_mapper,constructor_name))
                                else:
                                    new_mapper[return_par] = return_value
                        elif type(constructor_parameter) == str:
                            if constructor_parameter == '':
                                append_value = eval(constructor_name+"()")
                                str_list.append(append_value)
                            elif is_number(constructor_parameter):
                                append_value = eval(constructor_name)(int(constructor_parameter,16))
                                str_list.append(append_value)
                            elif is_list(constructor_parameter):
                                hw_addr = hw_str_to_hw_list(constructor_parameter)
                                append_value = eval(constructor_name)(hw_addr)
                                str_list.append(append_value)
                            elif is_bytes(constructor_parameter):
                                bytes = string_to_bytes(constructor_parameter)
                                append_value = eval(constructor_name)(bytes)
                                str_list.append(append_value)
                            else:
                                append_value = eval(constructor_name)(constructor_parameter)
                                str_list.append(append_value)
                        else:
                            parameter_val = eval(constructor_name)(constructor_parameter)
                            return parameter_name,parameter_val
                    if str_list != []:
                        return parameter_name,str_list
                    parameter_str = ""
                    new_list.append(constuctor_merge(new_mapper,constructor_name))
                else:
                    if type(nest_parameter) == str:
                        if is_number(nest_parameter):
                            new_list.append(int(nest_parameter,16))
                            continue
                        elif is_list(nest_parameter):
                            new_list.append(hw_str_to_hw_list(nest_parameter))
                            continue
                        elif is_bytes(nest_parameter):
                            new_list.append(string_to_bytes(nest_parameter))
                            continue
                    else:
                        new_list = parameter_value
                    return parameter_name,new_list
            return parameter_name,new_list
        elif type(parameter_value) == dict:
            new_mapper = {}
            for key in parameter_value.keys():
                value = parameter_value[key]
                if type(value) == list:
                    return_par,return_value = parameter_recursion(key,value)
                    new_mapper[return_par] = return_value
                elif type(value) == dict:
                    return_par,return_value = parameter_recursion(key,value)
                    return parameter_name,return_value
                elif type(value) == str:
                    new_mapper[key] = value 
            constructor_result = constuctor_merge(new_mapper,parameter_name)
            return parameter_name,constructor_result          
    return  

def match_process(match_list):
    matches = []
    for key,value in match_list.items():
        value = int(value,16)
        matches.append(eval(key)(value))
    match = ofp.common.match(oxm_list=matches)
    return match

def is_number(s):
    try:
        if len(s) != 32 and s.startswith("0x"):
            int(s,16)
            return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    
    return False

def is_list(s):
    try:
        s = s.strip()
        if s.startswith("[") and s.endswith("]"):
            literal_eval(s)
            return True
    except ValueError:
        pass
    return False

def hw_str_to_hw_list(hw_str):
    hw_addr = []
    hw_str = hw_str.replace("'","")
    hw_str = hw_str.replace("[","")
    hw_str = hw_str.replace("]","")
    hw_addr_10 = hw_str.split(",")
    for item in hw_addr_10:
        item = int(item,10)
        hw_addr.append(item)
    return hw_addr

def is_bytes(s):
    try:
        if not s.startswith("0x"):
            b = s.encode(encoding="utf-8")
            return True
    except ValueError:
        pass
    return False

def string_to_bytes(s):
    b = s.encode(encoding="utf-8")
    return b

