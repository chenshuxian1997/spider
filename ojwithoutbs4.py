#代码规范优化
import urllib.request 
import urllib.error
import re
#教师通知http://jxb.ojc.zj.cn/Col/Col1400/Index.aspx
url_a="http://jxb.ojc.zj.cn/Col/Col1400/Index.aspx"
request_a=urllib.request.Request(url_a)
response_a= urllib.request.urlopen(request_a)
a= response_a.read().decode()
match_a=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',a)

print("\n教师通知")
for i in match_a:
    print(i[1])
print("\n-----------------------------------------------------------------------------------------------------------------")
#在线通知http://jxb.ojc.zj.cn/Col/Col1376/Index.aspx
url_b="http://jxb.ojc.zj.cn/Col/Col1376/Index.aspx"
request_b=urllib.request.Request(url_b)
response_b= urllib.request.urlopen(request_b)
b= response_b.read().decode()
match_b=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',b)

print("\n在线通知")
for j in match_b:
    print(j[1])
print("\n-----------------------------------------------------------------------------------------------------------------")

#学生通知http://jxb.ojc.zj.cn/Col/Col1401/Index.aspx
url_c="http://jxb.ojc.zj.cn/Col/Col1401/Index.aspx"
request_c=urllib.request.Request(url_c)
response_c= urllib.request.urlopen(request_c)
c= response_c.read().decode()
match_c=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',c)

print("\n学生通知")
for k in match_c:
    print(k[1])
print("\n-----------------------------------------------------------------------------------------------------------------")


#公示公告http://jxb.ojc.zj.cn/Col/Col1374/Index.aspx
url_d="http://jxb.ojc.zj.cn/Col/Col1374/Index.aspx"
request_d=urllib.request.Request(url_d)
response_d= urllib.request.urlopen(request_d)
d= response_d.read().decode()
match_d=re.findall(r'<li><a href=(.*?)>(.*?)</a><span>',d)

print("\n公示公告")
for l in match_d:
    print(l[1])
print("\n-----------------------------------------------------------------------------------------------------------------")


