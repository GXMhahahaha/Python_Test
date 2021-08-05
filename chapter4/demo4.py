ans = input('您是会员吗？y/n')
money = float(input("您的购物金额"))
if ans == 'y':
    if money >= 200:
        print(money * 0.8)
    elif 100 <= money < 200:
        print(money * 0.9)
    else:
        print(money)
else:
    if money >= 200:
        print(money * 0.95)
    else:
        print(money)
