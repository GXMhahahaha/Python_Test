name = '张三'
age = 20
print(type(name), type(age))
print('我叫', name, '今年', age)
print('我叫' + name + '今年' + str(age) + '岁')  # 字符串拼接，如果不进行类型转换，字符串与整形无法拼接

a = 10
b = 134.5
c = False

print(type(a), type(b), type(c))
print(str(a), str(b), str(c))

# a = str(a)                                    # 这样可以真正转换
# print(a)
print(type(a), type(str(a)))  # 并没有真正转换原始数据的类型

a = '125'
# b = '7923.54'
c = 78.43
d = True
e = 'hello world'
print(int(a), int(b), int(c))  # 字符串为小数串报错
print(d, int(d))
# print(int(e))                                  #报错，非数字


print(str(a), str(b), str(c), str(d), str(e))
print(float(a), float(b), float(c), float(d))  # 在整形后面加上.0
