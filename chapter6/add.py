lst1 = [10, 20, 30, 40]
# 向列表末尾添加一个元素
print(lst1, id(lst1))
lst1.append(50)
print(lst1, id(lst1))  # 没有新建一个对象

# 向列表末尾至少添加一个元素
lst2 = ['hello', 'world']
lst1.append(lst2)
print(lst1)  # 作为一个元素输入

lst1.extend(lst2)
print(lst1)  # 插入多个元素

# 任意位置添加
lst1.insert(2, 'niubi')  # 第一个参数是位置，第二个是插入对象
print(lst1)

lst1 = [10, 20, 30, 40]
lst2 = ['hello', 'world']

lst1[1:] = lst2
print(lst1)

lst1 = [10, 20, 30, 40]
lst2 = ['hello', 'world']

lst1[1:2] = lst2  # 将[1,2)之间内容切掉并用lst2来替换
print(lst1)
