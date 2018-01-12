import requests
import getpass
from HTMLParser import HTMLParser
import PIL.Image

class DoubanClient:
    def __init__(self):
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        self.session=requests.session()#浏览器本地缓存，参考sessionStorage

    def login(self,username,password,source='index_nav',redir='https://www.douban.com/',login='登录'):
        self.login_url='http://accounts.douban.com/login'
        self.response=self.session.get(self.login_url)

        captcha_id,captcha_url=_get_capture(response.content)#验证码id，验证码图片链接
        if captcha_id:
            r=self.session.get(captcha_url)
            with open(r'C:\Users\Administrator\Desktop\验证码.jpg','wb') as file:
                file.write(r.content)
                try:
                    im=Image.open('验证码.jpg')
                    im.show()
                    im.close()
                except:
                    print('请输入验证码')

            captcha_solution=input('输入验证码:')
        
        self.data={'from_email':username,
                   'form_password':password,
                   'source':source,
                   'redir':redir,
                   'login':login}

        if captcha_id:
            self.data['captcha-id']=captcha_id
            self.data['captcha-solution']=captcha_solution
        
        self.session.post(self.login_url,data=self.data,headers=self.headers)#发送登录请求
        print(self.session.get(redir).content.decode('gbk','ignore'))#已登录成功状态

    def _attr(attrs,attrname):
        for attr in attrs:
            if attr[0]==attrname:
                return attr[1]
        return None

    def _get_capture(content):
        
        class CaptchaParse(HTMLParser):#解析网页的类
            def __init__(self):
                HTMLParser.__init__(self)
                self.captcha_id=None
                self.captcha_url=None

            def handle_starttag(self,tag,attrs):
                if tag=='img' and _attr(attrs,'id')=='captcha_image' and _attr(attrs,'class')=='captcha_image':
                    self.capture_url=_attr(attrs,'src')
                if tag=='input' and _attr(attrs,'type')=='hidden' and _attr(attrs,'name'):
                    self.captcha_id=_attr(attrs,'value')
        p=CaptchaParse()
        p.feed(content)
        return p.captcha_id,p.captcha_url

if __name__ =="__main__":
    username=input('name:')
    password=getpass.getpass('password:')
    D=DoubanClient()
    D.login(username,password)
    
