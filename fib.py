def fibonacci(n):
    if n==1:
        fib=0
    f=0
    s=1
    i=0
    fib=f+s
    if n==1:
        fib=0
    while(i<n-2):
        fib=f+s
        f=s
        s=fib
        i=i+1
    print (fib);
num=input("no.");
fibonacci(int(num))
            
        
