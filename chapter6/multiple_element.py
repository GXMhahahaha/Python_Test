lst = ['hello', 'world', 98, 'hello', 'world', 234]
lst2 = lst[1:3:1]
print(lst2)  # 左闭右开

print(id(lst))
print(id(lst2))  # 这是一个新的对象
print(lst[0:5:2])  # 步长是2
print(lst[0:5])  # 缺省缺的是步长
print(lst[:5:2])  # 默认从0开始
print(lst[0::1])  # 默认到最后结束

print(lst[::-1])  # 从后向前输出
print(lst[7::-1])
print(lst[-1:-6:-1])  # 左闭右开
print(lst[6:0:-1])  # 左闭右开


