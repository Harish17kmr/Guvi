numbers=int(input())
rev=0
while numbers>0:
	a=numbers%10
	rev=rev*10+a
	numbers=numbers//10
print(rev)