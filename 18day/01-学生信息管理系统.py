student = []
while True:
	print("欢迎来到学生管理系统")
	print("1:添加学生")
	print("2:删去学生")
	print("3:查找学生")
	print("4:修改学生")
	print("5:欢迎下次使用")
	a = {}
	sum = int(input("请选择功能"))
	if sum == 1:
		print("添加")
		name = input("请输入名字")
		a["name"]=name
		age = int(input("请输入年龄"))
		a["age"] = age
		address = input("请输入住址")
		a["address"] = address
		phone = int(input("请输入电话"))
		a["phone"] = phone
		print("a")
		student.append(a)
		print(student)
	elif sum == 5:
		print("欢迎下次使用")
	elif sum == 3:
		name = input("输入学生名字")
		for a in student:
			if a["name"] == name:
				print("学生名字:%s\n学生年龄:%d\n学生住址:%s\n学生电话%d\n"%(a["name"],a["age"],a["address"],a["phone"]))
	elif sum == 4:
		print("1:修改学生名字") 
		print("2:修改学生年龄")
		print("3:修改学生住址")
		print("4:修改学生电话")
		num = int(input("输入修改序号"))
		if num == 1:
			name = input("输入新名字")
			a["name"]=name
		elif num == 2:
			age = int(input("输入新年龄"))
			a["age"]=age
		elif num == 3:
			address = input("输入新住址")
			a["address"]=address
	elif sum == 2:
			name = input("输入名字")
			for a in student:
				if a["name"] == name:
					student.remove(a)
					print("删除成功")		
