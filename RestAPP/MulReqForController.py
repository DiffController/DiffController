
import requests
import time

headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json'}

# controller ip & controller rest port
ryu_controller_ip = '172.17.0.2'
ryu_rest_port = '8080'
fl_controller_ip = '172.17.0.3'
fl_rest_port = '8080'

# controller switch url
ryu_switch_url = "http://"+ryu_controller_ip+":8080/collectswithes/switcheslist/json"
ryu_switch_list = []
fl_switch_url = "http://"+ fl_controller_ip +":8080/wm/statics/FloodlightSwitches/json"
fl_switch_list = []

# Ryu multiple request 
ryu_multiple_desc = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/desc/1"
ryu_multiple_flow = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/flow/1"
ryu_multiple_port_stats = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/port/1"
ryu_multiple_group = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/group/1"
ryu_multiple_group_desc = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/groupdesc/1"
ryu_multiple_group_feature = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/groupfeatures/1"
ryu_multiple_meter = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/meter/1"
ryu_multiple_meter_config = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/meterconfig/1"
ryu_multiple_meter_feature = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/meterfeatures/1"
ryu_multiple_port_desc = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/portdesc/1"
ryu_role = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/stats/role/1"
ryu_get_config_request = "http://"+ryu_controller_ip+":"+ryu_rest_port+"/v1.0/conf/switches"


fl_multiple_flow = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/flow/json"
fl_multiple_aggregate = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/aggregate/json"
fl_multiple_table = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/table/json"
fl_multiple_port_stats = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/port/json"
fl_multiple_queue = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/queue/json"
fl_multiple_group= "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/group/json"
fl_multiple_group_desc = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/group-desc/json"
fl_multiple_group_feature = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/group-features/json"
fl_multiple_meter = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/meter/json"
fl_multiple_meter_config = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/meter-config/json"
fl_multiple_meter_feature = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/switch/00:00:00:00:00:00:00:01/meter-features/json"
fl_role = "http://"+fl_controller_ip+":"+fl_rest_port+"/wm/core/role/json"

def send_multiple_request():
    
    while True:
        # ryu multiple request
        ryu_switch_list = []
        res = requests.get(url=ryu_switch_url ,headers=headers)
        res = res.json()
        for switch in res:
           ryu_switch_list.append(switch)
        print(ryu_switch_list)
        if ryu_switch_list != []:
            if '1' in ryu_switch_list:
                res = requests.get(url=ryu_multiple_desc,headers=headers)
                print(ryu_multiple_desc)
                res = requests.get(url=ryu_multiple_flow,headers=headers)
                res = requests.get(url=ryu_multiple_port_stats,headers=headers)
                res = requests.get(url=ryu_multiple_group,headers=headers)
                res = requests.get(url=ryu_multiple_group_desc,headers=headers)
                res = requests.get(url=ryu_multiple_group_feature,headers=headers)
                res = requests.get(url=ryu_multiple_meter,headers=headers)
                res = requests.get(url=ryu_multiple_meter_config,headers=headers)
                res = requests.get(url=ryu_multiple_meter_feature,headers=headers)
                res = requests.get(url=ryu_multiple_port_desc,headers=headers)
                res = requests.get(url=ryu_role,headers=headers)
                res = requests.get(url=ryu_get_config_request,headers=headers)

        # flodlight multiple request
        fl_switch_list = []
        res = requests.get(url=fl_switch_url,headers=headers)
        res = res.json()

        for switch in res:
            fl_switch_list.append(switch)
        if fl_switch_list != []:
            if '00:00:00:00:00:00:00:01' in fl_switch_list:
                res = requests.get(url=ryu_multiple_flow,headers=headers)
                res = requests.get(url=fl_multiple_aggregate,headers=headers)
                res = requests.get(url=fl_multiple_table,headers=headers)
                res = requests.get(url=fl_multiple_port_stats,headers=headers)
                res = requests.get(url=fl_multiple_queue ,headers=headers)
                res = requests.get(url=fl_multiple_group,headers=headers)
                res = requests.get(url=fl_multiple_group_desc,headers=headers)
                res = requests.get(url=fl_multiple_group_feature,headers=headers)
                res = requests.get(url=fl_multiple_meter,headers=headers)
                res = requests.get(url=fl_multiple_meter_config,headers=headers)
                res = requests.get(url=fl_multiple_meter_feature,headers=headers)
                res = requests.get(url=fl_role,headers=headers)
        time.sleep(2)

if __name__ == "__main__":
    send_multiple_request()