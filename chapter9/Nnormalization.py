name = 'Bill'
age = 22

# 使用%
print('我叫%s,今年%d岁了' % (name, age))  # 使用元组

# 使用{}
print('我叫{0},今年{1}岁了,今年真的{1}岁了'.format(name, age))

# python3以上 f-string
print(f'我叫{name},今年{age}岁了,今年真的{age}岁了')

# 宽度和精度
print("%10d" % age)

print('%.2f' % 3.1415926)

print('%10.2f' % 3.1415926)


