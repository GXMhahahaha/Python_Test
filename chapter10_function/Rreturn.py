def fun(lis):
    odd = []
    even = []
    for i in lis:
        if i % 2:  # 0的bool值为False
            odd.append(i)
        else:
            even.append(i)
    return odd, even


a, b = fun([54, 2, 4, 43, 1, 34, 67, 542, 4])
print(a, b)

print(fun([1, 2, 3, 4, 5, 6, 7, 8]))  # 当返回值为多个时，结果为元组
