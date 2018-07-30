list = []
def test():
	for i in range(5):
		l = []
		for a in range(3):
			grade = float(input("输入成绩"))
			l.append(grade)
		list.append(l)
	print(list)
maxgrade = 0
mi = 0
def bbu():
	global maxgrade
	global mi
	for p,i in enumerate(list):
		if sum(i) > maxgrade:
			maxgrade = sum(i)
			mi = p
	print(maxgrade)
	print(mi)
	print("平均值%.02f"%(maxgrade/3))
	print(list[mi][0],list[mi][1],list[mi][0])
test()
bbu()
