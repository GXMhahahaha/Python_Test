lst = [90, 32, 12, 4, 32, 5, 41, 32, 5, 63]
print(lst, id(lst))
lst.sort()  # 默认升序
print(lst, id(lst))  # 没有新建链表

lst.sort(reverse=True)  # 参数赋值中间不要加空格
print(lst)
lst.sort(reverse=False)
print(lst)

# 方法2调用内置函数sorted()，会产生新的链表对象
lst = [90, 32, 12, 4, 32, 5, 41, 32, 5, 63]
new_lst = sorted(lst)
print(lst)
print(new_lst)
new_lst = sorted(lst, reverse=True)
print(new_lst)

lst = [90, 32, 12, 4, 32, 54.6, 41, 32, 5, 63]
print(lst)
lst.sort()
print(lst)

# print("hello", "world", sep='\t', end=' ')
