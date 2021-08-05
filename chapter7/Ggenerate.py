items = ['Fruits', 'Books', 'Breads']
prices = [98, 100, 89]
zz = zip(items, prices)  # zip只能使用一次
# print(zz, type(zz))
# print(list(zz))  # 二元组list
# print(list(zz))
# zz = list(zz)
# print(zz, type(zz))
dic = {item.upper(): price for item, price in zz}
print(dic)

items = ['Fruits', 'Books', 'Breads']
prices = [98, 100]  # 如果长度不匹配，以短的为准
zz = zip(items, prices)
dic = {item.upper(): price for item, price in zz}
print(dic)
