 def fun(a, b):
    c = a + b  # c是局部变量，a，b也是局部变量
    print(c)


# print(c)

name = 'sabi'


def fun2():
    print(name)


fun2()


def fun(a, b):
    global c  # 声明为全局变量就可以使用了
    c = a + b  # c是局部变量，a，b也是局部变量
    print(c)


fun(1, 2)
print(c)
