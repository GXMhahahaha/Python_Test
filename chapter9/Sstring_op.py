sstr = 'Wow you can really you dance'
print(sstr.find('you'))  # 第一个
print(sstr.rfind('you'))  # 最后一个
print(sstr.find('Python'))  # 返回-1

print(sstr.index('you'))
print(sstr.rindex('you'))
# print(sstr.index('Python'))  # 报错

print(sstr.upper())
print(sstr.lower())
print(sstr.swapcase())
print(sstr.capitalize())  # 第一个字符大写
print(sstr.title())  # 所有单词第一个字符大写
print(sstr)
