def a(num):
	if num == 1:
		return num
	else:
		return num*a(num-1)
return = a(5)
print(return)
