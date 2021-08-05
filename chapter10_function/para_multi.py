# 默认传递参数
def fun(a, b=10):  # b有一个默认值
    print(a + b)


x = 100
y = 200
fun(x)
fun(x, y)


# 个数可变的参数
def fun1(*args):  # 只能有一个
    print(args)


# print(args[0] + args[1])


fun1(2)
fun1(30, 45)


def fun2(**args):
    print(args)


fun2(a=10)
fun2(a=10, b=20)
