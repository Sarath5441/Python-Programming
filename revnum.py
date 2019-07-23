nu=int(input())
rev=0
while(nu>0):
    dig=nu%10
    rev=rev*10+dig
    nu=nu//10
print(rev)
