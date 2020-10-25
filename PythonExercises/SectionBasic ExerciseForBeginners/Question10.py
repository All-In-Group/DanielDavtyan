#Given a two list of numbers create a new
# list such that new list should contain
# only odd numbers from the first list
# and even numbers from the second list

def mergingLists(list1, list2):
    list3 = []
    for x in list1:
        if x%2 != 0:
            list3.append(x)
    for x in list2:
        if x%2 == 0:
            list3.append(x)
    return list3


firstList = [10, 20, 23, 11, 17]
secondList = [13, 43, 24, 36, 12]

print(mergingLists(firstList, secondList))