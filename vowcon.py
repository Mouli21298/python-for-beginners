def vowcons(string):
    vow=0
    con=0
    for i in range(0,len(string)):
        if(string[i]=='a' or string[i]=='e' or string[i]=='i' or
           string[i]=='o' or string[i]=='u'):
            vow+=1
        if(string[i]=='A' or string[i]=='E' or string[i]=='I' or
           string[i]=='O' or string[i]=='U'):
            vow+=1
        con=len(string)-vow
    print("vowels="+str(vow))
    print("consonants="+str(con))
vowcons("Mouli")
