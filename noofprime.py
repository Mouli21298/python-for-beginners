def noofprime(start,end):
    countno=0
    for i in range(start,end+1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            countno+=1
    print ("The number prime no.s between the given range is "+str(countno))
start=int(input("Enter starting no."))
end=int(input("Enter ending no."))
noofprime(start,end)

    
        
