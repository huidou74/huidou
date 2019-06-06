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
print ('django connet to mysql OK')


