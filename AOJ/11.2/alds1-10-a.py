def fib(n):
    f=[0]*(n+1)
    f[0]=1
    f[1]=1
    if(n<=1):
        return f[n]
    
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]  

n=int(input())
ans=fib(n)
print(ans)
