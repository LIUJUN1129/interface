#LJ
import xlrd

class Operation_excel1:
    '''
    该类封装了对excel的常规操作

    '''

    def __init__(self,file_name = None,sheet_id = None):
        #该构造函数对file_name和sheet_id做判断，如果指定了参数即成为全局变量
        #如果不指定参数即使用指定的文件和sheet_id作为全局变量
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface_excel.xlsx'
            self.sheet_id = 0
        #调用get_data()方法获取具体表table
        self.table = self.get_data()

    # 获取指定文件中的指定表数据
    def get_data(self):
        # 将指定表赋值给book
        book = xlrd.open_workbook(self.file_name)
        # 对book文件的sheet_id做指定
        table = book.sheet_by_index(self.sheet_id)
        return table


    # 获取指定文件中的行数
    def get_lines(self):
        table = self.table
        return table.nrows

if __name__ == '__main__':
    opers = Operation_excel1()
    print(opers.get_lines())