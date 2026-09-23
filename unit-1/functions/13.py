string = 'ayush'
reverse = ''

for i in range(len(string)):
    last_char=string[-1]
    string = string[:-1]
    reverse += last_char    
print(reverse)
