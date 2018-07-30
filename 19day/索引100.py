list = [1,43,4,54,546,5,77,6878,675543,442212,44,65,7,8,]
def num():
		num = int(input("输入数值"))
		if num in list:
			print(list.index(num)) 
		else:
			print("不在")
	
num()
