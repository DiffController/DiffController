from ast import literal_eval
from dis import Instruction
import sys
import os


pyloxi_project = 'pyloxi3'
sys.path.append(os.getcwd() +"/"+ pyloxi_project)
from loxi import of13 as ofp
from loxi.of13.oxm import *
from loxi.of13.common import *

def match_struct_process(of_msg_data,field,value):
    if "entries" in field:
        if len(of_msg_data.__dict__['entries']) == 0 :
            oxm_list = []
        else:
            oxm_list = of_msg_data.__dict__['entries'][0].__dict__['match'].__dict__['oxm_list']
    else:
        oxm_list = of_msg_data.__dict__['match'].__dict__['oxm_list']
    oxm_type = field.split('.')[-1]
    for oxm in oxm_list:
        if type(oxm) == eval(oxm_type):
            oxm.__dict__['value'] = int(value,16)
    return of_msg_data

def entries_struct_process(of_msg_data,field,value):
    value = value_conevrt(value)
    entries_list = of_msg_data.__dict__['entries']
    modify_field = field.split('.')[-1]
    for entry in  entries_list:
        if modify_field in entry.__dict__.keys():
            entry.__dict__[modify_field] = value
            break
    return of_msg_data

def value_conevrt(value):
    if type(value) == str:
        if is_number(value):
            value = int(value,16)
        else:
            pass
    elif type(value) == list:
        value = value
    else:
        pass
    return value


def match_struct_del_process(of_msg_data,block):
    oxm_list = of_msg_data.__dict__['match'].__dict__['oxm_list']
    oxm_type = block.split('.')[-1]
    # remove the first oxm field
    for oxm in oxm_list:
        oxm_list.remove(oxm)
        break
    return of_msg_data

def match_struct_add_process(of_msg_data,value):
    oxm_list = of_msg_data.__dict__['match'].__dict__['oxm_list']
    for item in value.items():
        if type(item[1]) == str and is_number(item[1]):
            oxm_list.append(eval(item[0])(int(item[1],16)))
        elif type(item[1]) == list:
            oxm_list.append(eval(item[0])(item[1]))
    return of_msg_data

def flow_struct_del_process(of_msg_data,block):
    return of_msg_data

def flow_struct_add_process(of_msg_data,value):
    table_id = value["table_id"]
    duration_sec = value["duration_sec"]
    duration_nsec = value["duration_nsec"]
    idle_timeout = value["idle_timeout"]
    hard_timeout = value["hard_timeout"]
    flags = int(value["flags"],16)
    cookie = value["cookie"]
    packet_count = value["packet_count"]
    byte_count = value["byte_count"]
    match = match_process(value["match"])
    instructions = value["instructions"]
    flow_stats_entry = ofp.common.flow_stats_entry(table_id=table_id,duration_sec=duration_sec,duration_nsec=duration_nsec,
                    idle_timeout=idle_timeout,hard_timeout=hard_timeout,flags=flags,cookie=cookie,packet_count=packet_count,
                    byte_count=byte_count,match=match,instructions=instructions)
    of_msg_data.__dict__["entries"].append(flow_stats_entry)
    return of_msg_data

def entries_struct_add_process(of_msg_data,value,block):
    entries_type = block.split(".")[1]
    val_mapper = {}
    for k,v in value.items():
        if type(v) == str:
            if is_number(v) == True:
                val_mapper[k+"_val"] = int(v,16)
            else:
                val_mapper[k+"_val"] = v
        elif type(v) == list:
            val_mapper[k+"_val"] = v
        else:
            val_mapper[k+"_val"] = v
    par_list = [str(k)+ "=" +str(k)+"_val" for k,v in value.items()]
    par_str = ",".join(par_list)
    build_entries_str = ""+entries_type+"("+par_str+")"
    entry = eval(build_entries_str,globals(),val_mapper)
    of_msg_data.__dict__["entries"].append(entry)
    return of_msg_data

def entries_struct_del_process(of_msg_data,block):
    entry_list = of_msg_data.__dict__['entries']
    entry_type = block.split('.')[-1]
    """ len(entry_list) = 0 , default * in match field"""
    # remove the first oxm field
    for entry in entry_list:
        entry_list.remove(entry)
        break
    return of_msg_data

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
        b = s.encode(encoding="utf-8")
        return True
    except ValueError:
        pass
    return False

def string_to_bytes(s):
    b = s.encode(encoding="utf-8")
    return b