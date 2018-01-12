import urllib.request as ur
import ssl
import json
ssl._create_default_https_context=ssl._create_unverified_context
'''
ajax异步加载
源代码里面没有找到页面源码，两种可能性，js加密和ajax异步加载
'''

def get_list():
    url=r'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-10&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
    req=ur.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    response=ur.urlopen(req)
    html=response.read().decode('utf-8')
    #print(html)
    #print('=================================')
    dict1=json.loads(html)
    #return html
    #print(dict1)
    return dict1['data']['result']

print(get_list())
#def get
