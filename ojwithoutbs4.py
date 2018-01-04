import urllib.request 
import urllib.error
import re
url = "http://jxb.ojc.zj.cn/Col/Col58/Index.aspx"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
read= response.read().decode()
matc=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',read)
url = "http://jxb.ojc.zj.cn/Col/Col57/Index.aspx"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
li= response.read().decode()
match=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',li)
url = "http://jxb.ojc.zj.cn/Col/Col55/Index.aspx"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
lii= response.read().decode()
mat=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',lii)
url= "http://jxb.ojc.zj.cn/Col/Col53/Index.aspx"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
lit= response.read().decode()
ma=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',lit)  
print("在线通知")
for h in matc:
    print(h[1])
print("\n-----------------------------------------------------------------------------------------------------------------")
print("学生通知")
for i in match:
    print(i[1])
print("\n-----------------------------------------------------------------------------------------------------------------")
print("\n教师通知")
for k in mat:
    print(k[1])
print("\n-----------------------------------------------------------------------------------------------------------------")
print("\n公告")
for j in ma:
    print(j[1])
print("\n-----------------------------------------------------------------------------------------------------------------")

    
