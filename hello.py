#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
print ('HELLO !')
print ('test to webhook!')
print ('test tag and requests messages')
print ('test tag and requests messages')
import requests  # 发送请求，然后获取相应内容
url= 'https://api.github.com/repos/huidou74/huidou/tags'
r = requests.get(url).json()
print (r,type(r))  # list
print ('webhook test OK! ')
print ('django connet to mysql ok! ')
print ('第二次测试 数据解析 ')
print ('OK webhook data to DB')

print ('eval(str(data)) 阿西吧 少个括号 MMP')

print("NameError: name 'true' is not defined,  唉 所以 那里还是需要转换成字符串")

print('0610 -  测试 webhook 的验证功能 3 ')
print('0610 -  测试 webhook 的验证功能 4 hmac ')
print('0610 -  测试 webhook 的验证功能 5 hmac ')
print('0610 -  测试 webhook 的验证功能 6 hmac ')
print('0610 -  测试 webhook 的验证功能 6 payload = pickle.dumps(request.POST) ')
print('0610 -  测试 webhook 的验证功能 7 bytes ')
print('0610 -  测试 webhook 的验证功能 8 string argument without an encoding ')
print('0610 -  测试 webhook 的验证功能 9  hashlib.sha1 ')