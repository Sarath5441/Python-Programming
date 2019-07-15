k=list(input())
g=len(k)
for i in range(0,g,2):
    k[i],k[i+1]=k[i+1],k[i]
print(*k,sep="")
