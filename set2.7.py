a=int(input())
sum=0
temp=a
while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
if(a==sum):
    print("yes")
else:
    print("no")
