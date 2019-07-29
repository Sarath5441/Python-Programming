from fractions import gcd
o,l=map(int,input().split())
u=[]
y=list(map(int,input().split()))
for i in range(0,l):
  e,f=list(map(int,input().split()))
  u.append([e,f])
for j in u:
  f=j[0]-1
  g=j[1]-1
  print(gcd(y[f],y[g]))
