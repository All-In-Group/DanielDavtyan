#Reverse a given number and return
# true if it is the same as the original number



def reverseNumber(num, ravednum=0):
    originalNum = num
    while num > 0:
        remind = num % 10
        revednum = (ravednum * 10) + remind
        num = num // 10

    if originalNum == originalNum:
        return True
    else:
        return False


num = 121
print(reverseNumber(num))