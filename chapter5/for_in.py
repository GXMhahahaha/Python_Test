# 从字符串中取出字母
for item in 'Python':
    print(item)

# range生成一个整数序列
for i in range(10):
    print(i)

# 如果不需要用到循环变量
for _ in range(10):
    print("人生苦短，我用python")

summ = 0
for i in range(1, 101):
    if i % 2 == 0:
        summ += i

print(summ)
