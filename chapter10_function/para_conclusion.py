# 默认传递参数
def fun(a, b=10):  # b有一个默认值
    print(a + b)


x = 100
y = 200
fun(x)
fun(x, y)


def fun1(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun1(11, 22, 33)
print()
lst = [11, 22, 33]
fun1(*lst)  # 在函数调用时，将列表中每个元素拆开

fun1(a=111, b=222, c=333)  # 关键字实参
print()
dic = {'a': 111, 'b': 222, 'c': 333}
fun1(**dic)  # 两个*


def fun2(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


temp = fun2(43, 54, 23, 12, 54)
print(temp)


def fun3(**kwargs):
    summ = 0
    for i in kwargs:  # 遍历的是键
        summ += kwargs[i]
    return summ


temp = fun3(a=100, b=200, c=300)
print(temp)


def fun4(a, b, *, c, d): # *之后的只能使用关键字传递
    print(a, b, c, d)


fun4(1, 2, c=3, d=4)
# fun4(1, 2, 3, 4) 报错
