uy=list(str(input()))
v=0
for i in range (len(uy)):
  if(uy[i]=='a' or uy[i]=='e' or uy[i]=='i' or uy[i]=='o' or uy[i]=='u'or uy[i]=='A' or uy[i]=='E' or uy[i]=='I' or uy[i]=='O' or uy[i]=='U'):
     v+=1
if(v>0):
  print("yes")
else:
  print('no')
