# 集合是可变的数据类型 只有key 没有 value 使用hash

s = {'Python', 'Hello', 98, 98, 98.3}  # 不能重复
print(s)

s = set(range(6))
print(s)

s = set([1, 2, 3, 4, 65])
print(s)

s = set({1, 2, 3, 4, 65})
print(s)

s = set((1, 2, 3, 4, 65))  # 65跑到前面去说明集合无序
print(s, type(s))

s = set('Python')
print(s)

s = {}  # 字典类型
print(s, type(s))

s = set()  # 集合类型
print(s, type(s))
