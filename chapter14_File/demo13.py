# OS模块使用操作系统的函数

import os
# import os.path
# os.system('notepad.exe')
# os.startfile('D:\\Softwares\\QQ\\Bin\\QQScLauncher.exe')

print(os.getcwd())
print(os.listdir('../chapter10_function'))
# os.mkdir('newdir2')
# os.makedirs('A/B/C')  # 创建多级目录

# os.rmdir('newdir2')
# os.removedirs('A\B\C')

# os.chdir('C:\\Program Files')
# print(os.getcwd())

print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'), os.path.exists('demo'))
print(os.path.split('demo13.py'))  # 将文件路径和文件名字拆分
print(os.path.splitext('demo13.py'))

# print(os.path.basename(''))
print(os.path.isdir('D:\\Softwares\\QQ\\Bin\\QQScLauncher.exe'))