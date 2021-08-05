i = 1
while i:
    try:
        n1 = int(input())
        n2 = int(input())
        re = n1 / n2
        print(re)
        break

    except ZeroDivisionError:
        print("除数不能为0")

    except ValueError:
        print("请输入整数")

