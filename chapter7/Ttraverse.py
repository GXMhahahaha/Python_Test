scores = {'张三': 100, '李四': 90, '王五': 70}

for item in scores:  # 遍历的是键
    print(item, scores[item], sep='->')
print()
for item in scores:
    print(item, scores.get(item), sep='->')