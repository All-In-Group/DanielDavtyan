#Write a code to extract each digit from
# an integer, in the reverse order

num = 156481
str1 = " "
def split(word):
    return [char for char in word]

b = split(str(num))

b.reverse()
for x in b:
    str1 += x + " "

print(str1)


