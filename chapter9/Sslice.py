s = 'hello world'
s1 = s[:5]  # 从0开始  左闭右开
print(s1)
s2 = s[6:]  # 切到结尾
print(s2)
s3 = s1 + '!' + s2
print(s3)

print(s[1:8:2])  # [起始，结束) 步长
print(s[::2])
print(s[::-1])  # 倒序输出
print(s[5:0:-1])
print(s[-1:-6:-1])

print('#', s[0:5:-1])  # 不会有输出的