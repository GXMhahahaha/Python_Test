print(520)
print(98.5)
print("helloworld")
# print(helloworld)  报错
print(3.4 + 8.2)
print("43+89")

# 输出到文件中
fp = open('C:/Users/18447/Desktop/test.txt', 'a+')  # a+表示追加
print("Helloworld", file=fp)
fp.close()

# 不进行换行输出
print("hello", "world", 3 + 5)  # ","直接换行
