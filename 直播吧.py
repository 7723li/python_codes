import requests
import lxml
import threading
import time
import re

def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    html=requests.get(url,headers=headers).content.decode('utf-8')
    return html

def get_text_before(html):
    start_num=html.find('"live_text":"')
    end_num=html.find('","live_pid"')
    text=html[start_num:end_num].replace('"live_text":"','')
    #print(type(text))
    #print(text)
    #text1=text.encode('utf-8')
    return text.encode('utf-8').decode('unicode_escape')


def get_text_after(html):
    html=html.replace(html[0:html.find('}')],'')
    #re.compile(html)
    start_num=html.find('"live_text":"')
    end_num=html.find('","live_pid"')
    text=html[start_num:end_num].replace('"live_text":"','')
    #print(type(text))
    #print(text)
    #text1=text.encode('utf-8')
    return text.encode('utf-8').decode('unicode_escape')

def get_text(page):
    text=''
    url='http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/92450/0/lit_page_2/%d.htm' % page
    html=get_html(url)
    text+=get_text_before(html)
    '''
    if text:
        print(page,text)
    '''
    text+=get_text_after(get_html(url))
    '''
    if text:
        print(page,text)
    '''
    return text

def get_page():
    with open('page.txt','r') as f:
        return int(f.read())

def save_page(page):
    with open('page.txt','w') as f:
        f.write(str(page))
'''
def restart():
    page=get_page()
    print(page)
    main(page)
'''
def main(page):
    a=0
    while True:
        #print(a)
        text=get_text(page)
        page+=1
        if text:
            print(page,text)
            
        else:
            time.sleep(0.05)
            '''
            save_page(page)
            time.sleep(0.05)
            restart()
            '''
if __name__ == '__main__':
    page=input('请输入开始的页数：')
    save_page(page)
    page=get_page()
    #print(page)
    main(page)
