name = input("输入备份文件名字")
f = open(name,"r")
content = f.read()
newname = name+"备份"
position = name.rfind(".")
newname = name[:]
