names = ["小胡","小齐","小黑"]
for i in names:
	print("hello%s"%i)
print(names[0])
print(names[1])
print(names[2])
way = ["骑马","开车","骑电动"]
for a in way:
	print("I like%s"%a)	
for i in names:
	print("%s我想请你下饭店"%i)
print("小黑有事来不了")
names[2] = "小周"
print(names)	
for c in names:
	print("吃饭去，%s"%c)
print("我找到一个更大的餐桌")
names.insert(0,"小李")
print(names)
names.insert(2,"小刘")
print(names)
names.append("老宋")
print(names)
for c in names:
	print("我想请你吃饭，%s"%c)
print("我只能请俩个人吃饭")
names.pop()
print(names)
print("小周我不能请你吃饭了")
names.pop()
print(names)
print("小齐我不能请你吃饭了")
names.pop()
print(names)
print("小刘我不能请你吃饭了")
names.pop()
print(names)
for d in names:
	print("我仍要邀请你，%s"%d)
names.pop()
print(names)
names.pop()
print(names)
