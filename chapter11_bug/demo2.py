lst = [{'rating': [9, 7, 50], id: [1292052], 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆.罗宾斯', '摩根.弗里曼']},
       {'rating': [9, 6, 50], id: [1291546], 'type': ['爱情', '剧情', '同性'], 'title': '霸王别姬', 'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
       {'rating': [9, 6, 50], id: [1296141], 'type': ['犯罪', '剧情', '嫌疑'], 'title': '控方证人', 'actors': ['泰隆.鲍华', '玛琳.黛德丽']}]

actor = input("请输入姓名")
for item in lst:
    if actor in item['actors']:
        print(actor + "参演了" + item['title'])
        break
else:
    print("没有参演")
