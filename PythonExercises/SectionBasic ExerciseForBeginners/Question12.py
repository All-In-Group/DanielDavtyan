#Calculate income tax for the given income by
# adhering to the below rules
#First $10,000	0%
#Next $10,000	10%
#The remaining	20%


def percent(number, percent):
    return number * (percent/100)


def taxCounter(income):
    base = income - 20000
    tax = percent(base, 20)
    tax += 1000
    return tax

income = 45000
print(taxCounter(income))