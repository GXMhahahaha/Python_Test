grade = float(input("请输入成绩"))
if 90 < grade < 100:
    print("优秀")
elif 80 < grade < 90:
    print("良好")
elif 70 < grade < 80:
    print("一般")
elif 60 < grade < 70:
    print("及格")
else:
    print("不及格")