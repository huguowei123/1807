student = []
while True:
	print("欢迎进入学生管理系统.py")
	print("1:新增学生")
	print("2:查找学生")
	print("3:修改学生")
	print("4:删减学生")
	print("5:欢迎下次使用")
	a = {}
	num = int(input("请输入序号"))
	if num == 1:
		print("新增")
		name = input("请输入名字")	
		a["name"] = "name"
		age = int(input("请输入年龄"))
		a["age"] = "age"
		address = input("请输入住址")
		a["address"] = "address"
		phone = int(input("请输入电话"))
		a["phone"]="phone"
		
