# 变量名存放的是一个引用
name = 'maliya'
NUM = 100
print(name)
print(id(name), type(name), name, type(NUM))

# 多次赋值之后变量会指向新的地址

name = '玛丽亚'
old_name = name
print(name, id(name))
name = '希纳'
print(old_name, id(old_name), name, id(name))

# 整形
print("二进制", 0b1011001)
print("八进制", 0o77564)
print("十六进制", 0x48ADD12)

# 浮点型
a = 3.1415926
print(a, type(a))
a = 1.1
b = 2.2
print(a + b)  # 结果可能不精确

from decimal import Decimal  # 应该放在文件最开始

print(Decimal('1.1') + Decimal('2.2'))  # 注意这里传入的是字符串

# 布尔类型
a = True
print(a)
print(a + 1)  # 可以转成整数运算

# 字符串类型

str1 = '人生苦短，我学python'
str2 = "人生苦短，我学python"
str3 = """人生苦短，
我学python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
