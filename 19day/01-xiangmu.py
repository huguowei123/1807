list = []
def isNum(num): #判断是否是数字
	if num.isdigit():
		return True
	else:
		return False
def print_menu():
	print("欢迎进入点菜系统".center(50," "))
	while True:
		a = input("输入帐号")
		b = input("输入密码")
		if a != "aaa" and b != "111":
			print("重新输入")
		else:
			print("登录成功")
			while True:
				print("1:上菜")
				print("2:查菜")
				print("3:改菜")
				print("4:删菜")
				print("5:打印菜单")
				print("6:退出")
				input_info()  #调用选择功能函数
def input_info():
	num = input("请选择功能")
	if isNum(num):
		num = int(num)
	else:
		print("输入有误")
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 6:
		exit()
def add():
	dcb = {}
	while True:
		num = input("输入桌号")
		if isNum(num):
			num = int(num)
		else:
			print("输入有误")
			continue
		if num > 0 and num < 101:
			dcb["num"] = num
			break
		else:
			print("桌号必须大于0小于101")
	name = input("输入菜名")
	dcb["name"] = name
	while True:
		count = input("输入数量")
		if isNum(count):
			count = int(count)
		else:
			print("输入有误")
			continue
		if count > 0 and count < 11:
			dcb["count"] = count
			break
		else:
			print("数量必须大于0小于11")
	list.append(dcb)
	print("完成")
def find():
	num = int(input("输入要查找的桌号"))
	for dcb in list:
		if dcb["num"] == num:
			print("桌号:%d\n菜名:%s\n数量%d"%(dcb["num"],dcb["name"],dcb["count"]))
			break
def change():
	num = int(input("输入要修改菜名的桌号"))
	
	for dcb in list:
		if dcb["num"] == num:
				print("1:修改菜名")
				print("2:修改数量")
				num = input("请选择功能")
				if isNum(num):
					num = int(num)
				else:
					print("输入有误")
					continue
				if num == 1:
					name = input("请输入新菜名")
					dcb["name"] = name
				elif num == 2:
					count = int(input("请输入新数量"))
					dcb["count"] = count
			
			
def delete():
	num = int(input("请选择要删除的桌号"))
	for dcb in list:
		if dcb["num"] == num:
			list.remove(dcb)
			print("删除成功")
			break
def print_list():
	print("桌号        菜名        数量")
	for dcb in list:
		print("%d        %s        %d"%(dcb["num"],dcb["name"],dcb["count"]))
print_menu()
