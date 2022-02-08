import requests

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
# 代理请求
# Response = requests.get('https://www.baidu.com/s',proxies=proxies)
# print(Response.text)

urlpara = {
    'wd':'iphone&ipad',
    'rsv_spt':'1'
}
# 参数请求
# Response = requests.get('https://www.baidu.com/s',params=urlpara)
# print(Response.text)

headers={
"user-agent":"my-app/0.0.1",
"auth-type":"jwt-token"
}
# 携带请求头请求   post请求
# r = requests.post("http://httpbin.org/post", headers=headers)
# print(r.text)


# XML 格式消息体请求
payload = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''

# r = requests.post("http://httpbin.org/post",
#                   data=payload.encode('utf8'))
# print(r.text)


# urlencoded 格式消息体
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)


# json 格式消息体 请求
import requests,json
payload = {
    "Overall":"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        },
    ]
}
# r = requests.post("http://httpbin.org/post", data=json.dumps(payload))
# r=requests.post("http://httpbin.org/post",json=payload)
# status_code  获取请求状态码  .text获取请求响应     .headers,获取HTTP响应的消息头
# 有时候，服务端并不一定会在消息头中指定编码格式，这时， requests的推测可能有误，需要我们指定编码格式。
# r.encoding='utf8'
# print(r.text,r.status_code)
# response.headers 对象的类型 是 继承自 Dict 字典 类型的一个 类。
# print(r.headers['Content-Type'])
# 如果我们要直接获取消息体中的字节串内容，可以使用 content 属性，
# print(r.content)
# 可以直接对 获取的字节串 bytes对象进行解码
# print(r.content.decode('utf8'))  json.loads 函数把json格式字符串转换成数据对象
# print(r.content.decode('utf8'))
# print("---------")
# obj = json.loads(r.content.decode('utf8'))
# print(obj)

# requests库为我们提供了更方便的方法，可以使用 Response对象的 json方法，
response = requests.post("http://httpbin.org/post", data={1:1,2:2})
obj = response.json()
print(obj)



# respen=requests.post('http://mirrors.sohu.com/')