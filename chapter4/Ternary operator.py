# python语言是一步一步来解释的，后面又错误如果运行不到它也不会报错

num_a = int(input())
num_b = int(input())

# if num_a > num_b:
#     print(num_a, '大于', num_b)
# else:
#     print(num_a, '小于等于', num_b)

print((str(num_a) + '大于' + str(num_b)) if (num_a > num_b) else (str(num_a) + '小于' + str(num_b)))

x = int(input())
y = int(input())
Max = x if x > y else y
print("最大值为", Max)
