scores = {'张三': 100, '李四': 90, '王五': 70}
print('张三' in scores)  # 判断键是否在字典当中

del scores['张三']  # 删除指定键指对
print(scores)

scores.clear()  # 清空
print(scores)

scores['陈六'] = 98
print(scores)

a = {}
a['shabi'] = 100
print(a)
