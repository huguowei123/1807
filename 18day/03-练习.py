
list = ["小胡","小李"]
list.append("小刘")  #加
print(list)
list.insert(1,"小周")
print(list)      #指定位置加
list.pop()     #最后一个删去
print(list)
list.pop(2)     #指定位置删去
print(list)
list.remove("小周")  #指名道姓删去
print(list)
list.extend("小明")   #分开加
print(list)
list1 = ["小红","小绿","小白"]
list.append(list1)   #列表套列表
print(list)
list[0]    #索引查人
print(list[0])
list[1]="小兰"     #索引改人
print(list)
