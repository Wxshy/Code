list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
def mergeList(l1, l2):
    mergedList = l1
    for i in range(len(l2)):
        mergedList.append(l2[i])
    mergedList.sort()
    return mergedList

print(len(set(list1))-1)


