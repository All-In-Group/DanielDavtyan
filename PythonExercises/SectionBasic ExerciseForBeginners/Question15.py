#Write a function called exponent
# (base, exp) that returns an int
# value of base raises to the power of exp.

def pow(base, exp):
    originalNumber = base
    while exp > 1:
        base *=originalNumber
        exp -= 1
    return base
print(pow(5, 4))