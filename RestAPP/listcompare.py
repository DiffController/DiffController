import dictdiffer

def similaritycal(dictA,dictB):
    for item in dictA.items():
        if type(item[1]) == list:
            new_value = str(item[1])
            dictA[item[0]] = new_value
    for item in dictB.items():
        if type(item[1]) == list:
            new_value = str(item[1])
            dictB[item[0]] = new_value
    sharedValue = set(dictA.items()) & set(dictB.items())
    dictLength = len(dictA)
    scoreOfSimilarity = len(sharedValue)
    similarity = scoreOfSimilarity/dictLength
    return similarity

def infodifferdict(list1,list2):
    result = None
    
    if len(list1) == 0 and len(list2) == 0:
        return ('unchange','','')
    r1 = range(len(list1))
    r2 = range(len(list2))
    for item in list1:
        item["pair"] = False
    for item in list2:
        item["pair"] = False

    for i in r1: 
        for j in r2:
            if list1[i]["pair"] ==True or list2[j]["pair"] == True:
                continue
            else:
                diff_list = list(dictdiffer.diff(list1[i], list2[j]))
                if diff_list == []:
                    list1[i]["pair"] = True
                    list2[j]["pair"] = True     

    unpairlist1 = []
    unpairlist2 = []

    for item in list1:
        if item["pair"] == False :
            unpairlist1.append(item)

    for item in list2:
        if item["pair"] == False :
            unpairlist2.append(item)

    change_pair_list = []
    change_differ_list = []

    if len(unpairlist1) == 0 or len(unpairlist2) == 0 :
        if len(unpairlist1) == 0 and len(unpairlist2) == 0:
            result = ('unchange','','')
        elif len(unpairlist1) > len(unpairlist2):
            for item in unpairlist1:
                del item['pair']
            result = ('remove',len(unpairlist1) - len(unpairlist2),unpairlist1)
        elif len(unpairlist1) < len(unpairlist2):
            for item in unpairlist2:
                del item['pair']
            result = ('add',len(unpairlist2) - len(unpairlist1),unpairlist2)

    elif len(unpairlist1) == len(unpairlist2):
        r1 = range(len(unpairlist1))
        r2 = range(len(unpairlist2))
        for i in r1: 
            score_list = []
            for j in r2:
                score_list.append(similaritycal(unpairlist1[i],unpairlist2[j]))
            max_index = score_list.index(max(score_list))
            if unpairlist1[i]["pair"] == False and unpairlist2[max_index]["pair"] == False:
                unpairlist1[i]["pair"] = True
                unpairlist2[max_index]["pair"] = True
                del unpairlist1[i]['pair']
                del unpairlist2[max_index]['pair']
                change_pair_list.append([unpairlist1[i],unpairlist2[max_index]])
                change_differ_list.append(list(dictdiffer.diff(unpairlist1[i], unpairlist2[max_index])))
        result = ('change',change_pair_list,change_differ_list)
        
    return result

def infodifferlist(list1,list2):
    """ here list1&list2 don't have nested structure,for example [{},{}] """ 
    result = None
    if len(list1) >= len(list2):
        diff_set = set(list1).difference(set(list2))
        result = ('remove',len(list1)-len(list2),list(diff_set))
    elif len(list1) < len(list2):
        diff_set = set(list2).difference(set(list1))
        result = ('add',len(list2)-len(list1),list(diff_set))
    if diff_set == set():
        result = ('unchange','','')

    return result

def infodifferset(set1,set2):
    """here want to compare set1 & set2 """
    result = None
    same_value = set1 & set2
    
    if len(same_value) == len(set1) == len(set2):
        result = ('unchange','','')
    else:
        if len(set1) > len(set2):
            diff_set = set1.difference(set2)
            result = ('remove',len(set1)-len(set2),list(diff_set))
        elif len(set1) < len(set2):
            diff_set = set2.difference(set1)
            result = ('add',len(set2)-len(set1),list(diff_set))
        elif len(set1) == len(set2):
            set_before = set1.difference(set2)
            set_after = set2.difference(set1)
            result = ('change',set_before,set_after)
    return result