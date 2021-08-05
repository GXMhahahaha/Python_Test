s = 'hello world python'
lst1 = s.split('o')  # 分割的结果返回list类型
print(lst1)

lst2 = s.split()  # 默认以空格作为分割
print(lst2)

s2 = 'surprise|mother|fucker'
lst3 = s2.split(sep='|', maxsplit=1)  # 可以省略sep  最大分割几次
print(lst3)

lst4 = s2.rsplit('|', maxsplit=1)  # 从右侧开始分割
print(lst4)


