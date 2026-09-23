data1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
target=7
low=0
high=len(data1)-1
mid=int(len(data1)/2)
isFound=False

if(target==data1[low]):
    print("target is at position data1[",low,"]")
    isFound=True
elif(target==data1[high]):
    print("target is at position data1[",high,"]")
    isFound=True

if(isFound==False):
    while(target!=data1[mid]):
        if(target!=data1[mid]):
            if(target>data1[mid]):
                low=mid
                mid=(low+high)//2
            elif(target<data1[mid]):
                high=mid
                mid=(low+high)//2
        else:
            print("target is at position data1[",mid,"]")
            print("l5")
            
print("target is at position data1[",mid,"]")
