#Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

i = 6

for num in range(i):
    for i in range(num):
        print(num, end=" ")

    print()