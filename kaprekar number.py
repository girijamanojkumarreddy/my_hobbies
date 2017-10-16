jklq=[]
for j in range(1000,10000):
    u=str(j)
    n=[]
    for m in u:
        n.append(int(m))
    count=0
    while True:
        n=sorted(n)
        sl=0
        su=0
        l=[]
        for i in range(len(n)):
            su=su+(n[i]*(10**i))
            sl=sl+(n[i]*(10**(len(n)-i-1)))
        diff1=su-sl
        count=count+1
        if count>=20:
            break
        diff=str(diff1)
        for k in diff:
            p=int(k)
            l.append(p)
        l=sorted(l)    
        if diff1==6174:
            
            jkl.append(count)
            break
        else:
            n=l
print(max(jklq))
