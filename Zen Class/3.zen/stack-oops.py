class stack:
	def __init__(self):
		self.__items=[]
	def push(self,a):
		self.__items.append(a)
	def pop(self):
		return self.__items.pop()
s1=stack()
s1.push(3)
s1.push(8)
s1.pop()
print(s1.pop())

