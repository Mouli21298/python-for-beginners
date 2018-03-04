string1=input("Enter first string")
string2=input("Enter secong string")
def ascii(string):
    value=0
    for i in range(0,len(string)):
        value+=ord(string[i])
    return value
if(ascii(string1)==ascii(string2)):
    print("Anagram")
else:
    print("Not a Anagram")
