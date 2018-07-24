'''
1-----石头
2-----剪刀
3-----布
玩家：1---2 2---3 3---1
电脑：1
'''
import random
player = int(input("1.石头 2.剪刀 3.布"))
pc = random.randint(1,3)
if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
	print("玩家赢")
elif player == pc:
	print("平局")
else:
	print("电脑赢")
