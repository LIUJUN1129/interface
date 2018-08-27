#LJ
from base.runmethod import RunMethod
from data.getdata import GetData


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    #程序执行的入口
    def go_on_run(self):
        self.data.get_case_lines()