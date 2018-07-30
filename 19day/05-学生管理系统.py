list = []
code = 1000
def showError(mag):  #显示错误
	print("输入有误，重新输入"+msg)
def isNum(num):#判断是否一个数字
	if num.isdigit():
		return True
	else:
		return False
def add():#添加功能
	stu = {}
	while True:
		name = input("输入学生名字")
		if len(name) >= 2 and len(name) <= 4:
			stu["name"] = name
			break
		else:
			showError("学生姓名必须大于2小于4")
	while True:
		age = input("输入年龄")
		if isNum(age):
			age = int(age)
		else:
			print("输入有误")
			continue
		if age > 1 and age < 120:
			stu["age"] = age
			break
		else:
			showError("年龄必须大于1小于120")
	if len(list) == 0:
		stu["code"]=code
	else:
		stu["code"] = list[len(list)-1]["code"]+1
	stu["isdelete"] = False 
	list.append(stu)
	print("添加成功")
def find():
	name = input("输入学生名字")
	for stu in list:
		if stu["name"] == name:
			print("学生名字:%s\n学生年龄:%d"%(stu["name"],stu["age"]))	
			break
def change():
	name = input("输入要修改的名字")
	flag = False#假设这里头没有
	for stu in list:
		if stu["name"] == name:
			flag = True
			while True:
				print("1:修改名字")
				print("2:修改年龄")
				num = input("输入序号")
				if isNum(num):
					num = int(num)
				else:
					print("输入有误")
					continue
				if num == 1:
					name = input("输入新名字")
					stu["name"] = name
				elif num == 2:
					age = int(input("输入新年龄"))
					stu["age"] = age
				break
			break
	if not flag:
		print("查无此人")
def delete():
	name = input("输入要删的名字")
	delist = []
	for stu in list:
		if stu["name"] == name:
			#list.remove(stu)   #物理删除
			dellist.append(stu)
			stu["isdelete"] = True#非物理删除
			print("删除成功")
			break
	if dellist:
		print("序号      姓名      年龄      学号")
		for p,stu in enumerate(sellist):
			print("%d        %s        %d        %d"%(p+1),stu["name"],stu["age"],stu["code"])
def print_list():
	print("姓名      年龄      学号")
	for stu in list:
		if stu["isdelete"] == Flase:
			print("%s        %d        %d"%(stu["name"],stu["age"],student["code"]))





def print_menu():
	print("欢迎进入学生管理系统".center(50," "))
	while True:
		print("1:添加学生")
		print("2:查找学生")
		print("3:修改学生")
		print("4:删除学生")
		print("5:打印学生信息")
		print("6:退出学生系统")
		#input_information()
def input_info():
	num = input("选择功能")
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
		delete
def print_menu():
