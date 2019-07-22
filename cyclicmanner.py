    
m,ne=list(map(int,input().split()))
x=list(map(int,input().split()))
for s in range(0,ne):
  x=([x[-1]] + x[:-1])
print(*x)
