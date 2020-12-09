# cookiesTest
# 2020/12/3
# cookie:是服务器给客户端的，返回在响应头

# 登录接口--基于cookis机制
import requests
def login():
    # url
    url='http://120.55.190.222:7080/api/mgr/loginReq'
    # 请求体
    payload={'username':'auto','password':'sdfsdfsdf'}
    # 请求
    resp=requests.post(url,data=payload)
    # 获取cookie,直接从响应中获取
    print(resp.cookies)
    return resp.json()
if __name__ == '__main__':
    print(login())