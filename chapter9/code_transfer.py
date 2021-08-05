s = '天涯共此时'
temp = s.encode(encoding='GBK')
print(s.encode(encoding='GBK'))  # 一个汉字占两个字节
print(s.encode(encoding='UTF-8'))  # 一个汉字占三个字节

print(temp.decode(encoding='GBK'))