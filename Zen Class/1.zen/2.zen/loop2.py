marks=[]
total=0
for i in range(1,6):
	marks.append(int(input("Enter the mark%d: "%i)))
for j in range(5):
	total=total+marks[j]
average=total/5
print("Total=",total)
print("Average=",average)
	
