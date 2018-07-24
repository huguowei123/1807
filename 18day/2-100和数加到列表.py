ist = [] # 定义一个空列表
for i in range(2,101):
	for j in range(2,i):
		if i%j == 0:
			list.append(i)	
print(list)
