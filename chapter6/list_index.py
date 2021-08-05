lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 如果有多个相同元素，只返回第一个元素的索引
# print(lst.index('python'))  # 不存在
print(lst.index('hello', 1, 4))  # 左闭右开[....)

arr = "Wow You Can Really Dance"
print(arr.index('C'))
