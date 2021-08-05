# 两种创建方式
t1 = ('Python', 'Hello', 99)
t2 = tuple(('Python', 'Hello', 99))
print(t1)
t1 = 'Python', 'Hello', 99  # 小括号可以省略

# 如果元组只有一个元素，必须加上逗号
t1 = 'Python',

print(t1, type(t1))
print(t2)

# 空元组
t3 = ()
t4 = tuple()
print(t3, type(t3), t4)
