sa,sa2=map(int,input().split())
p=sa*sa2
for i in range(0,p+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
