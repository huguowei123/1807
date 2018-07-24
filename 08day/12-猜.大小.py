import random
i = 0
a = random.randint(1,100)
while i < 9:
	b = int(input("猜的数字"))
	if b > a:
		print("猜大了") 
	elif b < a:
		print("猜小了")
	else:
		print("你真棒")
	i+=1
