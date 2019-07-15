A,B=map(int,input().split())
for g in range(A+1,B):
    for h in range(2,g):
       if(g%h==0):
           break
    else:   
        print(g,end=" ")
