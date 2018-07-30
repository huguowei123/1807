'''
a = 1
def l():
	global a
	a = 3
	print(a)
l() 
print(a)
'''
'''
list = []
def l():
	list.append(10)
l()
print(list)
'''
def test(a,b,c,d = 10):
	f = a+b+c+d
	print(f)
test(1,2,3,5)
