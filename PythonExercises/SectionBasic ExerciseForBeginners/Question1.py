#Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

def sumAndProduct(integer1, integer2):
    if integer1*integer2 >= 1000:
        return integer1+integer2
    else:
        return integer1*integer2

num1 = int(input("Enter the first number"))
num2 = int(input("enter the second number"))


print(sumAndProduct(num1, num2))
