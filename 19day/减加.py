sum = 0
sum1 = 0
for i in range(1,100):
	if i %2 == 1:
		sum += i
	else:
		sum1 -= i
print(sum+sum1)
