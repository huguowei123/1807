i = 1
a = 0
b = 0
while i < 100:
	if a%2 == 0:
		a+=1
	elif b%2 == 1:
		b+=1
	i+=1
	print("输出数值%d"%(b-a))
