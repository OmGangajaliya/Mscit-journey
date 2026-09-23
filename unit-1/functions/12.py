vowels={'a','e','i','o','u'}
string='atmiya uniuersity'
stringLen = len(string)
count = 0
for i in range(stringLen):
        if string[i] in vowels:
            count+=1
print("Total Vowels : ",count)

