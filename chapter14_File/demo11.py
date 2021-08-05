class MycontextMgr(object):
    def __enter__(self):
        print('enter方法')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法')

    def show(self):
        print('show方法')


with MycontextMgr() as file:
    file.show()

