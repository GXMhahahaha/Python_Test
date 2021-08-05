# 元组是不可变序列，不能进行增删改
# ----------------可变序列----列表，字典-------------------
# 内存地址不会发生更改

lst = [10, 20, 30, 40]
print(lst, id(lst))
lst.append(50)  # 不会改变列表的地址
print(lst, id(lst))

dic = {"Bill": 43, "Tommy": 70, "July": 100}
print(dic, id(dic))
dic["Monica"] = 99
print(dic, id(dic))

# --------------不可变序列----字符串，元组------------------
# 内存地址发生了改变，不再是同一个数据
s = 'hello'
print(s, id(s))
s += 'world'
print(s, id(s))

t = ('Python', 'hello', 90)
print(t, type(t))
