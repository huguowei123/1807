def test(x,y,z):
	ret = z(x,y)
	return ret
ret = test(1,2,lambda x,y:x+y)
print(ret)
def test1(x,y):
	c = x+y
	return c


