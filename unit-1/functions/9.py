def fact(a):
    i=1
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
print(fact(5))
