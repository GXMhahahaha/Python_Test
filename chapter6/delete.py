lst = [10, 20, 30, 40, 50, 30]
lst.remove(30)  # 移除某个指定元素有重复元素移除第一个
print(lst)
# lst.remove(60)
lst.pop(0)  # 移除索引位置元素
print(lst)
# lst.pop(10)
lst.pop()  # 不加参数则删除最后一个元素
print(lst)


print("----------切片操作----------------")
lst = [0, 1, 2, 3, 5, 6]
lst_new = lst[1:3]
print(lst)
print(lst_new)  # 会产生新的列表对象

lst = [0, 1, 2, 3, 5, 6]
lst[1:3] = []  # 用一个空列表来替代一部分元素从而达到删除一部分元素的目的
print(lst)

lst.clear()  # 清空元素
print(lst)

# del lst  # 直接删除列表
# print(lst)

lst = [0, 1, 2, 3, 5, 6]
del lst[0]
print(lst)

