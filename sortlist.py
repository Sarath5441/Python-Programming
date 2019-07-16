n=int(input())
a=list(map(int,input().split()))
if(len(a)==n):
 a.sort()
 for i in range(len(a)):
   print(a[i],end=" ") 
