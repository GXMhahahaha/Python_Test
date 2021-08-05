def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100  # n1不会改变
    arg2.append(20)  # n2末尾会增加20


# return可以省略不写

n1 = 30
n2 = [2, 4, 6, 8]
print('n1', n1)
print('n2', n2)

fun(n1, n2)
print('n1', n1)
print('n2', n2)

# 在函数调用过程中修改不可变对象不会影响变量值
# 如果是可变对象则在函数体内的修改会影响到实参的值
