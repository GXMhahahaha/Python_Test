pwd = "Bill"
# flag = False
for _ in range(3):
    if input("请输入密码") == pwd:
        print("欢迎使用")
        # flag = True
        break
    else:
        print("密码错误")

else:                               # 循环正常结束才会使用这个
    print("已冻结")



