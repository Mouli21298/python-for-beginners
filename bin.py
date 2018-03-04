def binary(n):
    temp=n
    list=[];
    while(temp//2!=1):
        list.append(temp%2)
        temp=temp//2
    list.append(temp%2)
    list.append(temp//2)
    print (list)
    for i in range(len(list)-1,-1,-1):
          print(list[i])
binary(int(input("Enter a number")))
        
