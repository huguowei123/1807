a = {"name":"小胡","sex":"男","birthday":"1996年3月一日","address":"山西"}
#添
a["age"]=18
print(a)
#改
a["address"]="河北"
print(a)
#删
a.pop("sex")
print(a)
#查
a["address"]
print(a["address"])
#遍历
for i in a:
	print(i)   #键
for i in a:
	print(a[i])    #值
for k,v in a.items():
	print(k)
	print(v)
