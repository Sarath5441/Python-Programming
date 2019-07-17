u=int(input())
if u!=0:
	print(1,end=' ')
	o=1
	k=0
	for i in range(1,u):
		z=k+o
		print(z,end=' ')
		k=o
		o=z
else:
	print(0)
