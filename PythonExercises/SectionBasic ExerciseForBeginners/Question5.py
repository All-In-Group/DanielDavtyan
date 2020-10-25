#Given a list of numbers, return True if
# first and last number of
# a list is same


def firstAndLastEquality(list1):
    lastIndex = len(list1)-1
    if(list1[0] == list1[lastIndex]):
        return True
    else:
        return False


list1  = [10, 20, 30, 40, 220]
print(firstAndLastEquality(list1))

