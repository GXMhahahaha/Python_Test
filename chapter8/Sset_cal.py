s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 4, 5, 6, 7, 8}

# 交集操作
print(s1.intersection(s2))
print(s1 & s2)  # 普通数字按位与，集合求交集

a = 13
b = 26
print(a & b)

# 并集操作
print(s1.union(s2))
print(s1 | s2)
# print(s1 + s2)  这种操作是错误的

# 差集操作
print(s1.difference(s2))
print(s1 - s2)

# 对称差集  去除两个集合的公共部分
print(s1.symmetric_difference(s2))
print(s1 ^ s2)