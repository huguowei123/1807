list = []
list1 = [1,2,3,4]
list.append(1)
print(list)
list.append(2)
print(list)
list.append(3)
print(list)
list.append(4)
print(list)
list.extend(list1)
print(list)
for i in list:
	print("%s"%i)
