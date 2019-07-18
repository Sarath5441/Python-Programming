Np=int(input())
fl=0
if Np>2:
    for i in range(3,int(Np/2)):
        if Np%i==0:
            fl=1
            print("no")
            break
if fl==0 or Np==2:
    print("yes")
