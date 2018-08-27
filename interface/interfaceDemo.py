#LJ
import json
import requests

class RunMain():
    '''
    RunMain类是为了get和post请求，
    初始化实例之后通过run_main来判断请求类型
    '''

    #实例化后直接调用run_main()
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)


    #get请求
    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)


    #post请求
    def send_post(self,url,data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    url= 'http://127.0.0.1:8000/web/login/'
    data = {
        'username': 'lj',
        'password': '123456'
    }
    run = RunMain(url,'GET',data)
    print(run.res)