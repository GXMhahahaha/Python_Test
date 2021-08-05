# 同一内容内存地址不会改变
a = 'Python'
b = "Python"
c = """Python"""
print(a, b, c)
print(id(a), id(b), id(c))

s1 = 'op#'
s2 = 'op#'
print(id(s1), id(s2))



