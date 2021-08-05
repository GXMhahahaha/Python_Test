scores = {'张三': 100, '李四': 90, '王五': 70}
print(scores['李四'])
print(scores.get('李四'))

# print(scores['sb'])  会报错
print(scores.get('sb'))  # 输出None

print(scores.get('sb', 99))  # 查找不存在时的默认值为 99
