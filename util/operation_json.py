#LJ
import json

class OperationJson:
    '''
    该类用于操作json文件，获取该文件中的数据
    '''

    #通过构造函数将获取文件这一步重构，实例化时直接可以打开文件
    def __init__(self):
        self.file = self.read_file()


    #通过句柄找到文件，由于需要文件读取完成后自动关闭，因此用with来加载
    def read_file(self):
        with open('../dataconfig/interface_json.json') as fp:
            file = json.load(fp)
        return file

    #通过关键字key来获取value
    def get_value(self,key):
        value = self.file[key]
        return value

if __name__ == '__main__':
    opers = OperationJson()
    print(opers.get_value('xiaoming2'))