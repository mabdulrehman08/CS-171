def total_tution(price,terms):
    return price*terms


p=233172
r=(0.055)/12
n=120
a=p*(r)

#print=(total_tution(19431,12))
#print=(total_tution(20014,10))
#print=(total_tution(20014,10))
#print=(total_tution(20015,10))

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

print(countdown(3))


