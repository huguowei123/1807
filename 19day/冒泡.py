list = [1,2,4,65,7,8,6,64,86]
for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
print(list)

