s = 'hello,python'
print('1.', s.isidentifier())  # 判断是否是标识符

print('2.', s.isspace())
print('3', 'abc'.isalpha())
print('4', '张三'.isalpha())
print('5', '张三1'.isalpha())

print('6', '123'.isdecimal())
print('7', '0b1001'.isdecimal())  # 不是十进制
print('8', '1001'.isdecimal())
print('9', '123FA'.isdecimal())

print('10', '123'.isnumeric())

print('11', '123四'.isnumeric())  # 汉字认识，罗马数字也认识

print('12', '12312gadfs213'.isalnum())  # 全部由字母和数字组成
print('13', 'fasdf!32'.isalnum())