list = [1,2,3,6,7,8,9,10,12]
min = 0
max = len(list)-1
count = 7
while True:
	center = int((min+max)/2)
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center + 1
	elif list[center] == count:
		print("索引%d"%center)
		break
