def divisors(n):
    temp=n
    list=[];
    for i in range(1,temp+1):
        if(temp%i==0):
            list.append(i)
    print(len(list))
divisors(int(input("Enter a number")))
