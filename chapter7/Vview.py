scores = {'张三': 100, '李四': 90, '王五': 70}
keys = scores.keys()
print(keys, type(keys))

lst_k = list(keys)  # list函数转成链表
print(lst_k)
print(keys, type(keys))

values = scores.values()
print(values, type(values))

lst_y = list(values)
print(lst_y)

items = scores.items()  # key-value对
print(items, type(items))
# 转成的元素时元组
lst_t = list(items)
print(lst_t)