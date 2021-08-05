a = 3 + 4
print(a)

# 支持链式赋值
a = b = c = 100
print(a, id(a))
print(b, id(b))
print(c, id(c))  # 其实只有一个变量

a = 98
b = a
print(a, id(a))
print(b, id(b))  # 其实只有一个变量

a = 20
a += 30
print(a, type(a))
a /= 3
print(a, type(a))
a //= 2
print(a, type(a))

a, b, c = 20, 30, 40    # 黄色波浪线表示代码不规范
print(a, id(a))
print(b, id(b))
print(c, id(c))

a, b = b, a             # 实现交换功能
print(a, b)



