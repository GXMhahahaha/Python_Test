# 判断元素是否在集合中
s = {'Python', 'Hello', 98, 98, 98.3}
print('Python' in s, 88 not in s)

# 集合元素的添加操作
s.add(65)
print(s)

s.update({666, 'sabi'})  # 添加多个元素
print(s)

s.update(['zhizhang', 'Bill'])
print(s)

# 集合删除
s.remove(98)
# s.remove(500) 报错
print(s)
s.discard(500)  # 不会报错

s.pop()  # 随意删除一个元素
print(s)

# s.pop(400)  不能添加参数
print(s)

s.clear()
print(s)

