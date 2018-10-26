l=int(input())
for i in range(l):
    p=list(input())
    x,y=input().split(" ")
    x,y=int(x),int(y)
    counta=0
    countb=0
    req=[]
    for i in p:
        if i=="a":
            counta=counta+1
        elif i=="b":
            countb=countb+1
    g=min(counta,countb)        
    req.append("ab"*g)
    counta=counta-g
    countb=countb-g
    while counta>0 or countb>0:
        if counta>0:
            for i in range(x):
                req.append("a")
                counta=counta-1
                if counta==0:
                    break
            if counta!=0:    
                req.append("*")
        elif countb>0:
            for i in range(y):
                req.append("b")
                countb=countb-1
                if countb==0:
                    break
            if countb!=0:    
                req.append("*")        
    print("".join(req))            
    print("Rey manoj gaa")    
