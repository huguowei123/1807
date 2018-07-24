a = input("请输入帐号")
b = input("请输入密码")
i = 1 
while i<4:
if a == "huguowei" and b == "123456":
	print("登录成功")
	x = input("0:ADC 1:肉 3:法师")				
	if x == "0":
		print("鲁班大师")
	elif x == "1":
		print("程咬金")
	elif x == "3":
		print("王昭君")
else:
	i+=1
	print("重新输入")

