str=input()
j=len(str)-1
a=0
for i in range(0,len(str)):
	if(str[i]==str[j]):
		a+=1
		j=j-1
if(a==len(str)):
	print("Pallindrome")
else:
	print(" Not Pallinedrome")



