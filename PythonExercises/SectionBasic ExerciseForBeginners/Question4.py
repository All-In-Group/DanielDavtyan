#Given a string and an integer number n,
# remove characters from a string starting
# from zero up to n and return a new string



def split(str ,n):
    return str[n:]

word = "pynative"
num = 4
print(split(word, num))
