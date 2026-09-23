def checkNum(a):
    if(a>0):
        return 'Positive'
    elif(a<0):
        return 'Negative'
    else:
        return 'Zero'
b=-8976
print("The Number",b,"is ",checkNum(b))
