import os

os.chdir('../')
path = os.getcwd()
print(path)
lst_files = os.walk(path)
print(lst_files)
# print(lst_files[0])

for dirpath, dirname, filename in lst_files:
    # print('----------------------')
    # print(dirpath)
    # print('----------------------')
    # print(dirname)
    # print('----------------------')
    # print(filename)

    for dir in dirname:
        print(os.path.join(dirpath, dir))  # join(path,name)

    for file in filename:
        print(os.path.join(dirpath, file))
