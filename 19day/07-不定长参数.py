'''
def cl(a,b,*c,**d):
	print(a)
	print(b)
	print(c)
cl(1,2,3,4,5)
'''
def test(a,*args,b=12,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
	sum = 0
	sum = sum+a
	for i in args:
		print(i)
		sum = sum+i
	sum = sum+b
	for n in kwargs.values():
		print(n)
		sum = sum+n
		continue
test(1,2,3,4,5,b=20,m=12,n=22)
print(sum)
