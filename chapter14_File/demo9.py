file = open('a.txt', mode='a+', encoding='UTF-8')  # UTF-8是三个字节的
file.seek(3)
print(file.read())
print(file.tell())  # 3*7 = 24
file.close()

# 英文是一个字节

file2 = open('b.txt', mode='a+')
print(file2.read())
print(file2.tell())
file2.close()

file3 = open('b.txt', mode='a+')
file3.write('sdfasdfgasdg')
file3.flush()
file3.write('\nfdsdfasdf')
file3.close()