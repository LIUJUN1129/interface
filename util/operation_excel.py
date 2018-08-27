#LJ

import xlrd
import xlwt

class OperationExcel():
    #初始化实例，如果未指定文件名和sheet_id，即使用默认数据
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface_excel.xlsx'
            self.sheet_id = 0
        self.book = self.get_data()

    #获取表格内容，需要知道文件名、表格序号
    def get_data(self):
        book = xlrd.open_workbook(self.file_name)
        tables = book.sheet_by_index(self.sheet_id)
        return tables

    #获取单元格行数
    def get_lines(self):
        tables = self.book
        return tables.nrows

    #获取某单元格具体数据
    def get_content(self,cols,rows):
        tables = self.book
        return tables.cell(cols,rows).value

if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers.get_content(1,6))
