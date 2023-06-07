import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/DecoderGuider")
import copy
import math
import random
import re
import time
from StrategyGenerator import Strategy
from StrategyGenerator import StrategyGenerator
from ryu_parser import ryu_decoder_parsered_result
from floodlight_parser import fl_decoder_parsered_result
from onos_parser import onos_decoder_parsered_result
from odl_parser import odl_decoder_parsered_result
import jpype
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

def action_mutation(population):

    mutation_probality   = 0.5

    offspring = copy.deepcopy(population)

    del_index = []
    for i in range(len(offspring)):
        mutation_finished = False
        while not mutation_finished:
            strategy_mutated = copy.deepcopy(offspring[i])
            random_float = random.random()
            if random_float < mutation_probality:
                mutate_individual_action(strategy_mutated)
            else:
                mutate_action_list(strategy_mutated)
            mutation_finished = True
        offspring[i] = strategy_mutated
    return offspring

def crossover(population):
    offspring = copy.deepcopy(population)
    for i in range(1,len(offspring),2):
        ind = offspring[i-1]
        mate(ind,offspring[i])

    return offspring

def crossover_and_action_mutation(population):
    crossover_probality   = 0.1
    random_float = random.random()
    if random_float < crossover_probality:
        return crossover(population)
    else:
        return action_mutation(population)


def mate(ind1,ind2):
    action_str1 = ind1.action
    action_str2 = ind2.action
    action_list1 = action_str1.split("|")
    action_list2 = action_str2.split("|")
    if ind1.pkt_type == ind2.pkt_type:
        action_list1,action_list2 = no_limit_swap(action_list1,action_list2)
        
        action_list1 = action_list_sort(action_list1)
        action_list2 = action_list_sort(action_list2)
        
        new_action_str1 = "|".join(action_list1)
        ind1.action = new_action_str1
        new_action_str2 = "|".join(action_list2)
        ind2.action = new_action_str2
    else:
        action_list1,action_list2 = conditional_swap(action_list1,action_list2)
        
        action_list1 = action_list_sort(action_list1)
        action_list2 = action_list_sort(action_list2)

        new_action_str1 = "|".join(action_list1)
        ind1.action = new_action_str1
        new_action_str2 = "|".join(action_list2)
        ind2.action = new_action_str2
    
def no_limit_swap(action_list1,action_list2): 

    list1_index = random.randint(0,len(action_list1)-1)
    list2_index = random.randint(0,len(action_list2)-1)
    new_action_list1 = action_list1[0:list1_index]+action_list2[list2_index:]
    new_action_list2 = action_list2[0:list2_index]+action_list1[list1_index:]
    return new_action_list1,new_action_list2

def conditional_swap(action_list1,action_list2):
    list1_index = random.randint(0,len(action_list1)-1)
    list2_index = random.randint(0,len(action_list2)-1)

    list1_swap = []
    list2_swap = []
    list1_no_swap = []
    list2_no_swap = []

    for item in action_list1[list1_index:]:
        action_type = item.split(",")[0]
        if action_type == "MOD" or action_type == "ADD"  or action_type == "DEL" :
            list1_no_swap.append(item)
        else:
            list1_swap.append(item)
    for item in action_list2[list2_index:]:
        action_type = item.split(",")[0]
        if action_type == "MOD" or action_type == "ADD"  or action_type == "DEL" :
            list2_no_swap.append(item)
        else:
            list2_swap.append(item)
    new_action_list1 = action_list1[0:list1_index]+list1_no_swap+list2_swap
    new_action_list2 = action_list2[0:list2_index]+list2_no_swap+list1_swap

    return new_action_list1,new_action_list2

def mutate_individual_action(strategy_mutated):
    # individual mutation
    strategy_mutated.mutate()
    # check strategy
    now_action_list = strategy_mutated.action.split("|")
    new_action_list = action_list_sort(now_action_list)
    strategy_mutated.action = "|".join(new_action_list)
    return strategy_mutated

def mutate_action_list(strategy_mutated):
    # action list mutation
    strategy_mutated.mutate_action_list()
    # check strategy
    now_action_list = strategy_mutated.action.split("|")
    new_action_list = action_list_sort(now_action_list)
    strategy_mutated.action = "|".join(new_action_list)
    return strategy_mutated

def action_list_sort(action_list):
    drop_action_list = []
    dup_action_list = []
    delay_action_list = []
    build_action_list = []
    add_action_list = []
    del_action_list = []
    mod_action_list = []
    for item in action_list:
        action_type = item.split(",")[0]
        if action_type == "DROP":
            drop_action_list.append(item)
        elif action_type == "DUP":
            dup_action_list.append(item)
        elif action_type == "DELAY":
            delay_action_list.append(item)
        elif action_type == "BUILD":
            build_action_list.append(item)
        elif action_type == "ADD":
            add_action_list.append(item)
        elif action_type == "DEL":
            del_action_list.append(item)
        elif action_type == "MOD":
            mod_action_list.append(item)
    
    

    # rule 1 : DROP invalidates operations other than BUILD
    if drop_action_list != []:
        dup_action_list = []
        delay_action_list = []
        add_action_list = []
        del_action_list = []
        mod_action_list = []
    
    # rule2 : multiple DUP,DELAY,DROP only the first one reserved
    if len(dup_action_list) > 1 :
        new_dup_action_list = []
        new_dup_action_list.append(dup_action_list[0])
        dup_action_list = copy.deepcopy(new_dup_action_list)
    if len(delay_action_list) > 1 :
        new_delay_action_list = []
        new_delay_action_list.append(delay_action_list[0])
        delay_action_list = copy.deepcopy(new_delay_action_list)
    if len(drop_action_list) >1 :
        new_drop_action_list = []
        new_drop_action_list.append(drop_action_list[0])
        drop_action_list = copy.deepcopy(new_drop_action_list)

    # rule3 : Mod the same field multiple times, keeping only the last one
    del_index_list = []
    for i in range(0,len(mod_action_list),1):
        for j in range (i+1,len(mod_action_list),1):
            field1 = re.findall('field=\(.*?\)',mod_action_list[i])[0]
            field1 = field1.split("=")[1]
            field1 = field1.replace('(', '')
            field1 = field1.replace(')', '')

            field2 = re.findall('field=\(.*?\)',mod_action_list[j])[0]
            field2 = field2.split("=")[1]
            field2 = field2.replace('(', '')
            field2 = field2.replace(')', '')
            if field1 == field2:
                del_index_list.append(i)
                break
    # dynamic delete the corresponding index , should not use del
    counter = 0 
    for index in del_index_list:
        mod_action_list.pop(index-counter)
        counter += 1

    # rule 4 : MOD type must be the second last in the mod_action_list( length will not be MOD )
    version_index = len(mod_action_list)-1
    if version_index <= 0:
        pass
    else:
        for index in range(0,len(mod_action_list),1):
            field = re.findall('field=\(.*?\)',mod_action_list[index])[0]
            field = field.split("=")[1]
            field = field.replace('(', '')
            field = field.replace(')', '')
            if field == "type":
                version_index = index
                break
        if version_index != len(mod_action_list)-1:
            mod_action_list[version_index],mod_action_list[len(mod_action_list)-1] = mod_action_list[len(mod_action_list)-1],mod_action_list[version_index]

    # rule 5 : MOD version must be the last in the mod_action_list( length will not be MOD )
    version_index = len(mod_action_list)-1
    if version_index <= 0:
        pass
    else:
        for index in range(0,len(mod_action_list),1):
            field = re.findall('field=\(.*?\)',mod_action_list[index])[0]
            field = field.split("=")[1]
            field = field.replace('(', '')
            field = field.replace(')', '')
            if field == "version":
                version_index = index
                break
        if version_index != len(mod_action_list)-1:
            mod_action_list[version_index],mod_action_list[len(mod_action_list)-1] = mod_action_list[len(mod_action_list)-1],mod_action_list[version_index]

    # rule 6 : action list execution order
    new_action_list = add_action_list+del_action_list+mod_action_list+drop_action_list+build_action_list+delay_action_list+dup_action_list
    return new_action_list 


def population_str_to_strategy(population_str_list):
    population = []
    for strategy_str in population_str_list:
        strategy = strategy_process(strategy_str)
        population.append(strategy)
    return population

def strategy_process(strategy_str):
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

def comment_reomved(init_population):
    init_population = [individual for individual in init_population if type(individual) is not str]
    return init_population


def genetic_solve():
    
    hall = {}

    strategy_Gen = StrategyGenerator()
    
    strategy_Gen.build_strategies()
    
    # initialize population generation
    population = strategy_Gen.strategy_list[0:20]
    population = comment_reomved(population)
    before_hash = []
    before_hash = [ hash(ind.to_str()) for ind in population]
    offsprings = []
    try:
        offspring = []
        gen = 0
        while(True):
            if (len(population)==0): break
            gen += 1
            strategy_index = 0
            priority_population = []
            current_seed_source = 'population'
            fuzz_time = 0
            
            while strategy_index < len(population):
                pickpb = random.random()
                if len(priority_population)!=0 and pickpb < 0.66:
                    current_seed_source = 'priority'
                    population.append(copy.deepcopy(priority_population[0]))
                    seed_ind = population[-1]
                    seed_ind.was_fuzzed = True
                    del priority_population[0]
                
                else:
                    current_seed_source = 'population'
                    seed_ind = population[strategy_index]
                    strategy_index += 1
                
                # same individual has been mutation
                if seed_ind.was_fuzzed == True and current_seed_source == 'population':
                    continue
                fuzz_time += 1
                task_sequence = [copy.deepcopy(seed_ind) for x in range(math.ceil(seed_ind.perf_score/100))]
                offspring  = crossover_and_action_mutation(task_sequence)
                for seed in offspring:
                    if current_seed_source == 'priority':
                        seed.source_dict["priority"] += 1
                    else:
                        seed.source_dict["population"] += 1
                    seed.hash = hash(seed.to_str())
                
                # judge whether offspring should be added
                offspring = selection_next_generation(offspring,seed_ind,gen,before_hash)

                if len(offspring) != 0:
                    seed_ind.has_child = True
                
                add2priority = 0
                add2pop = 0
                for new_ind in offspring:
                    if new_ind.saved_reason == '++':
                        priority_population.append(new_ind)
                        add2priority += 1
                    else:
                        population.append(new_ind)
                        add2pop += 1
            population = list(filter(lambda x: x.no_good_count <= 4 or (x.no_good_count <= 8 and x.has_child == False),population))  
    except KeyboardInterrupt:
        pass

    finally:
        pass

    return hall

def genetic_solve_one_generation(population,gen,before_hash):
    population = comment_reomved(population)
    strategy_index = 0
    priority_population = []
    original_len = len(population)
    current_seed_source = 'population'
    offsprings = []
    while strategy_index < len(population):
        pickpb = random.random()
        if len(priority_population)!=0 and pickpb < 0.66:
            current_seed_source = 'priority'
            population.append(copy.deepcopy(priority_population[0]))
            seed_ind = population[-1]
            seed_ind.was_fuzzed = True
            del priority_population[0]
        
        else:
            current_seed_source = 'population'
            seed_ind = population[strategy_index]
            strategy_index += 1
        
        # same individual has been mutation
        if seed_ind.was_fuzzed == True and current_seed_source == 'population':
            continue
        
        task_sequence = [copy.deepcopy(seed_ind) for x in range(math.ceil(seed_ind.perf_score/100))]

        offspring  = crossover_and_action_mutation(task_sequence)
        
        for seed in offspring:
            if current_seed_source == 'priority':
                seed.source_dict["priority"] += 1
            else:
                seed.source_dict["population"] += 1
            seed.hash = hash(seed.to_file())
        
        # judge whether offspring should be added
        offspring = selection_next_generation(offspring,seed_ind,gen,before_hash)
        if len(offspring) != 0:
            seed_ind.has_child = True

        offsprings += offspring
    
    add2priority = 0
    add2pop = 0
    for new_ind in offsprings:
        if new_ind.saved_reason == '++':
            priority_population.append(new_ind)
            population.append(new_ind)
            add2priority += 1
        else:
            population.append(new_ind)
            add2pop += 1
    next_population = list(filter(lambda x: x.no_good_count <= 7 or (x.no_good_count <= 14 and x.has_child == False),population))
    
    if len(next_population) > original_len:
        next_population.sort(key=lambda x:x.perf_score)
        next_population = next_population[0:original_len]
    return next_population,offsprings,priority_population

def genetic_solve_one_generation_without_decoder(population,gen,before_hash):
    population = comment_reomved(population)

    strategy_index = 0
    priority_population = []
    current_seed_source = 'population'
    offsprings = []
    while strategy_index < len(population):
        pickpb = random.random()
        if len(priority_population)!=0 and pickpb < 0.66:
            current_seed_source = 'priority'
            population.append(copy.deepcopy(priority_population[0]))
            seed_ind = population[-1]
            seed_ind.was_fuzzed = True
            del priority_population[0]
        else:
            current_seed_source = 'population'
            seed_ind = population[strategy_index]
            strategy_index += 1
        
        # same individual has been mutation
        if seed_ind.was_fuzzed == True and current_seed_source == 'population':
            continue
        
        task_sequence = [copy.deepcopy(seed_ind) for x in range(math.ceil(seed_ind.perf_score/100))]

        offspring  = crossover_and_action_mutation(task_sequence)
        
        for seed in offspring:
            if current_seed_source == 'priority':
                seed.source_dict["priority"] += 1
            else:
                seed.source_dict["population"] += 1
            seed.hash = hash(seed.to_file())
        
        # judge whether offspring should be added
        offspring = selection_next_generation_without_decoder(offspring,seed_ind,gen,before_hash)
        if len(offspring) != 0:
            seed_ind.has_child = True

        offsprings += offspring
    
    add2priority = 0
    add2pop = 0
    for new_ind in offsprings:
        if new_ind.saved_reason == '++':
            priority_population.append(new_ind)
            population.append(new_ind)
            add2priority += 1
        else:
            population.append(new_ind)
            add2pop += 1
    next_population = list(filter(lambda x: x.no_good_count <= 4 or (x.no_good_count <= 8 and x.has_child == False),population))
    return next_population,offsprings,priority_population


def selection_next_generation(individuals,seed_ind,gen,before_hash):
    """
    Select individual from the last generation based on OpenFlow Decoder 
    Core thought : if one packet sequence can be parsed successfully by one Decoder while failing in other Decoder,
    good sign for difference in multiple controller
    """
    chosen = []
    father_strategy = seed_ind
    handicap = 0 

    for i in range(len(individuals)):
        child_strategy = individuals[i]
        child_strategy.first_added_time = gen
        if child_strategy.hash not in before_hash:
            before_hash.append(child_strategy.hash)
            # whether to limit the length of action list??
            pcap_path = "../DecoderGuider/of13_sequence.pcap"
            ryu_result = ryu_decoder_parsered_result(pcap_path,child_strategy.to_file())
            fl_jar_path = '../DecoderGuider/openflowjtest-1.0-SNAPSHOT.jar'
            onos_jar_path = '../DecoderGuider/onosopenflowtest-1.0-SNAPSHOT.jar'
            odl_jar_path = '../DecoderGuider/odlopenflowtest-1.0-SNAPSHOT.jar'
            jvmPath = jpype.getDefaultJVMPath()
            try:
                jpype.startJVM(jvmPath, "-ea",classpath=[fl_jar_path,onos_jar_path,odl_jar_path])
            except :
                pass
            floodlight_result = fl_decoder_parsered_result(pcap_path,child_strategy.to_file())
            onos_result = onos_decoder_parsered_result(pcap_path,child_strategy.to_file())
            odl_result = odl_decoder_parsered_result(pcap_path,child_strategy.to_file())

            # all succeed , bad
            if ryu_result[0] == "succeed" and floodlight_result[0] == "succeed" and onos_result[0]== "succeed" and odl_result[0] == "succeed":
                father_strategy.no_good_count += 1
                child_strategy.mutate_weight = 0
                handicap += 1

            # one decoder failed, but others succeed ,very very interesting
            elif ryu_result[0] == "succeed" or floodlight_result[0] == "succeed" or onos_result[0]== "succeed" or odl_result[0] == "succeed":
                child_strategy.mutate_weight += 2
                child_strategy.saved_reason = "++"
                if father_strategy.no_good_count >= 2 :
                    father_strategy.no_good_count -= 2
                else:
                    father_strategy.no_good_count = 0
                child_strategy.no_good_count = 0
            
            # all decoder failed ,little interesting 
            else:
                file_name = "interesting_strategy.txt"
                interest_str = "father_strategy:{}strategy:{}ryu:{} floodlight:{},onos:{},odl:{}\n\n".format(father_strategy.to_file(),child_strategy.to_file(),ryu_result,floodlight_result,onos_result,odl_result)
                interest_file = open( file = file_name,mode = 'a+', encoding = "utf-8")
                interest_file.write(interest_str)
                if child_strategy.mutate_weight >= 1:
                    child_strategy.mutate_weight -= 1
                child_strategy.saved_reason = "+"
                child_strategy.no_good_count += 1
            
            if child_strategy.saved_reason == "+" or child_strategy.saved_reason == "++":
                child_strategy.handicap = handicap
                chosen.append(copy.deepcopy(child_strategy))
                handicap -= 1
        else:
            pass
        
    
    for i in range(len(chosen)):
        chosen[i].perf_score = calculate_score(chosen[i])
  
    return chosen

def selection_next_generation_without_decoder(individuals,seed_ind,gen,before_hash):
    """
    Select individual from the last generation based on OpenFlow Decoder 
    Core thought : if one packet sequence can be parsed successfully by one Decoder while failing in other Decoder,
    good sign for difference in multiple controller
    """
    chosen = []
    father_strategy = seed_ind
    handicap = 0 

    for i in range(len(individuals)):

        child_strategy = individuals[i]
        child_strategy.first_added_time = gen

        if child_strategy.hash not in before_hash:
            child_strategy.mutate_weight += 2
            child_strategy.saved_reason = "++"
            if father_strategy.no_good_count >= 2 :
                father_strategy.no_good_count -= 2
            else:
                father_strategy.no_good_count = 0
            child_strategy.no_good_count = 0
            child_strategy.handicap = handicap
            chosen.append(copy.deepcopy(child_strategy))
            handicap -= 1
    
    for i in range(len(chosen)):
        chosen[i].perf_score = calculate_score(chosen[i])
  
    return chosen

def calculate_score(individual):
    """
    Like afl, we calculate mutate weight based on individual's depth handicap and init mutate_weight

    Args:
        individual (Strategy): Single Strategy
    """
    if individual.mutate_weight <=4: perf_score = 1000     # 8 100 |2
    #elif individual.mutate_weight <=4: perf_score = 200
    elif individual.mutate_weight <=8: perf_score = 1500   # 16 200 | 8 400
    elif individual.mutate_weight <=12: perf_score = 2000  # 24 400 | 12 800
    else :                              perf_score = 3000   # 800 | 1200

    # Adjust score based on handicap . Handicap is proportional to how late in the game we learned about this path. Latecommers are allowed to run for a bit longer 
    # until they catch up 
    if (individual.handicap >= 4):
        perf_score *=2     # 4
    elif (individual.handicap):
        perf_score *=1     # 2

    # Adjust score based on input depth , under the assumption that fuzzing deeper test cases is more likely to reveal security problem
    if   individual.get_action_list_len() < 2 : pass
    elif individual.get_action_list_len() >=2 and individual.depth <=3 : perf_score*=3 
    elif individual.depth >=4 and individual.depth <=5 : perf_score*=4 
    else :                                                 perf_score*=5 

    # reduce + mutate_time
    if individual.saved_reason == '+':
        perf_score = perf_score/2
    # Make sure that we don't go over limit
    if (perf_score > 40 * 100) : perf_score = 4000

    return perf_score/2

if __name__ == "__main__":
    strategy1 = "[0,of_aggregate_stats_reply,*,DROP,f=True]"
    strategy2 = "[0,of_aggregate_stats_reply,*,DELAY,s=1]"
    strategy3 = "[0,of_table_stats_reply,*,DUP,n=2]"
    strategy4 = "[0,of_aggregate_stats_reply,*,MOD,field=(version)&val=(0x66)]"
    strategy5 = "[0,of_packet_in,*,ADD,field=(match.match)&val=({'in_port': '0xa28b8e02', 'in_phy_port': '0xf715434d', 'eth_src': [142, 140, 73, 151, 166, 54], 'eth_dst': [86, 117, 108, 238, 140, 246], 'eth_type': '0x3b96', 'ip_proto': '0xf1'})]"
    strategy6 = "[0,of_packet_in,*,DEL,field=(match.match)]"
    strategy7 = "[0,of_queue_get_config_reply,*,BUILD,type=(of_aggregate_stats_reply)&val=({'xid': '0x5502c42f', 'flags': '0xf6b6', 'packet_count': '0xe514eba1e014f151', 'byte_count': '0x693aadae70d1749c', 'flow_count': '0x6142bbc7'})]"
    strategy8 = "[0,of_flow_removed,*,MOD,field=(match.match.oxm_list.eth_type)&val=(0x93a2)]"
    strategy9 = "[0,of_role_reply,*,MOD,field=(role)&val=(0x2b20471b)]"
    strategy10 = "[0,of_packet_in,*,ADD,field=(match.match)&val=({'in_phy_port': '0xfffffff7'})]"
    strategy11 = "[0,of_port_stats_reply,*,ADD,field=(entries.port_stats_entry)&val=({'port_no': '0xba100c09', 'rx_packets': 0, 'tx_packets': '0xae69831f1f1da02a', 'rx_bytes': '0xb362e76ae0e72589', 'tx_bytes': '0x2a757497757bd8f2', 'rx_dropped': '0x63ee2b03667c4ba5', 'tx_dropped': '0xfd270ac6a114252a', 'rx_errors': '0xc68dad04d417c2a6', 'tx_errors': '0x47180883473bd817', 'rx_frame_err': '0xee11c8dc09335abc', 'rx_over_err': '0x57cfbbf9dc41f5d3', 'rx_crc_err': '0xd1b24e4cadeb8461', 'collisions': '0xc1aca9cca8fc20a2', 'duration_sec': '0x6e656fea', 'duration_nsec': '0x80875690'})]"
    strategy12 = "[0,of_aggregate_stats_reply,*,BUILD,type=(of_port_status)&val=({'xid': '0xed03e81c', 'reason': '0x31', 'desc': {'port_desc': {'port_no': '0x4356bc10', 'hw_addr': '[101, 135, 129, 252, 29, 29]', 'name': 'ZR53fFHwpamnNYhA9vB', 'config': '0xb929481f', 'state': '0xa0a0d76f', 'curr': '0x24def02f', 'advertised': '0x5fef1881', 'supported': '0xdcac5049', 'peer': '0x280b1a5c', 'curr_speed': '0xff5941b9', 'max_speed': '0xaf325c5a'}}})]"

    strategy13 = "[0,of_packet_in,*,BUILD,type=(of_flow_stats_reply)&val=({'xid': '0xaf1db94c', 'flags': '0x68cc', 'entries': [{'flow_stats_entry': {'table_id': '0xc', 'duration_sec': '0x2c6e0ed', 'duration_nsec': '0xece545af', 'priority': '0x686d', 'idle_timeout': '0xe5b8', 'hard_timeout': '0xf726', 'flags': '0x961a', 'cookie': '0x406e00f3', 'packet_count': '0x9bc37b2f5d8c7692', 'byte_count': '0x2eb650c5c61a1d32', 'match': {'match': {'oxm_list': [{'arp_tha': '[58, 207, 23, 126, 58, 161]', 'eth_dst': '[210, 106, 87, 119, 79, 197]', 'ipv6_dst': 'b5258bcbeec178a66388a30a008e068b', 'arp_spa': '0xe9d25247', 'tcp_dst': '0xe55b', 'ipv4_dst': '0xb4e2d23e', 'icmpv4_type': '0x82', 'ipv6_nd_target': '287d1e55fd6833b681801e660d651bbb', 'vlan_pcp': '0xe3', 'metadata': '0x8a3df42501df75e8', 'mpls_label': '0x9a9c60ad', 'arp_sha': '[10, 150, 119, 153, 34, 48]', 'sctp_src': '0x5292', 'eth_type': '0xc705', 'in_phy_port': '0x2629bd89', 'vlan_vid': '0x5dd5', 'ipv6_nd_tll': '[168, 2, 100, 204, 16, 190]', 'ipv6_flabel': '0xfec190a0', 'arp_tpa': '0x23e92cd0', 'eth_src': '[237, 204, 70, 231, 187, 64]', 'sctp_dst': '0x5734', 'in_port': '0xfa58adac', 'ipv6_src': '3a7b40a408130c33a7cb2323e30f8284', 'arp_op': '0x4a9e'}]}}, 'instructions': [{}]}}]})]"
    strategy14 = "[0,of_packet_in,*,MOD,field=(total_len)&val=(0x810b)|MOD,field=(version)&val=(0x07)]"
    strategy15 = "[0,of_packet_in,*,MOD,field=(total_len)&val=(0x810b)|DUP,n=2|BUILD,type=(of_features_request)&val=({'xid': '0xde000f6f'})|DROP,f=True]"
    strategy16 = "[0,of_role_reply,*,DELAY,s=1|MOD,field=(role)&val=(0x2b20471b)|DUP,n=5|DROP,f=True]"
    strategy17 = "[0,of_role_reply,*,DELAY,s=1|MOD,field=(role)&val=(0x2b20471b)|DUP,n=5|DELAY,s=2|DELAY,s=3|DELAY,s=4]"
    strategy18 = "[0,of_role_reply,*,DELAY,s=1|DUP,n=5|DUP,n=6|DUP,n=7|DUP,n=8|DUP,n=9]"
    strategy19 = "[0,of_role_reply,*,DELAY,s=1|MOD,field=(role)&val=(0x2b20471b)|MOD,field=(role)&val=(0x12345678)|MOD,field=(role)&val=(0x76543210)|MOD,field=(role)&val=(0x22223333)|MOD,field=(role)&val=(0x44445555)]"
    strategy20 = "[0,of_role_reply,*,MOD,field=(total_len)&val=(0x810b)|MOD,field=(version)&val=(0x07)|DELAY,s=1|MOD,field=(role)&val=(0x2b20471b)]"

    genetic_solve()