from statistics import median
n=int(input())
a=list(map(int,input().split()))
if(len(a)==n):
   a.sort()
   print(median(a))
