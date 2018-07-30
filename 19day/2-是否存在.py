list = [1,2,3,4,43,45,3,65,65,767,676,8]
num = int(input("输入数值"))
'''
if num in list:
	for p,i in enumerate(list):
		if i == num:
			print("索引是%d"%p)
			print(list)
			break
else:
	print("不存在")
'''
'''
if num in list:
	print(list.index(num))
else:
	print("无")
'''
p = 0
if num in list:
	for i in list:
		if i == num:
			print("索引是%d"%i)
			break
		p += 1
else:
	print("wu")
