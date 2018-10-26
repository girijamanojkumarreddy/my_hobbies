n=int(input())
for i in range(int(n**(1/3))):
    for j in range(int(n**(1/3))):
                if i!=j :
                    print(i**3+j**3)
                    print("This is a correct way")
