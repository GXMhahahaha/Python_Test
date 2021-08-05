# 输出100到999之间的水仙花数
for i in range(100, 1000):
    temp = i
    ge = i % 10
    i //= 10                # 整除
    shi = i % 10
    i //= 10
    bai = i
    # print(bai, shi, ge)
    if temp == ge ** 3 + shi ** 3 + bai ** 3:
        print(temp)
