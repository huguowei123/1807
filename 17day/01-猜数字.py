import random
pc=random.randint(1,100)
i=1
while i<10:
	player=int(input("输入数值"))
	if player > pc:
		print("大了")
	elif player < pc:
		print("小了")
	elif player == pc:
		print("可以呀")  
		break
	i+=1
	
