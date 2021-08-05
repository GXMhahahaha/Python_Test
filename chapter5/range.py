# range()的三种创建方式
r = range(10)  # 从0开始 到9结束

for i in r:
    print(i)

print(r)
print(range(1, 100))
print(r)
print(list(r))  # list是列表

r = range(1, 10)  # 从1开始到9结束  左闭右开
print(list(r))

r = range(1, 10, 2)  # 步长为2
print(list(r))

print(9 in r)
print(10 in r)
print(9 not in r)

print("exist" if int(input("请输入一个数字\n")) in r else "not exist")
