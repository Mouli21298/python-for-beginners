def firsthalf(string):
    str1=""
    for i in range(0,len(string)//2):
        str1+=string[i]
    return str1
def secondhalf(string):
    str2=""
    for i in range(len(string)-1,(len(string)//2)-1,-1):
        str2+=string[i]
    return str2
string=input("Enter a string:")
start=firsthalf(string)        
end=secondhalf(string)
if(start==end):
    print("Palindrome")
else:
    print("Not a Palindrome")
