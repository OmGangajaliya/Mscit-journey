n=int(input("Enter Number to Reverse : "))
rev=0
digit=1
while(n>0):
    digit=n%10
    n=int(n/10)
    if(rev==0):
        rev=digit
    else:
        rev=((rev*10)+digit)
print(rev)
