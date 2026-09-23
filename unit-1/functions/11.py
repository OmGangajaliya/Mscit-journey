def find(a,b,c):
    if(a>b and a>c):
        return 'A is big'
    elif(b>c and b>c):
        return 'B is big'
    elif(c>a and c>b):
        return 'C is big'
    else:
        return 'All Equal'
a=10
b=290
c=90

print("A = ",a)
print("B = ",b)
print("C = ",c)
print("Result : ",find(a,b,c))
