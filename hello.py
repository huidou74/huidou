#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
# print ('HELLO !')
# print ('test to webhook!')
# print ('test to webhook!')
# print ('test 7')
import requests  # 发送请求，然后获取相应内容
r = requests.get('https://api.github.com/repos/Codertocat/Hello-World/tags').json()
print (r,type(r))  # list