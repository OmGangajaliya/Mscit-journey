def palin(string):
    reverse=''
    for i in range(len(string)):
        last_char=string[-1]
        string = string[:-1]
        reverse += last_char
    return reverse
string = 'omo'
reverse=palin(string)
if(string==reverse):
    print("Palindrome")
else:
    print("Not Pallindrome")
