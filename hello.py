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
print('0610 -  测试 webhook 的验证功能 10  request.POST.get(\'payload\') ')
print('0610 -  测试 webhook 的验证功能 11 hashlib.sha1')
print('0610 -  测试 webhook 的验证功能 12 hashlib.sha1 ')
print('0610 -  测试 webhook 的验证功能 13 request.POST ')
print('0610 -  测试 webhook 的验证功能 14 request.data ')
print('0610 -  测试 webhook 的验证功能 15 request.POST.get() ')
print('0610 -  测试 webhook 的验证功能 16 bytes(request.POST.get(\'payload\')) ')
print('0610 -  测试 webhook 的验证功能 17 pickle.dumps(request.POST.get(\'payload\')) ')
print('0610 -  测试 webhook 的验证功能 18 request.body ')
print('0610 -  测试 webhook 的验证功能 19 APP_KEY ')
print('0610 -  测试 webhook 的验证功能 20 request object all to test')
print('0610 -  测试 webhook 的验证功能 21 payload = request.body')