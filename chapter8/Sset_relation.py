s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50}
s3 = {20, 40, 30, 10}
print(s1 == s2)
print(s1 == s3)  # 无序

s4 = {10, 20}
print(s4.issubset(s1))  # s4是s1的子集

print(s1.issuperset(s4))  # s1是s4的超集
print(s1.issuperset(s2))

print(s1.issuperset(s3))  # 相同集合既是超集又是子集
print(s1.issubset(s3))

print(s1.isdisjoint(s2))  # 说明二者有交集
s5 = {90, 100}
print(s1.isdisjoint(s5))

