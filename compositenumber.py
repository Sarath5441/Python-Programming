zc=int(input())
fl=0
if(zc>2):
    for i in range(2,int(zc/2)+1):
        if zc%i==0:
            print("yes")
            fl=1
            break
if fl==0 or zc==2:
    print("no")
