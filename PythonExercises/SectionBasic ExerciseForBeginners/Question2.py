# Given a range of first 10 numbers, Iterate from start
# number to the end number and print
# the sum of the current number and previous number

num = input("input the number: ")
for x in range(int(num)):
    if x == 0:
        print("Current number "+str(x)+" previous number "+str(x)+" Sum: "+str((x+x)))
    else:
        print("Current number "+str(x)+" previous number "+str(x-1)+" Sum: "+str((x+(x-1))))