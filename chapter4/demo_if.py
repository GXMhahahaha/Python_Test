money = 1000
s = int(input('请输入取款金额'))           # 默认输入都是字符串，需要强制类型转换
if money >= s:
    money = money-s
    print("取款成功 余额为：", money)
else:
    print("取款失败")
