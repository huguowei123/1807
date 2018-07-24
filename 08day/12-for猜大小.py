import random
a = random.randint(1,100) 
for i in range(1,11):
	player = int(input("猜的数字"))
	if player > a:
		print("大了")
	elif player < a:
		print("小了")
	elif player == a:
		print("对啦")
		break
