list = []
def print_menu():
	print("欢迎进入点菜系统".center(30," "))
	while True:
		print("1:上菜")
		print("2:查菜")
		print("3:换菜")
		print("4:撤菜")		
		print("5:打印菜单")
		print("6:退出")
		input_info()
def input_info(): # 选择
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
	else:
		showError()
def showError():
	print("输入有误,重新输入")
def isNum(num):
	if num.isdigit():
		return True
	else:
		return False
def add(): # 添加
	dcb = {}
	while True:
		num = input("请输入桌号")
		if isNum(num):
			num = int(num)
		else:
			print("输入有误")
			continue
		if num > 0 and num < 101:
			dcb["num"] = num
			break
		else:
			showError("桌号必须大于0小于101")
	while True:
		name = input("输入菜名")
		if len(name) >= 2 and len(name) <= 8:
			dcb["name"] = name
			break
		else:
			showError("菜名必须大于等于2小于8")
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
			showError("数量必须大于0小于11")
	list.append(eat)
	print("完成")
def find(): # 查看
	a = input("输入要查找桌号")
	for eat in list:
		if eat["a"] == a:
			print("桌号:%d\n菜名:%s\n数量%d"%(eat["a"],eat["name"],eat["count"]))
			break
def change(): # 修改
	while True:
		a = input("输入桌号")
		flag = False  #假定不存在
		for eat in list:
			if eat["name"] == name:
				print("1:修改菜名")
				print("2:修改数量")
				num1 = input("请选择功能")
				if isNum(num1):
					num1 = input(num1)
				else:
					print("输入有误")
					continue
				if num1 == 1:
					name = input("输入新菜名")
					eat["name"] = name
				elif num1 == 2:
					count = input("输入新数量")
					eat["count"] = count
					print("修改成功")
					break
				break
		if not flag:
			print("无")
def delete(): # 删除
	a = input("输入桌号")
	name = input("选择要删除的菜")
	for eat in list:
		if eat["name"] == name:
			list.remove(eat)
			print("删除成功")
			break
def print_list(): # 打印
	print("桌号        菜名        数量        ")
	for eat in list:
		print("%d        %s        %d"%(eat["a"],eat["name"],eat["count"]))	
		
print_menu()

