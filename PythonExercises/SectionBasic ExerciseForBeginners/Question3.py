#Given a string, display only those
# characters
# which are present at an even index number.

def split(word):
    return [char for char in word]

word = input("Orginal String is ")
list1 = split(word)

for x in range(len(list1)):
    if x % 2 == 0:
        print(list1[x])
