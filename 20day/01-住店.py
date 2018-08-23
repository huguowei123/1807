l = []`
def print_menu:
	print("住店系统")
	print("1:入住")
	print("2:离店")
	print("3:统计")
	print("4:退出")
	input_info():
def print_info():
	if num == 1:
		add()
	elif num == 2:
		leave()
	elif num == 3:
		count()
	elif num == 4:
		exit()
def add():
	a = {}
	while True:
	name = input("请输入姓名")
	num = int(input("请输入身份证号"))
	if len(num) == 18:
		print("入住成功")
		c = time.time  #入住时间
	else:
		print("请重新输入")
		break
def leave():
	name = input("请输入离店人姓名")
	a["name"] = name
	l.remove(name)
		print("删除成功")
	print(l)
def count():
	money = float(input("输入收益"))
	b = time.time  #当前时间
	if(b-c)%86400 == 0:
		print("收益是%f((b-c)/86400*10).02"%money)
	else:
		print("收益是%f(int(((b-c)/86400)+1)*10).02"%money)
menu()
