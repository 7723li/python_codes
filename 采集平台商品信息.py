#socket设置超时，class类，bs4以及正则，反爬机制
import urllib.request as ur
import re
import time
import socket
from bs4 import BeautifulSoup

fanli_url=r'http://zhide.fanli.com/p'
format_url=r'http://zhide.fanli.com/detail/'

class Fanli:
    def __init__(self):
        self.User_Agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        self.html_data=[]#放置商品信息的列表

    def get_html(self,start_page=1,end_page=3):
        for i in range(start_page,end_page + 1):
            self.req = ur.Request(fanli_url + str(i))
            self.req.add_header('User-Agent',self.User_Agent)
            
            self.html=url.urlopen(req).read().decode('utf-8')
            self.html_data.append(self.html)
            time.sleep(2)
            socket.setdefaulttimeout(15)#控制下载内容的时间

            #if hasattr(e,'reason')
        return(self.html_data)

#获取商品链接
class GetData():
    def __init__(self):
        html=Fanli().get_html()
        self.href=[]
        self.ls=[]
        self.url=[]

    def get_hreturl(self):
        reg=r'data-id="\d{6}"'
        result=re.compile(reg)
        tag=result.findall(self.html)
        for i in tag:
            self.href.append(i)
            print(self.href)

        reg2=r"\d{6}"
        result2=re.findall(reg2,str(self.href))
        if len(result2):
            for data in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url=format_url+str(data)
                    self.append(url)
                    print()

a=GetData().get_hreturl()
