i = 1
while i:
    try:
        n1 = int(input())
        n2 = int(input())
        re = n1 / n2

    except BaseException as e:
        print(e)

    else:
        print(re)
        break
    finally:
        print("无论是否异常都会执行的代码")
print("程序结束")
