list = []
for i in range(3):
	d = {}
	name = input("请输入名字")
	d["name"] = name
	age = int(input("请输入年龄"))
	d["age"] = age
	sex = input("请输入性别")
	d["sex"] = sex
	list.append(d)
print(list)
for i in list:
	for k,v in items():
		print(k,v)

