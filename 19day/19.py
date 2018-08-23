import random 
pc = random.randint(1,3)
player = int(input("输入数值"))
if(player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
	print("player赢")
elif player == pc:
	print("平")
else:
	print("pc赢")

