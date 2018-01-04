import urllib.request 
import urllib.error
import urllib.robotparser 
import re
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
li= response.read().decode()
match=re.findall(r'<tr(.*?)>(.*?)</tr>(.*?)<td(.*?)>(.*?)</td>',li)
print("种类    最低    平均    最高    品质    单位    时间")
for i in match:
    #print(i[1])
    a=i[1].replace("</td><td>","    ")
    b=a.replace('<td style="text-align:left;padding-left:5px;">',"")
    c=b.replace('</td>',"")  
    print(c)
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
li= response.read().decode()
match=re.findall(r'<tr>(.*?)</tr>(.*?)<td(.*?)>(.*?)</td>',li)
print("种类    最低    平均    最高    品质    单位    时间")
for i in match:
    #print(i[0]) 
    a=i[0].replace("</td><td>","    ")
    b=a.replace('<td style="text-align:left;padding-left:5px;">',"")
    c=b.replace('</td>',"")  
    print(c)
