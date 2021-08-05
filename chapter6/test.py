# 改变数值即改变对象
a = 10
print(a, id(a))
a = 20
print(a, id(a))

# 不改变数值就不改变对象
b = 10
print(b, id(b))
b = 20
print(b, id(b))

