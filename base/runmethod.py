#LJ
import json

import requests

class RunMethod:

    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,header=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,header,data=None):
        res = None
        if header != None:
            res = requests.get(url=url,header=header,data=data)
        else:
            res = requests.get(url=url,header=header,data=data)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False)