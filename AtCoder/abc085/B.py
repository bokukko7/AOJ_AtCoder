def readinput():
    n=int(input())
    d=[]
    for i in range(n):
        d.append(int(input()))
    return (n,d)

def main(n,d):
    d.sort(reverse=True)
    npre=d[0]
    ndan=1
    for i in range(1,n):
        if(d[i]<npre):
            npre=d[i]
            ndan+=1
    
    return ndan

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    print(ans)
