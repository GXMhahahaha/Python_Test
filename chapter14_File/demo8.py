file = open('a.txt', mode='a+', encoding='UTF-8')
file.write('牛逼')
file.seek(0)
print(file.read())