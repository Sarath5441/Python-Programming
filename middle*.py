fg=input()
n=len(fg)
if n%2!=0:
    fg=fg[:int(n/2)]+'*'+fg[int(n/2)+1:n]
else:
    fg=fg[:int(n/2)-1]+'**'+fg[int(n/2)+1:n]
print(fg)
