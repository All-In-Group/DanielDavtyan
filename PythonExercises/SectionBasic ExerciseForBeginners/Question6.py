#Given a list of numbers, Iterate it and
# print only those numbers which are
# divisible of 5

def isDevideToFive(list1):
    print("Divisible of 5 in a list")
    for x in range(len(list1)):
        if list1[x] % 5 == 0:
            print(str(list1[x]))


list1 = [10, 20, 33, 46, 55]
isDevideToFive(list1)
