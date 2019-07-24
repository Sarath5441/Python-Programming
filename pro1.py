gj=int(input())
df=[]
for i in range(0,gj):
 ij=input()
 df.append(ij)
ff8=[]
for i in zip(*df):
 if(i.count(i[0])==len(i)):
  ff8.append(i[0])
 else:
  break
print(''.join(ff8))
