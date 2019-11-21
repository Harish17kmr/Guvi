a=[]
a=input().split()
odd=[]
even=[]
for i in a:
	if(int(i)%2==0):
		even.append(i)
	else:
		odd.append(i)
print(odd)
print(even)