from urllib.parse import quote
import requests
import re
from lxml import etree

class BaiduBaike:
    def __init__(self,global_name,
                 url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd={}',
                 text='''<a href="(.*?)" target="_blank"><em>%s</em>_百度百科</a>''',
                 path='//div[@class="result-op c-container xpath-log"]/h3[@class="t c-gap-bottom-small"]/a/@href'):
        self.name=global_name
        self.key=quote(str(self.name))
        self.url=url.format(self.key)
        self.homepage_html=Html(self.url)
        self.homepage_html=self.homepage_html.get_html()
        self.text=text
        self.path=path
        
    def BaiduBaike(self):
        html=self.get_BaikeHtml()
        if html:
            text=Text()
            text=text.get_text(html)
            try:
                return('\n'+'百度百科：'+'\n'+'======================='+'\n'+text+'\n'+'======================='+'\n')
            except TypeError:
                return('\n'+'没有关于该词条的详细信息'+'\n')
        else:
            return ''

    def get_BaikeHtml(self):
        if '_百度百科'in self.homepage_html:
            try:
                url=Url()
                url=url.get_sth_re(self.text,self.homepage_html,self.name)
            except:
                url=Url()
                url=url.get_sth_lxml(self.homepage_html,self.path)
        else:
            url=''
        num=int(len(url))
        if num:
            if num > 1:
                try:#c++情况
                    for i in range(num):
                        html=Html(url[i][0])
                        html=html.get_html()
                        titles=Title()
                        titles=titles.get_title(html)
                        for each_title in titles:
                            if '_百度百科' in each_title:
                                choose_url=Url()
                                choose_url=choose_url.url_choice(html=html,selected_url=url[i][0])
                                break
                            else:
                                pass
                except:#你 情况
                    html=Html(url=url[0])
                    html=html.get_html()
                    choose_url=Url()
                    choose_url=choose_url.url_choice(html=html,selected_url=url[0])
            else:
                html=Html(url=url[0])
                html=html.get_html()
                choose_url=Url()
                choose_url=choose_url.url_choice(html=html,selected_url=url[0])
            html=Html(url=choose_url)
            html=html.get_html()
            return html
        else:
            try:
                str_list,title_list,url_list=[],[],[]
                path_list=['//span[@class="c-tools"]/@data-tools','//div[@class="c-tools"]/@data-tools']
                url_obj=Url()
                for i in path_list:
                    for j in url_obj.get_sth_lxml(self.homepage_html,i):
                        str_list.append(j)
                for i in str_list:
                    try:
                        i=i.replace('{','')
                        i=i.replace('}','')
                        i=i.replace('"','')
                        i=i.split(',')
                        title=i[0]
                        url=i[1]
                        if '_百度百科' in title:
                            title_list.append(title.split(':')[1].replace("'",'').split('_')[0])
                            url_list.append(url.split(':')[2].replace("'",''))
                        else:
                            pass
                    except:
                        pass
                num=len(title_list)
                print('你要找的是不是：')
                for i in range(num):
                    print(i+1,'.',title_list[i])
                while True:
                    choice=input('请输入所需关键字的序号，没有输入q退出：')
                    if choice=='q':
                        return ''
                    else:
                        try:
                            if int(choice)>0 and int(choice)<=num:
                                url=url_list[int(choice)-1]
                                break
                            else:
                                print('输入正确的数字范围！')
                        except ValueError:
                            print('请输入正确的数字字符！')
                html=Html(url='http:'+url)
                html=html.get_html()
                return html
                    
            except:
                print('\n'+'没有关于该关键字的百度百科'+'\n')
                return ''
        return html

class Title:
    def get_title(self,html,string='''<title>(.*?)</title>'''):
        title=re.findall(self.string,html)
        return title

class Html:
    def __init__(self,url):
        self.url=url
        self.headers=headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
                
    def get_html(self):
        try:
            html=requests.get(self.url,headers=self.headers).content.decode('utf-8')
        except:
            html=requests.get(self.url,headers=self.headers).content.decode('gbk','ignore')
        return html

class Url:
    def get_sth_re(self,text,html,name=None):
        try:
            find=text % name
        except:
            find=text
        url=re.findall(find,html)
        if len(url)==0:
            find=text % name.title()
            url=re.findall(find,html)
            if len(url)==0:
                find=text % name.upper()
                url=re.findall(find,html)
                if len(url)==0:
                    find=text % name.lower()
                    url=re.findall(find,html)
        return url

    def get_sth_lxml(self,html,path):
        url=[]
        soup=etree.HTML(html)
        items=soup.xpath(path)
        for item in items:
            url.append(item)
        return url

    def url_choice(self,html,selected_url,
                   mark_to_judge='polysemantList-wrapper cmn-clearfix',
                   mark_selected='<li class="item">▪<span class="selected">(.*?)</span></li>',
                   path_title='//ul[@class="polysemantList-wrapper cmn-clearfix"]/li[@class="item"]/a/@title',
                   path_choice='//ul[@class="polysemantList-wrapper cmn-clearfix"]/li[@class="item"]/a/@href',
                   url_to_replace='http://www.baidu.com',
                   url_to_add='http://baike.baidu.com'):
        if mark_to_judge in html:
            soup=etree.HTML(html)
            choice_list,url_list=[],[]
            if mark_selected:
                selected_choice=Url()
                selected_choice=selected_choice.get_sth_re(mark_selected,html)
            else:
                selected_choice=''
            title_items=soup.xpath(path_title)

            choice_url=soup.xpath(path_choice)
            selected_url=selected_url.replace(url_to_replace,'')
            
            for item in title_items:
                choice_list.append(item)
            choice_list.insert(0,selected_choice[0])

            num=len(choice_list)
            
            for item in choice_url:
                url_list.append(item)
            url_list.insert(0,selected_url)
            
            print('共有%d个选项，请选择所需查询的编号，按回车确认：' % num)
            for i in range(0,num):
                print(i+1,'.',choice_list[i])
            while True:
                try:
                    choice=int(input('请填写所需选项的序号，按回车键结束：'))
                    if choice<=num and choice>=1:
                        choose_url=url_list[choice-1]
                        break
                    else:
                        print('请输入正确范围！')
                except ValueError:
                    print('请输入正确数字符号！')
            return url_to_add+choose_url
        else:
            return selected_url

class Text:
    def get_text(self,html):
        html_to_find=html
        try:
            text=self.get_fixedtext(html_to_find,"promotion-declaration","configModuleBanner")
            if text:
                return text
            else:
                text=self.get_fixedtext(html_to_find,"lemmaWgt-lemmaTitle-subTitle","configModuleBanner")
                if text:
                    return text
                else:
                    text=self.get_fixedtext(html_to_find,"lemmaWgt-lemmaSummary lemmaWgt-lemmaSummary-light","lemmaWgt-lemmaSummary-more")
                    if text:
                        return text
                    else:
                        text=self.get_fixedtext(html_to_find,'lemmaSummary"',"configModuleBanner").replace('lemmaSummary">','')
                        if text:
                            return text
                        else:
                            text=self.get_fixedtext(html_to_find,'lemmaWgt-lemmaSummary lemmaWgt-lemmaSummary-dark"',"lemmaWgt-lemmaSummary-more").replace('lemmaWgt-lemmaSummary lemmaWgt-lemmaSummary-dark">','')
                            if text:
                                return text
        except:
            return ''

    def get_fixedtext(self,html_to_find,start_str,end_str):
        tabs=['div','a','b','sup','h3','dd','ul','li','dl','i','img']
        tabs_content=['<div(.*?)>','<a(.*?)>','<dd(.*?)>','<img(.*?)>']
        start=html_to_find.find(start_str)
        end=html_to_find.find(end_str)
        text=html_to_find[start:end]
        text=text.replace(start_str+'">','')

        for each in tabs_content:
            content=re.findall(each,text)
            for i in content:
                text=text.replace(i,'')

        for each in tabs:
            text=text.replace('<'+each+'>','')
            text=text.replace('</'+each+'>','')

        try:
            text=text.replace('&nbsp','').replace('<div class="','').strip()
        except:
            text=text.replace('&nbsp','').replace('<a class="','').strip()
        return text

if __name__== '__main__':
    function_list=['百度百科']
    while True:
        for i in range(len(function_list)):
            print(i+1,'.',function_list[i])
        function=input('请选择功能（按q退出）:')
        print('\n')
        if function=='q':
            break
        elif function=='1':
            while True:
                global_name=input('搜索关键字（输入“离开当前页面”退出本次搜索）:')
                if global_name=='离开当前页面':
                    break
                else:
                    baidubaike=BaiduBaike(global_name).BaiduBaike()
                    print(baidubaike)
