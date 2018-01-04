import urllib.robotparser  
rp = urllib.robotparser.RobotFileParser()  
rp.set_url("http://www.xinfadi.com.cn/robots.txt")  
rp.read()  
url = "http://www.xinfadi.com.cn/"  
user_agent = "*"  
print(rp.can_fetch(user_agent,url))  
