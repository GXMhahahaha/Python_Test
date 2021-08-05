# python中的字典就是c++中的map
scores = {'张三': 100, '李四': 90, '王五': 70}  # 无序数据结构, 存储之前先使用了hash, 键是不可变序列
print(scores, type(scores))

ss = dict(name='jack', grade='100')
print(ss)
