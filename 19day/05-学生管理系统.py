list = []
code = 1000
def showError(mag):  #显示错误
	print("输入有误，重新输入"+msg)
def is
def add():
	student = {}
	while True:
		name = input("输入学生名字")
		if len(name) >= 2 and len(name) <= 4:
			student["name"] = name
			break
		else:
			showError("学生姓名必须大于2小于4")
	while True:
		age = input("输入年龄")
		if age.isdigit():
			age = int(age)
		else:
			print("输入有误")
			continue
		if age > 1 and age < 130:
			student["age"] = age
			break
		else:
			showError("年龄必须大于1小于120")
	list.append(student)
	print("添加成功")
	address = input("输入住址")
	student["address"]=address
	phone = int(input("输入电话"))
	student["phone"]=phone
	list.append(student)
	print(list)
def find():
	name = input("输入学生名字")
	for student in list:
		if student["name"] == name:
			print("学生名字:%s\n学生年龄:%d\n学生住址:%s\n学生电话:%d\n")	
			break
def change():
	name = input("输入要修改的名字")
	for student in list:
		if student["name"] == name:
			print("1:修改名字")
			print("2:修改年龄")
			print("3:修改住址")
			print("4:修改电话")
			num = int(input("输入序号"))
		if num == 1:
			name = input("输入新名字")
			student["name"]=name
		elif num == 2:
			age = input("输入新年龄")
			student["age"]=age
		elif num == 3:
			address = input("输入新住址")
			student["address"]=address
		elif num == 4:
			phone = input("输入新电话")
			student["address"]=address
			break
def delete():
	name = input("输入名字")
	for student in list:
		if student["name"] == name:
			list.remove(student)
			print("删除成功")
			break
def print_list():
	
	for student in list:
		print("%s        %d        %s        %s"%(student["name"],student["age"],student["address"],student["phone"]))





def print_menu():
	print("欢迎进入学生管理系统".center(50," "))
	while True:
		print("1:添加学生")
		print("2:查找学生")
		print("3:修改学生")
		print("4:删除学生")
		print("5:打印学生信息")
		print("6:退出学生系统")
		input_information()
def input_information():
	num = input("选择功能")
	if num.isdigit():
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
print_menu()
