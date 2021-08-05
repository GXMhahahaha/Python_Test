pwd = "Bill"
i = 0

while i < 3:
    if input("请输入密码") == pwd:
        print("欢迎使用")
        break
    else:
        print("密码错误")
    i += 1

else:                               # 循环正常结束才会使用这个  这样使用会让人困惑  尽量不要用
    print("已冻结")