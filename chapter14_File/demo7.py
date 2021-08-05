file = open('a.txt', mode='r', encoding='UTF-8')  # 默认编码方式是由操作系统决定的

print(file.read(2))  # 指针停留在上次读取的位置
print(file.readline())
print(file.readlines())  # 以列表的形式
file.close()


file2 = open('a.txt', mode='a+', encoding='UTF-8')
file2.write('Hello')
file2.seek(0)  # offset 相对于whence的偏移  whence的默认为文件头
print(file2.read())

file2.writelines(['牛逼', 'Java', 'Go', 'Python'])  # 做完写的操作，指针会跟着一起移动
file2.seek(0)
print(file2.read())

file3 = open('a.txt', mode='w')
file3.write('')
file3.close()
