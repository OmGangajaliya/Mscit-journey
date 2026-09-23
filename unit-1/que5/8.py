n=int(input("Enter Number to count : "))
count=0
while(n>0):
    count+=1
    n=int(n/10)
print("Length of Number : ",count)
