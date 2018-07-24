a = int(input ("请输入数字"))
if (a%4 == 0 and a%100 != 0) or (400%a == 0):	
	print("润年")
else :
	print("平年")
