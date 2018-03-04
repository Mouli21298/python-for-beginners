def firstocc(string):
    dict={}
    for i in range(0,len(string)):
        if(string[i] in dict):
            print(string[i])
            break
        else:
            dict[string[i]]=1
firstocc("abcda")
