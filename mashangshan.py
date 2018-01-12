'''
def word():
    chance=3
    while chance>0:
        password=str(input('请输入你的六位密码：'))
        if '*' in password:
            continue
        elif not (password.isdigit()):
            print('请输入数字密码！')
            continue
        elif(len(password)!=len(default) or password!=default):
            chance-=1
            print('密码错误')
            print('剩余',str(chance),'次机会')
        else:
            print('Welcome!')
            break
    if(chance==0):
        print('已没有剩余机会')
default = '123456'
word()

def sxh():
    for i in range(100,1000):
        a,b,c=int(i/100),int(i/10%10),int(i%10)
        if((a**3+b**3+c**3)==i):
            print(i,'是水仙花数')

sxh()


print('red\tyellow\tblue')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)


def four():
    import os
    import easygui as g

    def resault_show():
        for i in name:
          print(name[i])  

    def save_name(total,list1,save_path):
        
        for j in pho_number:
            numbers=pho_number[j]
            total+=numbers
        print('共有 %d 张图片' % total)
        list1.append('共有 %d 张图片' % total)
        with open (str(save_path),'w') as tpmc:
            for i in range(len(list1)):
                tpmc.write (str((list1)[i])+'\n')
    
    def pitcher_search(num,start_path):
        os.chdir(start_path)
        for each_file in os.listdir(os.curdir):
            ext=os.path.splitext(each_file)[1]
            if ext in target:
                try:
                    pho_number[ext]+=1
                except KeyError:
                    pho_number[ext]=1

                name[num]=str(os.getcwd())
                num+=1
                name[num]=os.path.splitext(each_file)[0]
                num+=1
            if os.path.isdir(each_file):#判断指定路径是否存在且是一个目录
                pitcher_search(num,each_file)#若指定路径中含有文件夹则递文件夹归该路径，若是文件则不进入此处
                os.chdir(os.pardir)#改变工作目录为上一路径，避免有文件夹遗漏
        
        list1=[]
        total=0
        
        for i in name.values():
            list1.append(i)
            
        if yn==1:
            save_name(total,list1,save_path)

    target=['.jpg','.gif','.png','.JPG','.PNG','.GIF']

    name={}
    pho_number={}

    path=g.diropenbox('请打开搜索路径：')

    yn=g.ynbox(msg='完成后是否保存图片名称',title='YES/NO')
    if yn==1:
        save_path=g.filesavebox(msg='选择保存路径',title='请选择',default='图片名称.txt')
    
    num=0
    pitcher_search(num,path)
    resault_show()

four()
'''
'''
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)
# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
import os
os.chdir('C:\\Users\\Administrator\\Desktop')
list1='abcdefghijklmnopqrstuvwxyz'
list1=list(list1)
list2=[]
num=0
for i in list1:
        for j in list1:
                for k in list1:
                        num+=1
                        list2.append(i+j+k)
with open('图片名称.txt','w') as tpmc:
        tpmc.write(str(list2)+'\n')
print(num)

'''
'''
class Animal():#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
        def __init__(self,kind,food):
                self.kind=kind
                self.food=food
        def run(self):
                print('Animal is running')
        def eat(self):
                print('Animal is eating food')

class Dog(Animal):
        def run(self):
                print('%s is running' % self.kind)
        def eat(self):
                print('%s is eating %s'% (self.kind,self.food))

def runandeat(animal):
        animal.run()
        animal.eat()

a=Dog('dog','meat')
print(runandeat(Animal()))
'''
'''
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
'''
'''
class Ticket(object):
        def __init__(self,weekend=False,child=False):
                self.exp=100
                
                if weekend:
                        self.inc=1.2
                else:
                        self.inc=1
                        
                if child:
                        self.discount=0.5
                else:
                        self.discount=1

        def calPrice(self,num):
                return self.exp * self.inc * self.discount *num

adult=Ticket()
child=Ticket(child=True)
print('两个成人+一个未成年人平日票价为： %.2f' % (adult.calPrice(2)+child.calPrice(1)))
'''
'''
#组合
class Turtle:
    def __init__(self,x):
        self.num=x
    def Double(self):
        return self.num*2

class Fish:
    def __init__(self,x):
        self.num=x
    def Double(self):
        return self.num*2

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)

    def Print(self):
        print('共有 %d 只龟， %d条鱼'% (self.turtle.Double(),self.fish.Double()))

pool=Pool(1,10)
pool.Print()
'''

'''
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Line:
    def __init__(self,p1,p2):
        self.x=p1.getX()-p2.getX()
        self.y=p1.getY()-p2.getY()

    def getLen(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

p1=Point(3,4)
p2=Point(0,0)
line=Line(p1,p2)
print(line.getLen())
'''

'''
class C:
    count=0
    def __init__(self):
        C.count+=1
    def __del__(self):
        C.count-=1
'''

'''
class FileObject:
    def __init__(self,path):
        self.path=path
        self.new_path=open(self.path)

    def save(self):
        self.new_path.close()
        del self.new_path
'''

'''
class TemTurn:
    def __init__(self,temperture):
        self.temperture=temperture

    def turn(self):
        return self.temperture*1.8+32
'''

'''
class C2F(float):
    def __new__(cls,arg=0.0):
        return float.__new__(cls,arg*1.8+32)
'''


'''
class C2F(float):
    def __new__(cls,arg=()):
        return float.__new__(cls,arg*1.8+32)
        
'''

'''
class Nint(int):
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            total=0
            for each in arg:
                total+=ord(each)#odr,ASCII码
            arg=total
        return int.__new__(cls,arg)
'''

'''
class Nstr(str):
    def __sub__(self,other):
        return self.replace(other,'')
 '''

'''
class Nstr(str):
    def __lshift__(self,num):
        return self[num:]+self[:num]
    def __rshift__(self,num):
        return self[:num]+self[num:]

'''
'''
class Nstr(str):
    total=0
    def __add__(self,other):
        
        for i in other:
            total+=ord(i)
        return total
'''

'''
class Nstr(str):
    def __init__(self,string):
        if isinstance(string,str):
            self.total=0
            for i in string:
                self.total+=ord(i)

    def __add__(self,other):
        return (self.total+other.total)
 '''

'''
class Nstr(str):
    def __lshift__(self,other):
        return self[other:]+self[:other]

    def __rshift__(self,other):
        return self[:other]+self[other:]
'''


'''
class MyRev():
    def __init__(self,string):
        self.string=string
        self.index=len(self.string)

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index==0:
            raise StopIteration

        self.index=self.index-1
        return self.string[self.index]
'''

'''
class C:
    def __init__(self,*args):
        if not args:
            print('no')
        else:
            print('传入了%d个参数，分别是：'%len(args),end='')
            for i in args:
                print(i,end=' ')
'''


'''
class Word:
    def __lt__(self,other):
        if len(self)<len(other):
            return True
        else:
            return False
'''


'''
class Nstr(str):
    def __init__(self,string):
        self.string=string
        
    def __sub__(self,other):
        return self.replace(other,'')

    def count(self):
        i=0
        while True:
            if ' ' in self.string:
                i+=1
                self.string=self.string-(self.string[:self.string.index(' ')]+' ')
                    
            else:
                break
'''


'''
import urllib.request as a
b=a.urlopen('http://www.bilibili.com/')
c=b.read()
c=c.decode('utf-8')

'''

'''
import sys
sys.path.append('D:\python安装\自写模块')#由于此保存路径不在默认范围，需要插入后才能使用pytosql模块
import pytosql
a=pytosql.pytosql()
a.use('test')#使用test数据库
a.execute('create table user1 (id int auto_increment not null primary key,name varchar(20),birth varchar(20))')
a.execute('create table user2 (id int auto_increment not null primary key,name varchar(20),birth varchar(20))')
#执行创建列表命令
'''

'''
from tkinter import *

root=Tk()

LANGS=[
    ('python',1),
    ('Perl',2),
    ('Ruby',3),
    ('Lus',4)]

v=IntVar()
v.set(1)#默认为Python

for lang,num in LANGS:
    b=Radiobutton(root,
                  text=lang,
                  variable=v,
                  value=num,
                  indicatoron=False)
    #指示器，指示指令接通，设置为False取消选项前的圆圈，设置为按钮模式
    b.pack(fill='x',
           #anchor='w'
           )
    #fill横纵向居中填充，一般为用在按钮模式

mainloop()
'''




'''
import sys
sys.path.append(r'D:\python安装\自写模块')
import pytosql

from tkinter import *
root=Tk()

def idcheck():
    print('1')

def passcheck():
    print('2')

def Login():
    print('3')

def Register():
    print('4')

root.title('登录界面')


v1=StringVar()
v2=StringVar()

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)

Id=Label(frame1,text='账号')
Pass=Label(frame2,text='密码')
Id.pack(side=LEFT)
Pass.pack(side=LEFT)

Idin=Entry(frame1,textvariable=v1,validate='focusout',validatecommand=idcheck)
Passin=Entry(frame2,textvariable=v2,validate='focusout',validatecommand=passcheck)
Idin.pack(side=LEFT)
Passin.pack(side=LEFT)

b1=Button(frame3,text='确认',command=Login)
b2=Button(frame3,text='注册',command=Register)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)

frame1.pack()
frame2.pack()
frame3.pack()

mainloop()
'''
'''
from tkinter import *
def Register():
    Regiroot=Tk()
    Regiroot.title('请注册')
    
    Id=StringVar()
    Name=StringVar()
    Sex=StringVar()
    Birth=StringVar()
    PhNumber=StringVar()

    frame1=Frame(Regiroot)
    frame2=Frame(Regiroot)
    frame3=Frame(Regiroot)
    frame4=Frame(Regiroot)
    frame5=Frame(Regiroot)

    IdLabel=Label(frame1,text='身份证号码')
    NameLabel=Label(frame2,text='设置密码')
    SexLabel=Label(frame3,text='性别')
    BirthLabel=Label(frame4,text='出生日期')
    PhNumber=Label(frame5,text='手机号码')
    
    IdLabel.pack(side=LEFT)
    NameLabel.pack(side=LEFT)
    SexLabel.pack(side=LEFT)
    BirthLabel.pack(side=LEFT)
    PhNumber.pack(side=LEFT)
    

    #Idin=Entry(frame1,textvariable=Id,validate='key',validatecommand=idcheck)
    
    mainloop()

Register()
'''

'''
import sys
sys.path.append(r'D:\python安装\自写模块')
import pytosql

from tkinter import *

def IdExistCheck():
    print('1')

def Login():

a=pytosql.pytosql()
    a.use('账号密码')
    idnum=b2.get()
    print('3')

def Register():
    def erease_all():
        Idin.delete(0,END)
        Namein.delete(0,END)
        Birthin_year.delete(0,END)
        Birthin_month.delete(0,END)
        Birthin_day.delete(0,END)
        PhNumberin.delete(0,END)

    Regiroot=Tk()
    Regiroot.title('请注册')
    
    Id=StringVar()
    Name=StringVar()
    Sex=IntVar()
    Birth_Y=StringVar()
    Birth_M=StringVar()
    Birth_D=StringVar()
    PhNumber=StringVar()

    frame1=Frame(Regiroot)
    frame2=Frame(Regiroot)
    frame3=Frame(Regiroot)
    frame4=Frame(Regiroot)
    frame5=Frame(Regiroot)
    frame6=Frame(Regiroot)
    
    IdLabel=Label(frame1,text='身份证号码:')
    NameLabel=Label(frame2,text='设置密码:')
    SexLabel=Label(frame3,text='性别:')
    BirthLabel=Label(frame4,text='出生日期:')
    PhNumber=Label(frame5,text='手机号码:')

    IdLabel.pack(side=LEFT)
    NameLabel.pack(side=LEFT)
    SexLabel.pack(side=LEFT)
    BirthLabel.pack(side=LEFT)
    PhNumber.pack(side=LEFT)
    
    Idin=Entry(frame1,textvariable=Id,validate='key')
    Namein=Entry(frame2,textvariable=Name,validate='key')
    Sexin_m=Radiobutton(frame3,text='男',variable=Sex,value=1)
    Sexin_f=Radiobutton(frame3,text='女',variable=Sex,value=2)
    Birthin_year=Entry(frame4,textvariable=Birth_Y,validate='key',width=10)
    Y=Label(frame4,text='年')
    Birthin_month=Entry(frame4,textvariable=Birth_M,validate='key',width=10)
    M=Label(frame4,text='月')
    Birthin_day=Entry(frame4,textvariable=Birth_D,validate='key',width=10)
    D=Label(frame4,text='日')
    PhNumberin=Entry(frame5,textvariable=PhNumber,validate='key')
    
    Idin.pack(side=LEFT)
    Namein.pack(side=LEFT)
    Sexin_m.pack(side=LEFT)
    Sexin_f.pack(side=LEFT)
    Birthin_year.pack(side=LEFT)
    Y.pack(side=LEFT)
    Birthin_month.pack(side=LEFT)
    M.pack(side=LEFT)
    Birthin_day.pack(side=LEFT)
    D.pack(side=LEFT)
    PhNumberin.pack(side=LEFT)

    Regi_confirm=Button(frame6,text='确认注册',
                        command=print('1000')
              #,command= #将数据写入数据库
              )
    Regi_reset=Button(frame6,text='重置',
                      command=print('100'))
    Regi_confirm.pack(side=LEFT,padx=30,pady=10)
    Regi_reset.pack(side=RIGHT,padx=30,pady=10)

    frame1.pack(pady=10)
    frame2.pack(pady=10)
    frame3.pack(pady=10)
    frame4.pack(pady=10)
    frame5.pack(pady=10)
    frame6.pack()
    
    mainloop()

def LoginInterface():
    LoInroot=Tk()
    LoInroot.title('登录界面')

    Id=StringVar()
    Pass=StringVar()

    frame1=Frame(LoInroot)
    frame2=Frame(LoInroot)
    frame3=Frame(LoInroot)

    IdLabel=Label(frame1,text='账号')
    PassLabel=Label(frame2,text='密码')
    IdLabel.pack(side=LEFT)
    PassLabel.pack(side=LEFT,pady=10)

    Idin=Entry(frame1,textvariable=Id,validate='focusout',validatecommand=IdExistCheck)
    #此处检测账号是否存在
    Passin=Entry(frame2,textvariable=Pass)
    #不作操作，只作输入

    Idin.insert(0,'请输入身份证号码..')
    Idin.pack(side=LEFT,pady=10)
    Passin.pack(side=LEFT,pady=10)

    b1=Button(frame3,text='确认登陆',command=Login)#从此处检测密码是否正确
    b2=Button(frame3,text='注册',command=Register)
    b1.pack(side=LEFT,padx=30,pady=10)
    b2.pack(side=RIGHT,padx=30,pady=10)

    frame1.pack()
    frame2.pack()
    frame3.pack()

    mainloop()

if __name__ == '__main__':
    LoginInterface()#登陆界面
'''






'''
import sys
sys.path.append(r'D:\python安装\自写模块')
import pytosql

from tkinter import *

def IdExistCheck():
    print('1')

def Login():
    """a=pytosql.pytosql()
    a.use('账号密码')
    idnum=b2.get()"""
    print('3')

class LoginInterface:    
    def LoginInterface_1(self):
        self.LoInroot=Tk()
        self.LoInroot.title('登录界面')

        self.Id=StringVar()
        self.Pass=StringVar()

        self.frame1=Frame(self.LoInroot)
        self.frame2=Frame(self.LoInroot)
        self.frame3=Frame(self.LoInroot)

        self.IdLabel=Label(self.frame1,text='账号')
        self.PassLabel=Label(self.frame2,text='密码')
        self.IdLabel.pack(side=LEFT)
        self.PassLabel.pack(side=LEFT,pady=10)

        self.Idin=Entry(self.frame1,textvariable=self.Id,validate='focusout',validatecommand=IdExistCheck)
        #此处检测账号是否存在
        self.Passin=Entry(self.frame2,textvariable=self.Pass)
        #不作操作，只作输入

        self.Idin.insert(0,'请输入身份证号码..')
        self.Idin.pack(side=LEFT,pady=10)
        self.Passin.pack(side=LEFT,pady=10)

        self.b1=Button(self.frame3,text='确认登陆',command=Login)#从此处检测密码是否正确
        self.b2=Button(self.frame3,text='注册',command=self.Register_1())
        self.b1.pack(side=LEFT,padx=30,pady=10)
        self.b2.pack(side=RIGHT,padx=30,pady=10)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        mainloop()
        
    def Register_1(self):
        Register().Register()

class Register:
    def Register(self):
        self.Regiroot=Tk()
        def erease_all():
            self.Idin.delete(0,END)
            self.Namein.delete(0,END)
            self.Birthin_year.delete(0,END)
            self.Birthin_month.delete(0,END)
            self.Birthin_day.delete(0,END)
            self.PhNumberin.delete(0,END)
            
        self.Regiroot.title('请注册')
        
        self.Id=StringVar()
        self.Name=StringVar()
        self.Sex=IntVar()
        self.Birth_Y=StringVar()
        self.Birth_M=StringVar()
        self.Birth_D=StringVar()
        self.PhNumber=StringVar()

        self.frame1=Frame(self.Regiroot)
        self.frame2=Frame(self.Regiroot)
        self.frame3=Frame(self.Regiroot)
        self.frame4=Frame(self.Regiroot)
        self.frame5=Frame(self.Regiroot)
        self.frame6=Frame(self.Regiroot)
        
        self.IdLabel=Label(self.frame1,text='身份证号码:')
        self.NameLabel=Label(self.frame2,text='设置密码:')
        self.SexLabel=Label(self.frame3,text='性别:')
        self.BirthLabel=Label(self.frame4,text='出生日期:')
        self.PhNumber=Label(self.frame5,text='手机号码:')

        self.IdLabel.pack(side=LEFT)
        self.NameLabel.pack(side=LEFT)
        self.SexLabel.pack(side=LEFT)
        self.BirthLabel.pack(side=LEFT)
        self.PhNumber.pack(side=LEFT)
        
        self.Idin=Entry(self.frame1,textvariable=self.Id,validate='key')
        self.Namein=Entry(self.frame2,textvariable=self.Name,validate='key')
        self.Sexin_m=Radiobutton(self.frame3,text='男',variable=self.Sex,value=1)
        self.Sexin_f=Radiobutton(self.frame3,text='女',variable=self.Sex,value=2)
        self.Birthin_year=Entry(self.frame4,textvariable=self.Birth_Y,validate='key',width=10)
        self.Y=Label(self.frame4,text='年')
        self.Birthin_month=Entry(self.frame4,textvariable=self.Birth_M,validate='key',width=10)
        self.M=Label(self.frame4,text='月')
        self.Birthin_day=Entry(self.frame4,textvariable=self.Birth_D,validate='key',width=10)
        self.D=Label(self.frame4,text='日')
        self.PhNumberin=Entry(self.frame5,textvariable=self.PhNumber,validate='key')
        
        self.Idin.pack(side=LEFT)
        self.Namein.pack(side=LEFT)
        self.Sexin_m.pack(side=LEFT)
        self.Sexin_f.pack(side=LEFT)
        self.Birthin_year.pack(side=LEFT)
        self.Y.pack(side=LEFT)
        self.Birthin_month.pack(side=LEFT)
        self.M.pack(side=LEFT)
        self.Birthin_day.pack(side=LEFT)
        self.D.pack(side=LEFT)
        self.PhNumberin.pack(side=LEFT)

        self.Regi_confirm=Button(self.frame6,text='确认注册',
                            command=print('1000')
                  #,command= #将数据写入数据库
                  )
        self.Regi_reset=Button(self.frame6,text='重置',
                          command=erease_all())
        self.Regi_confirm.pack(side=LEFT,padx=30,pady=10)
        self.Regi_reset.pack(side=RIGHT,padx=30,pady=10)

        self.frame1.pack(pady=10)
        self.frame2.pack(pady=10)
        self.frame3.pack(pady=10)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=10)
        self.frame6.pack()
        
        mainloop()

if __name__ =='__main__':
    LoginInterface().LoginInterface_1()
    '''

'''
from tkinter import *
root=Tk()
def hahaha():
        root.quit()
def a():

    

    Label(root,text='作品').grid(row=0,column=0)#网格，n行n列
    Label(root,text='作者').grid(row=1,column=0)

    e1=Entry(root)
    e2=Entry(root)
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)

    def show():
        print('作品:%s'%e1.get())
        print('作者:%s'%e2.get())

    

    Button(root,text='获取信息',width=10,command=show)\
                                                   .grid(row=3,column=0,sticky='W',padx=10,pady=5)
    Button(root,text='退出',width=10,command=hahaha())\
                                                   .grid(row=3,column=1,sticky='E',padx=10,pady=5)
    #shell界面不能退出，双击点开可正常退出

    mainloop()

if __name__ == "__main__":
    a()
'''

"""
from tkinter import *
import time

import sys
sys.path.append(r'D:\python安装\自写模块')
import pytosql

LoInroot=Tk()

#注册
def ToDatabase(IdToWrite,PassToWrite,NameToWrite,SexToWrite,BirthToWrite,PhNumberToWrite):
    a=pytosql.pytosql()
    a.use('账号密码')
    print('==================')

def DataCheck(a,b,c,d,e,f,g,h):
    if(a and b and c and d and e and f and g and h):
        return True
    else:
        return False
    
def Register():  
    #检测数据是否全部填写完毕，并把数据写入数据库
    def DataUpdate():
        Birthin_month_Regi=Birthin_month.get()
        if len(Birthin_month_Regi)==1:
            Birthin_month_Regi='0'+Birthin_month_Regi
        else:
              pass
        
        Birthin_day_Regi=Birthin_day.get()
        if len(Birthin_day_Regi)==1:
            Birthin_day_Regi='0'+Birthin_day_Regi
        else:
              pass
        
        IdToWrite=Idin.get()
        PassToWrite=Passin.get()
        NameToWrite=Namein.get()
        SexToWrite=Sex.get()
        BirthToWrite=Birthin_year.get()+'-'+Birthin_month_Regi+'-'+Birthin_day_Regi
        PhNumberToWrite=PhNumberin.get()
        #检测是否全部填写完毕
        if DataCheck(IdToWrite,PassToWrite,NameToWrite,SexToWrite,
                     Birthin_year.get(),Birthin_month.get(),Birthin_month.get(),PhNumberToWrite):
            #再次监测数据是否合法               
            if(IdCheck() and PassCheck() and NameCheck() and Birthin_year_check()
               and Birthin_month_check() and Birthin_day_check() and PhNumber_check()):
                print(IdToWrite,PassToWrite,NameToWrite,SexToWrite,BirthToWrite,PhNumberToWrite)
                
                ToDatabase(IdToWrite,PassToWrite,NameToWrite,SexToWrite,BirthToWrite,PhNumberToWrite)

                Regiroot.destroy()
                LoginInterface()
            else:
                Regiroot.title('请先把数据填写完毕！')
        else:
            Regiroot.title('请先把数据填写完毕！')

    #重置
    def Reset():
        Regiroot.title('请注册')
        Idin.delete(0,END)
        Passin.delete(0,END)
        Namein.delete(0,END)
        Sex.set(1)
        Birthin_year.delete(0,END)
        Birthin_month.delete(0,END)
        Birthin_day.delete(0,END)
        PhNumberin.delete(0,END)
        ID_srting.set('身份证号码:')
        PASS_string.set('设置密码')
        NAME_string.set('姓名:')
        SEX_string.set('性别:')
        BIRTH_string.set('出生日期:')
        PHNUMBER_string.set('手机号码:')
        
    #检测输入数据是否合法
    def IdCheck():
        content=Idin.get() 
        if len(content)==18:
            if content[17]=='x' or content[17]=='X':
                if content[0:16].isdigit():
                    ID_srting.set('√')
                    return True
                else:
                    Idin.delete(0,END)
                    ID_srting.set('请输入正确的身份证号码！')
                    return False
            else:
                if content.isdigit():
                    ID_srting.set('√')
                    return True
                else:
                    Idin.delete(0,END)
                    ID_srting.set('请输入正确的身份证号码！')
                    return False
        else:
            Idin.delete(0,END)
            ID_srting.set('请输入正确的身份证号码！')
            return False

    def PassCheck():
        if len(Passin.get())>=8 and len(Passin.get())<=20:
            if Passin.get().isalnum:
                PASS_string.set('√')
                return True
            else:
                Passin.delete(0,END)
                PASS_string.set('密码只可由8到20位数字或字母组成')
                return False
        else:
            Passin.delete(0,END)
            PASS_string.set('密码只可由8到20位数字或字母组成')
            return False

    def NameCheck():
        if len(Namein.get())>=2 and len(Namein.get())<=20:
            if Namein.get().isalpha():
                NAME_string.set('√')
                return True
            elif ' ' in Namein.get():
                try:
                    a,b=Namein.get().split(' ')
                    if a.isalpha() and b.isalpha():
                        NAME_string.set('√')
                        return True
                    else:
                        Namein.delete(0,END)
                        NAME_string.set('请输入正确的名字！')
                        return False
                except ValueError:
                    Namein.delete(0,END)
                    NAME_string.set('请输入正确的名字！')
                    return False
            else:
                Namein.delete(0,END)
                NAME_string.set('请输入正确的名字！')
                return False
        else:
            Namein.delete(0,END)
            NAME_string.set('请输入正确的名字！')
            return False

    def SexCheck():
        b=Sex.get()
    
    def Birthin_year_check():
        try:
            if int(Birthin_year.get())>=1900 and int(Birthin_year.get())<=int(time.localtime().tm_year):
                return True
            else:
                Birthin_year.delete(0,END)
                Birthin_year.insert(0,'')
                return False
        except ValueError:
            Birthin_year.delete(0,END)
            Birthin_year.insert(0,'')
            return False
        
    def Birthin_month_check():
        try:
            if int(Birthin_month.get())<=12 and int(Birthin_month.get())>=1:
                return True
            else:
                Birthin_month.delete(0,END)
                Birthin_month.insert(0,'')
                return False
        except ValueError:
            Birthin_month.delete(0,END)
            Birthin_month.insert(0,'')
            return False

    def Birthin_day_check():
        try:
            if int(Birthin_day.get())>=1 and int(Birthin_day.get())<=31:
                return True
            else:
                Birthin_day.delete(0,END)
                Birthin_day.insert(0,'')
                return False
        except ValueError:
            Birthin_day.delete(0,END)
            Birthin_day.insert(0,'')
            return False

    def PhNumber_check():
        try:
            if len(PhNumberin.get())== 11 and PhNumberin.get().isdigit():
                if PhNumberin.get().isdigit():
                    PHNUMBER_string.set('√')
                    return True
                else:
                    PhNumberin.delete(0,END)
                    PHNUMBER_string.set('请输入正确的电话号码！')
                    return False
            else:
                PhNumberin.delete(0,END)
                PHNUMBER_string.set('请输入正确的电话号码！')
                return False
        except ValueError:
            PhNumberin.delete(0,END)
            PHNUMBER_string.set('请输入正确的电话号码！')
            return False

    #主体设置
    LoInroot.destroy()
    Regiroot=Tk()
    Regiroot.title('请注册')
    
    #框架设置
    frame1=Frame(Regiroot)
    frame_pass=Frame(Regiroot)
    frame2=Frame(Regiroot)
    frame3=Frame(Regiroot)
    frame4=Frame(Regiroot)
    frame5=Frame(Regiroot)
    frame6=Frame(Regiroot)

    #标题设置
    ID_srting=StringVar()
    ID_srting.set('身份证号码:')
    PASS_string=StringVar()
    PASS_string.set('设置密码')
    NAME_string=StringVar()
    NAME_string.set('姓名:')
    SEX_string=StringVar()
    SEX_string.set('性别:')
    BIRTH_string=StringVar()
    BIRTH_string.set('出生日期:')
    PHNUMBER_string=StringVar()
    PHNUMBER_string.set('手机号码:')
    
    IdLabel=Label(frame1,textvariable=ID_srting)
    PassLabel=Label(frame_pass,textvariable=PASS_string)
    NameLabel=Label(frame2,textvariable=NAME_string)
    SexLabel=Label(frame3,textvariable=SEX_string)
    BirthLabel=Label(frame4,textvariable=BIRTH_string)
    PhNumber=Label(frame5,textvariable=PHNUMBER_string)

    IdLabel.pack(side=LEFT)
    PassLabel.pack(side=LEFT)
    NameLabel.pack(side=LEFT)
    SexLabel.pack(side=LEFT)
    BirthLabel.pack(side=LEFT)
    PhNumber.pack(side=LEFT)

    #输入框架设置
    Id=StringVar()
    Pass=StringVar()
    Name=StringVar()
    Sex=StringVar()
    Birth_Y=StringVar()
    Birth_M=StringVar()
    Birth_D=StringVar()
    PhNumber=StringVar()

    Sexin_list=[('男','男'),('女','女')]
    Sex.set('男')
    
    Idin=Entry(frame1,textvariable=Id,validate='focusout',
               validatecommand=IdCheck)
    Passin=Entry(frame_pass,textvariable=Pass,validate='focusout',
                 validatecommand=PassCheck,show='*')
    Namein=Entry(frame2,textvariable=Name,validate='focusout',
                 validatecommand=NameCheck)
    for each,each_num in Sexin_list:
        Sexin=Radiobutton(frame3,text=each,variable=Sex,value=each_num,
                          validatecommand=SexCheck())
        Sexin.pack(side=LEFT)
        
    Birthin_year=Entry(frame4,textvariable=Birth_Y,validate='focusout',width=10,
                       validatecommand=Birthin_year_check)
    Y=Label(frame4,text='年')
    
    Birthin_month=Entry(frame4,textvariable=Birth_M,validate='focusout',width=10,
                        validatecommand=Birthin_month_check)
    M=Label(frame4,text='月')
    
    Birthin_day=Entry(frame4,textvariable=Birth_D,validate='focus',width=10,
                      validatecommand=Birthin_day_check)
    D=Label(frame4,text='日')
    
    PhNumberin=Entry(frame5,textvariable=PhNumber,validate='focusout',
                     validatecommand=PhNumber_check)
    
    Idin.pack(side=LEFT)
    Passin.pack(side=LEFT)
    Namein.pack(side=LEFT)
    Birthin_year.pack(side=LEFT)
    Y.pack(side=LEFT)
    Birthin_month.pack(side=LEFT)
    M.pack(side=LEFT)
    Birthin_day.pack(side=LEFT)
    D.pack(side=LEFT)
    PhNumberin.pack(side=LEFT)
    
    #按钮设置
    Regi_reset=Button(frame6,text='重置',command=Reset)
    Regi_reset.pack(side=RIGHT,padx=30,pady=10)
    Regi_confirm=Button(frame6,text='确认注册',command=DataUpdate)
    Regi_confirm.pack(side=LEFT,padx=30,pady=10)
                          
    frame1.pack(pady=10)
    frame_pass.pack(pady=10)
    frame2.pack(pady=10)
    frame3.pack(pady=10,side=TOP)
    frame4.pack(pady=10)
    frame5.pack(pady=10)
    frame6.pack()

    #窗口运行
    mainloop()


#登陆
def IdExistCheck():
    print('1')

def Login():
    '''a=pytosql.pytosql()
    a.use('账号密码')
    idnum=b2.get()'''
    print('3')
    
def LoginInterface():
    LoInroot.title('登录界面')

    Id=StringVar()
    Pass=StringVar()

    frame1=Frame(LoInroot)
    frame2=Frame(LoInroot)
    frame3=Frame(LoInroot)

    IdLabel=Label(frame1,text='账号')
    PassLabel=Label(frame2,text='密码')
    IdLabel.pack(side=LEFT)
    PassLabel.pack(side=LEFT,pady=10)

    Idin=Entry(frame1,textvariable=Id,validate='focusout',validatecommand=IdExistCheck)
    #此处检测账号是否存在
    Passin=Entry(frame2,textvariable=Pass)
    #不作操作，只作输入

    Idin.insert(0,'请输入身份证号码..')
    Idin.pack(side=LEFT,pady=10)
    Passin.pack(side=LEFT,pady=10)

    b1=Button(frame3,text='确认登陆',command=Login)#从此处检测密码是否正确
    b2=Button(frame3,text='注册',command=Register)
    b1.pack(side=LEFT,padx=30,pady=10)
    b2.pack(side=RIGHT,padx=30,pady=10)

    frame1.pack(
    frame2.pack()
    frame3.pack()

    mainloop()

if __name__ == '__main__':
    LoginInterface()#登陆界面
"""

'''
from tkinter import *
root=Tk()
messagebox.showinfo('222','111')
mainloop()
'''


'''
from tkinter import *
root = Tk()
root.title('试试文本框右键菜单')
root.resizable(False, False)
root.geometry("300x100+200+20")
Label(root, text='下面是一个刚刚被生成的文本框，试试操作吧').pack(side="top")
Label(root).pack(side="top")
show = StringVar()
Entry = Entry(root, textvariable=show, width="30")
Entry.pack()
class section:
    def onPaste(self):
        try:
            self.text = root.clipboard_get()
        except TclError:
            pass
        show.set(str(self.text))
    def onCopy(self):
        self.text = Entry.get()
        root.clipboard_append(self.text)
    def onCut(self):
        self.onCopy()
        try:
            Entry.delete('sel.first', 'sel.last')
        except TclError:
            pass
section = section()
menu = Menu(root, tearoff=0)
menu.add_command(label="复制", command=section.onCopy)
menu.add_separator()
menu.add_command(label="粘贴", command=section.onPaste)
menu.add_separator()
menu.add_command(label="剪切", command=section.onCut)
def popupmenu(event):
    menu.post(event.x_root, event.y_root)
Entry.bind("<Button-3>", popupmenu)
root.mainloop()
'''

'''
from tkinter import *
class Select(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.label = Label(self, text="选择项目")
        self.listBox = Listbox(self, height=1)
        self.button = Button(self, text='V', command=self.triggle)
        self.hideList = True
        for i in xrange(10):
            self.listBox.insert(i, 'Item%d'%i)
        self.label.grid(row=0, column=0, sticky=N)
        self.listBox.grid(row=0, column=1, sticky=N)
        self.button.grid(row=0, column=2, sticky=N)
        self.grid()
    def triggle(self):
        self.hideList ^= 1
        self.listBox.config(height=[self.listBox.size(), 1][self.hideList])
app = Select()
app.mainloop()
'''

'''
import serial
import time
while True:
    try:
        a=serial.Serial('com2')
    except serial.serialutil.SerialException:
        b=a.read().decode('utf-8')
        break
print(b
'''

'''
import serial
def A():
    c=[]
    a=serial.Serial(port='com2')
    while True:
        c.append(a.read().decode('utf-8'))
        if '\n' in c:
            break
    return c

def B():
    b=A()
    
    print (b)

B()
'''
'''
import django
<html>
<head>
<title>
哈哈
</title>
</head>
<body>
哈哈哈
</body>
</html>
'''

'''
import time
import serial
ser = serial.Serial( #下面这些参数根据情况修改
  port='COM7',
  baudrate=9600,
  parity=serial.PARITY_ODD,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.SEVENBITS
)
data = ''
while ser.inWaiting() > 0:
  data += ser.read(1)
if data != '':
  print (data)
'''

'''
class Rectangle:
    def __init__(self,height=0,width=0):
        self.height=height
        self.width=width
    def __setattr__(self,name,value):
        if name=='square':
            self.width=value
            self.height=value
        else:
            #super().__setattr__(name,value)
            self.__dict__[name]=value #用这两个方法避免（self.name=value）进入死循环
    def getArea(self):
        return self.width*self.height
'''

'''
class lis(list):
    def __new__(cls,num):
        return list.__new__(cls,num)
'''

'''
#!/etc/bin/env python
#-*-encoding=utf-8-*-
#auth@:dengyongkai
#blog@:blog.sina.com.cn/kaiyongdeng
 
import poplib,email
from email.header import decode_header
import smtplib
import time
import os,sys
import random
 
def accp_mail():
  try:
    p=poplib.POP3('pop.qq.com')
    p.user('用户名')
    p.pass_('密码')
    ret = p.stat()
  except poplib.error_proto:
    return 1
    print "Login failed:",e
    sys.exit(1)
#  for i in range(1,ret[0]+1):
#    str=s.top(i,0)
#    strlist=[]
#    for x in str[1]:
#      try:
#        strlist.append(x.decode())
#      except:
#        try:
#          strlist.append(x.decode('gbk'))
#        except:
#          strlist.append(x.decode('big5'))
#          
#    mm = email.message_from_string('\n'.join(strlist))
#    sub=decode_header(mm['subject'])
#    if sub[0][1]:
#      submsg = sub[0][0].decode(sub[0][1])
#    else:
#      submsg = sub[0][0]
#
#    if submsg.strip()=='startpc':
#      s.dele(i)
#      return 0
#    
#  s.quit()
#  return 1
#
  for item in p.list()[1]:
    number,octets = item.split(' ')
#    print "Message %s: %sbytes"%(number,octets)
    lines = p.retr(number)[1]
    msg = email.message_from_string("\n".join(lines))
#  print msg.as_string()
    print msg.get_payload()
    if msg.get_payload()=="start\n\n":
      return 0
 
def send_mail():
  try:
    handle = smtplib.SMTP('smtp.163.com', 25)
    handle.login('********@163.com','密码')
    msg = "To: ********@qq.com\r\nFrom: ********@163.com\r\nSubject: startpc \r\n\r\nstart\r\n"
    handle.sendmail('********@163.com','********@qq.com', msg)
    handle.close()
    return 1
  except:
    return 0
 
 
if __name__=='__main__':
  while send_mail()==0:
    time.sleep(2)
 
  while 1:
    time.sleep(5)
    if accp_mail()==0:
      os.system('shutdown -f -s -t 10 -c closing...')
      #print "哈哈哈哈哈哈哈，成功啦！！！！！！"
      break
'''

'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import VideoCapture
###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 566,535 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnButton )
        #self.m_panel1.Bind(wx.EVT_IDLE,self.OnIdel)
        self.timer=wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.OnIdel,self.timer)
    def OnIdel(self,evnet):
        #cam = VideoCapture.Device()
        self.cam.saveSnapshot('test.jpg')
        img=wx.Image("test.jpg",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        dc=wx.ClientDC(self.m_panel1)
        dc.DrawBitmap(img,0,0,False)
        
    def OnButton( self, event ):
        self.cam = VideoCapture.Device()
        #cam.saveSnapshot('test.jpg')
        self.timer.Start(100)
        event.Skip()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame1(None)
    frame.Show(True)
    app.MainLoop()
'''


'''
import urllib.request as ur  
import json  
  
def getHtml(url):  
    page = ur.urlopen(url)  
    html = page.read().decode('utf-8')
    return html  
  
if __name__ == '__main__':  
    key = 'c37cc4814cbf47febbb89f88f5f73122'  
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='  
    while True:  
        info = input('我: ')
        request = api + info  
        response = getHtml(request)  
        dic_json = json.loads(response)  
        print ('机器人: ' + dic_json['text'])
 '''

'''
import threading
import time
def loop0():
    print('start loop0() at %s' % (time.ctime()))
    time.sleep(4)
    print('finish loop0() at %s' % (time.ctime()))
def loop1():
    print('start loop1() at %s' % (time.ctime()))
    time.sleep(2)
    print('finish loop1() at %s' % (time.ctime()))
def main():
    print('statrint at %s' % time.ctime())
    loop0()
    loop1()
    print('all finish at %s' % time.ctime())
    
main()
'''
'''
import threading
import time
def loop(nloop,nsec):
    print('start loop',nloop,'at:',time.ctime())
    time.sleep(nsec)
    print('loop',nloop,'done at',time.ctime())
def main():
    print('starting at',time.ctime())
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all done at',time.ctime())
loops=[4,2]
main()
'''
'''
import threading
import time
class ThreadFunc:
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        self.func(*self.args)
        
def loop(nloop,nsec):
    print('start loop',nloop,'at:',time.ctime())
    time.sleep(nsec)
    print('loop',nloop,'done at',time.ctime())
def main():
    print('starting at',time.ctime())
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all done at',time.ctime())
loops=[4,2]
main()
'''

a='''
station_names ='@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|

BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|BXP|beijingxi|bjx|4@gzn|广州南|

IZQ|guangzhounan|gzn|5@cqb|重庆北|CUW|chongqingbei|cqb|6@cqi|重庆|CQW|chongqing|cq|7@cqn|重庆南

|CRW|chongqingnan|cqn|8@gzd|广州东|GGQ|guangzhoudong|gzd|9@sha|上海|SHH|shanghai|sh|10@shn|上海

南|SNH|shanghainan|shn|11@shq|上海虹桥|AOH|shanghaihongqiao|shhq|12@shx|上海西|SXH|shanghaixi|

shx|13@tjb|天津北|TBP|tianjinbei|tjb|14@tji|天津|TJP|tianjin|tj|15@tjn|天津南|TIP|tianjinnan|

tjn|16@tjx|天津西|TXP|tianjinxi|tjx|17@cch|长春|CCT|changchun|cc|18@ccn|长春南|CET|

changchunnan|ccn|19@ccx|长春西|CRT|changchunxi|ccx|20@cdd|成都东|ICW|chengdudong|cdd|21@cdn|成

都南|CNW|chengdunan|cdn|22@cdu|成都|CDW|chengdu|cd|23@csh|长沙|CSQ|changsha|cs|24@csn|长沙南|

CWQ|changshanan|csn|25@fzh|福州|FZS|fuzhou|fz|26@fzn|福州南|FYS|fuzhounan|fzn|27@gya|贵阳|GIW|

guiyang|gy|28@gzh|广州|GZQ|guangzhou|gz|29@gzx|广州西|GXQ|guangzhouxi|gzx|30@heb|哈尔滨|HBB|

haerbin|heb|31@hed|哈尔滨东|VBB|haerbindong|hebd|32@hex|哈尔滨西|VAB|haerbinxi|hebx|33@hfe|合肥

|HFH|hefei|hf|34@hfx|合肥西|HTH|hefeixi|hfx|35@hhd|呼和浩特东|NDC|huhehaotedong|hhhtd|36@hht|呼

和浩特|HHC|huhehaote|hhht|37@hkd|海  口东|KEQ|haikoudong|hkd|38@hkd|海口东|HMQ|haikoudong|hkd|

39@hko|海口|VUQ|haikou|hk|40@hzd|杭州东|HGH|hangzhoudong|hzd|41@hzh|杭州|HZH|hangzhou|hz|

42@hzn|杭州南|XHH|hangzhounan|hzn|43@jna|济南|JNK|jinan|jn|44@jnd|济南东|JAK|jinandong|jnd|

45@jnx|济南西|JGK|jinanxi|jnx|46@kmi|昆明|KMM|kunming|km|47@kmx|昆明西|KXM|kunmingxi|kmx|

48@lsa|拉萨|LSO|lasa|ls|49@lzd|兰州东|LVJ|lanzhoudong|lzd|50@lzh|兰州|LZJ|lanzhou|lz|51@lzx|兰

州西|LAJ|lanzhouxi|lzx|52@nch|南昌|NCG|nanchang|nc|53@nji|南京|NJH|nanjing|nj|54@njn|南京南|

NKH|nanjingnan|njn|55@nni|南宁|NNZ|nanning|nn|56@sjb|石家庄北|VVP|shijiazhuangbei|sjzb|57@sjz|

石家庄|SJP|shijiazhuang|sjz|58@sya|沈阳|SYT|shenyang|sy|59@syb|沈阳北|SBT|shenyangbei|syb|

60@syd|沈阳东|SDT|shenyangdong|syd|61@tyb|太原北|TBV|taiyuanbei|tyb|62@tyd|太原东|TDV|

taiyuandong|tyd|63@tyu|太原|TYV|taiyuan|ty|64@wha|武汉|WHN|wuhan|wh|65@wjx|王家营西|KNM|

wangjiayingxi|wjyx|66@wln|乌鲁木齐南|WMR|wulumuqinan|wlmqn|67@xab|西安北|EAY|xianbei|xab|

68@xan|西安|XAY|xian|xa|69@xan|西安南|CAY|xiannan|xan|70@xni|西宁|XNO|xining|xn|71@ych|银川|

YIJ|yinchuan|yc|72@zzh|郑州|ZZF|zhengzhou|zz|73@aes|阿尔山|ART|aershan|aes|74@aka|安康|AKY|

ankang|ak|75@aks|阿克苏|ASR|akesu|aks|76@alh|阿里河|AHX|alihe|alh|77@alk|阿拉山口|AKR|

alashankou|alsk|78@api|安平|APT|anping|ap|79@aqi|安庆|AQH|anqing|aq|80@ash|安顺|ASW|anshun|as|

81@ash|鞍山|AST|anshan|as|82@aya|安阳|AYF|anyang|ay|83@ban|北安|BAB|beian|ba|84@bbu|蚌埠|BBH|

bengbu|bb|85@bch|白城|BCT|baicheng|bc|86@bha|北海|BHZ|beihai|bh|87@bhe|白河|BEL|baihe|bh|

88@bji|白涧|BAP|baijian|bj|89@bji|宝鸡|BJY|baoji|bj|90@bji|滨江|BJB|binjiang|bj|91@bkt|博克图|

BKX|boketu|bkt|92@bse|百色|BIZ|baise|bs|93@bss|白山市|HJL|baishanshi|bss|94@bta|北台|BTT|

beitai|bt|95@btd|包头东|BDC|baotoudong|btd|96@bto|包头|BTC|baotou|bt|97@bts|北屯市|BXR|

beitunshi|bts|98@bxi|本溪|BXT|benxi|bx|99@byb|白云鄂博|BEC|baiyunebo|byeb|100@byx|白银西|BXJ|

baiyinxi|byx|101@bzh|亳州|BZH|bozhou|bz|102@cbi|赤壁|CBN|chibi|cb|103@cde|常德|VGQ|changde|cd|

104@cde|承德|CDP|chengde|cd|105@cdi|长甸|CDT|changdian|cd|106@cfe|赤峰|CFD|chifeng|cf|107@cli|

茶陵|CDG|chaling|cl|108@cna|苍南|CEH|cangnan|cn|109@cpi|昌平|CPP|changping|cp|110@cre|崇仁|

CRG|chongren|cr|111@ctu|昌图|CTT|changtu|ct|112@ctz|长汀镇|CDB|changtingzhen|ctz|113@cxi|曹县|

CXK|caoxian|cx|114@cxi|楚雄|COM|chuxiong|cx|115@cxt|陈相屯|CXT|chenxiangtun|cxt|116@czb|长治

北|CBF|changzhibei|czb|117@czh|池州|IYH|chizhou|cz|118@czh|长征|CZJ|changzheng|cz|119@czh|常

州|CZH|changzhou|cz|120@czh|郴州|CZQ|chenzhou|cz|121@czh|长治|CZF|changzhi|cz|122@czh|沧州|

COP|cangzhou|cz|123@czu|崇左|CZZ|chongzuo|cz|124@dab|大安北|RNT|daanbei|dab|125@dch|大成|DCT|

dacheng|dc|126@ddo|丹东|DUT|dandong|dd|127@dfh|东方红|DFB|dongfanghong|dfh|128@dgd|东莞东|DMQ|

dongguandong|dgd|129@dhs|大虎山|DHD|dahushan|dhs|130@dhu|敦煌|DHJ|dunhuang|dh|131@dhu|敦化|

DHL|dunhua|dh|132@dhu|德惠|DHT|dehui|dh|133@djc|东京城|DJB|dongjingcheng|djc|134@dji|大涧|DFP|

dajian|dj|135@djy|都江堰|DDW|dujiangyan|djy|136@dlb|大连北|DFT|dalianbei|dlb|137@dli|大理|DKM|

dali|dl|138@dli|大连|DLT|dalian|dl|139@dna|定南|DNG|dingnan|dn|140@dqi|大庆|DZX|daqing|dq|

141@dsh|东胜|DOC|dongsheng|ds|142@dsq|大石桥|DQT|dashiqiao|dsq|143@dto|大同|DTV|datong|dt|

144@dyi|东营|DPK|dongying|dy|145@dys|大杨树|DUX|dayangshu|dys|146@dyu|都匀|RYW|duyun|dy|

147@dzh|邓州|DOF|dengzhou|dz|148@dzh|达州|RXW|dazhou|dz|149@dzh|德州|DZP|dezhou|dz|150@ejn|额济

纳|EJC|ejina|ejn|151@eli|二连|RLC|erlian|el|152@esh|恩施|ESN|enshi|es|153@fdi|福鼎|FES|fuding|

fd|154@fhc|凤凰机场|FJQ|fenghuangjichang|fhjc|155@fld|风陵渡|FLV|fenglingdu|fld|156@fli|涪陵|

FLW|fuling|fl|157@flj|富拉尔基|FRX|fulaerji|flej|158@fsb|抚顺北|FET|fushunbei|fsb|159@fsh|佛

山|FSQ|foshan|fs|160@fxn|阜新南|FXD|fuxinnan|fxn|161@fya|阜阳|FYH|fuyang|fy|162@gem|格尔木|

GRO|geermu|gem|163@gha|广汉|GHW|guanghan|gh|164@gji|古交|GJV|gujiao|gj|165@glb|桂林北|GBZ|

guilinbei|glb|166@gli|古莲|GRX|gulian|gl|167@gli|桂林|GLZ|guilin|gl|168@gsh|固始|GXN|gushi|gs|

169@gsh|广水|GSN|guangshui|gs|170@gta|干塘|GNJ|gantang|gt|171@gyu|广元|GYW|guangyuan|gy|

172@gzb|广州北|GBQ|guangzhoubei|gzb|173@gzh|赣州|GZG|ganzhou|gz|174@gzl|公主岭|GLT|

gongzhuling|gzl|175@gzn|公主岭南|GBT|gongzhulingnan|gzln|176@han|淮安|AUH|huaian|ha|177@hbe|淮

北|HRH|huaibei|hb|178@hbe|鹤北|HMB|hebei|hb|179@hbi|淮滨|HVN|huaibin|hb|180@hbi|河边|HBV|

hebian|hb|181@hch|潢川|KCN|huangchuan|hc|182@hch|韩城|HCY|hancheng|hc|183@hda|邯郸|HDP|handan|

hd|184@hdz|横道河子|HDB|hengdaohezi|hdhz|185@hga|鹤岗|HGB|hegang|hg|186@hgt|皇姑屯|HTT|

huanggutun|hgt|187@hgu|红果|HEM|hongguo|hg|188@hhe|黑河|HJB|heihe|hh|189@hhu|怀化|HHQ|huaihua|

hh|190@hko|汉口|HKN|hankou|hk|191@hld|葫芦岛|HLD|huludao|hld|192@hle|海拉尔|HRX|hailaer|hle|

193@hll|霍林郭勒|HWD|huolinguole|hlgl|194@hlu|海伦|HLB|hailun|hl|195@hma|侯马|HMV|houma|hm|

196@hmi|哈密|HMR|hami|hm|197@hna|淮南|HAH|huainan|hn|198@hna|桦南|HNB|huanan|hn|199@hnx|海宁

西|EUH|hainingxi|hnx|200@hqi|鹤庆|HQM|heqing|hq|201@hrb|怀柔北|HBP|huairoubei|hrb|202@hro|怀

柔|HRP|huairou|hr|203@hsd|黄石东|OSN|huangshidong|hsd|204@hsh|华山|HSY|huashan|hs|205@hsh|黄

山|HKH|huangshan|hs|206@hsh|黄石|HSN|huangshi|hs|207@hsh|衡水|HSP|hengshui|hs|208@hya|衡阳|

HYQ|hengyang|hy|209@hze|菏泽|HIK|heze|hz|210@hzh|贺州|HXZ|hezhou|hz|211@hzh|汉中|HOY|hanzhong|

hz|212@hzh|惠州|HCQ|huizhou|hz|213@jan|吉安|VAG|jian|ja|214@jan|集安|JAL|jian|ja|215@jbc|江边村

|JBG|jiangbiancun|jbc|216@jch|晋城|JCF|jincheng|jc|217@jcj|金城江|JJZ|jinchengjiang|jcj|

218@jdz|景德镇|JCG|jingdezhen|jdz|219@jfe|嘉峰|JFF|jiafeng|jf|220@jgq|加格达奇|JGX|jiagedaqi|

jgdq|221@jgs|井冈山|JGG|jinggangshan|jgs|222@jhe|蛟河|JHL|jiaohe|jh|223@jhn|金华南|RNH|

jinhuanan|jhn|224@jhu|金华|JBH|jinhua|jh|225@jji|九江|JJG|jiujiang|jj|226@jli|吉林|JLL|jilin|

jl|227@jme|荆门|JMN|jingmen|jm|228@jms|佳木斯|JMB|jiamusi|jms|229@jni|济宁|JIK|jining|jn|

230@jnn|集宁南|JAC|jiningnan|jnn|231@jqu|酒泉|JQJ|jiuquan|jq|232@jsh|江山|JUH|jiangshan|js|

233@jsh|吉首|JIQ|jishou|js|234@jta|九台|JTL|jiutai|jt|235@jts|镜铁山|JVJ|jingtieshan|jts|

236@jxi|鸡西|JXB|jixi|jx|237@jxx|绩溪县|JRH|jixixian|jxx|238@jyg|嘉峪关|JGJ|jiayuguan|jyg|

239@jyo|江油|JFW|jiangyou|jy|240@jzh|锦州|JZD|jinzhou|jz|241@jzh|金州|JZT|jinzhou|jz|242@jzh|蓟

州|JKP|jizhou|jz|243@kel|库尔勒|KLR|kuerle|kel|244@kfe|开封|KFF|kaifeng|kf|245@kla|岢岚|KLV|

kelan|kl|246@kli|凯里|KLW|kaili|kl|247@ksh|喀什|KSR|kashi|ks|248@ksn|昆山南|KNH|kunshannan|

ksn|249@ktu|奎屯|KTR|kuitun|kt|250@kyu|开原|KYT|kaiyuan|ky|251@lan|六安|UAH|luan|la|252@lba|灵

宝|LBF|lingbao|lb|253@lcg|芦潮港|UCH|luchaogang|lcg|254@lch|隆昌|LCW|longchang|lc|255@lch|陆

川|LKZ|luchuan|lc|256@lch|利川|LCN|lichuan|lc|257@lch|临川|LCG|linchuan|lc|258@lch|潞城|UTP|

lucheng|lc|259@lda|鹿道|LDL|ludao|ld|260@ldi|娄底|LDQ|loudi|ld|261@lfe|临汾|LFV|linfen|lf|

262@lgz|良各庄|LGP|lianggezhuang|lgz|263@lhe|临河|LHC|linhe|lh|264@lhe|漯河|LON|luohe|lh|

265@lhu|绿化|LWJ|lvhua|lh|266@lhu|隆化|UHP|longhua|lh|267@lji|丽江|LHM|lijiang|lj|268@lji|临

江|LQL|linjiang|lj|269@lji|龙井|LJL|longjing|lj|270@lli|吕梁|LHV|lvliang|ll|271@lli|醴陵|LLG|

liling|ll|272@lln|柳林南|LKV|liulinnan|lln|273@lpi|滦平|UPP|luanping|lp|274@lps|六盘水|UMW|

liupanshui|lps|275@lqi|灵丘|LVV|lingqiu|lq|276@lsh|旅顺|LST|lvshun|ls|277@lxi|兰溪|LWH|lanxi|

lx|278@lxi|陇西|LXJ|longxi|lx|279@lxi|澧县|LEQ|lixian|lx|280@lxi|临西|UEP|linxi|lx|281@lya|龙岩

|LYS|longyan|ly|282@lya|耒阳|LYQ|leiyang|ly|283@lya|洛阳|LYF|luoyang|ly|284@lyd|连云港东|UKH|

lianyungangdong|lygd|285@lyd|洛阳东|LDF|luoyangdong|lyd|286@lyi|临沂|LVK|linyi|ly|287@lym|洛阳

龙门|LLF|luoyanglongmen|lylm|288@lyu|柳园|DHR|liuyuan|ly|289@lyu|凌源|LYD|lingyuan|ly|290@lyu|

辽源|LYL|liaoyuan|ly|291@lzh|立志|LZX|lizhi|lz|292@lzh|柳州|LZZ|liuzhou|lz|293@lzh|辽中|LZD|

liaozhong|lz|294@mch|麻城|MCN|macheng|mc|295@mdh|免渡河|MDX|mianduhe|mdh|296@mdj|牡丹江|MDB|

mudanjiang|mdj|297@meg|莫尔道嘎|MRX|moerdaoga|medg|298@mgu|明光|MGH|mingguang|mg|299@mgu|满归|

MHX|mangui|mg|300@mhe|漠河|MVX|mohe|mh|301@mmi|茂名|MDQ|maoming|mm|302@mmx|茂名西|MMZ|

maomingxi|mmx|303@msh|密山|MSB|mishan|ms|304@msj|马三家|MJT|masanjia|msj|305@mwe|麻尾|VAW|

mawei|mw|306@mya|绵阳|MYW|mianyang|my|307@mzh|梅州|MOQ|meizhou|mz|308@mzl|满洲里|MLX|

manzhouli|mzl|309@nbd|宁波东|NVH|ningbodong|nbd|310@nbo|宁波|NGH|ningbo|nb|311@nch|南岔|NCB|

nancha|nc|312@nch|南充|NCW|nanchong|nc|313@nda|南丹|NDZ|nandan|nd|314@ndm|南大庙|NMP|

nandamiao|ndm|315@nfe|南芬|NFT|nanfen|nf|316@nhe|讷河|NHX|nehe|nh|317@nji|嫩江|NGX|nenjiang|

nj|318@nji|内江|NJW|neijiang|nj|319@npi|南平|NPS|nanping|np|320@nto|南通|NUH|nantong|nt|

321@nya|南阳|NFF|nanyang|ny|322@nzs|碾子山|NZX|nianzishan|nzs|323@pds|平顶山|PEN|pingdingshan|

pds|324@pji|盘锦|PVD|panjin|pj|325@pli|平凉|PIJ|pingliang|pl|326@pln|平凉南|POJ|pingliangnan|

pln|327@pqu|平泉|PQP|pingquan|pq|328@psh|坪石|PSQ|pingshi|ps|329@pxi|萍乡|PXG|pingxiang|px|

330@pxi|凭祥|PXZ|pingxiang|px|331@pxx|郫县西|PCW|pixianxi|pxx|332@pzh|攀枝花|PRW|panzhihua|

pzh|333@qch|蕲春|QRN|qichun|qc|334@qcs|青城山|QSW|qingchengshan|qcs|335@qda|青岛|QDK|qingdao|

qd|336@qhc|清河城|QYP|qinghecheng|qhc|337@qji|曲靖|QJM|qujing|qj|338@qji|黔江|QNW|qianjiang|

qj|339@qjz|前进镇|QEB|qianjinzhen|qjz|340@qqe|齐齐哈尔|QHX|qiqihaer|qqhe|341@qth|七台河|QTB|

qitaihe|qth|342@qxi|沁县|QVV|qinxian|qx|343@qzd|泉州东|QRS|quanzhoudong|qzd|344@qzh|泉州|QYS|

quanzhou|qz|345@qzh|衢州|QEH|quzhou|qz|346@ran|融安|RAZ|rongan|ra|347@rjg|汝箕沟|RQJ|rujigou|

rjg|348@rji|瑞金|RJG|ruijin|rj|349@rzh|日照|RZK|rizhao|rz|350@scp|双城堡|SCB|shuangchengpu|

scp|351@sfh|绥芬河|SFB|suifenhe|sfh|352@sgd|韶关东|SGQ|shaoguandong|sgd|353@shg|山海关|SHD|

shanhaiguan|shg|354@shu|绥化|SHB|suihua|sh|355@sjf|三间房|SFX|sanjianfang|sjf|356@sjt|苏家屯|

SXT|sujiatun|sjt|357@sla|舒兰|SLL|shulan|sl|358@smi|三明|SMS|sanming|sm|359@smu|神木|OMY|

shenmu|sm|360@smx|三门峡|SMF|sanmenxia|smx|361@sna|商南|ONY|shangnan|sn|362@sni|遂宁|NIW|

suining|sn|363@spi|四平|SPT|siping|sp|364@sqi|商丘|SQF|shangqiu|sq|365@sra|上饶|SRG|shangrao|

sr|366@ssh|韶山|SSQ|shaoshan|ss|367@sso|宿松|OAH|susong|ss|368@sto|汕头|OTQ|shantou|st|369@swu|

邵武|SWS|shaowu|sw|370@sxi|涉县|OEP|shexian|sx|371@sya|三亚|SEQ|sanya|sy|372@sya|三  亚|JUQ|

sanya|sya|373@sya|邵阳|SYQ|shaoyang|sy|374@sya|十堰|SNN|shiyan|sy|375@sys|双鸭山|SSB|

shuangyashan|sys|376@syu|松原|VYT|songyuan|sy|377@szh|苏州|SZH|suzhou|sz|378@szh|深圳|SZQ|

shenzhen|sz|379@szh|宿州|OXH|suzhou|sz|380@szh|随州|SZN|suizhou|sz|381@szh|朔州|SUV|shuozhou|

sz|382@szx|深圳西|OSQ|shenzhenxi|szx|383@tba|塘豹|TBQ|tangbao|tb|384@teq|塔尔气|TVX|taerqi|

teq|385@tgu|潼关|TGY|tongguan|tg|386@tgu|塘沽|TGP|tanggu|tg|387@the|塔河|TXX|tahe|th|388@thu|通

化|THL|tonghua|th|389@tla|泰来|TLX|tailai|tl|390@tlf|吐鲁番|TFR|tulufan|tlf|391@tli|通辽|TLD|

tongliao|tl|392@tli|铁岭|TLT|tieling|tl|393@tlz|陶赖昭|TPT|taolaizhao|tlz|394@tme|图们|TML|

tumen|tm|395@tre|铜仁|RDQ|tongren|tr|396@tsb|唐山北|FUP|tangshanbei|tsb|397@tsf|田师府|TFT|

tianshifu|tsf|398@tsh|泰山|TAK|taishan|ts|399@tsh|唐山|TSP|tangshan|ts|400@tsh|天水|TSJ|

tianshui|ts|401@typ|通远堡|TYT|tongyuanpu|typ|402@tys|太阳升|TQT|taiyangsheng|tys|403@tzh|泰

州|UTH|taizhou|tz|404@tzi|桐梓|TZW|tongzi|tz|405@tzx|通州西|TAP|tongzhouxi|tzx|406@wch|五常|

WCB|wuchang|wc|407@wch|武昌|WCN|wuchang|wc|408@wfd|瓦房店|WDT|wafangdian|wfd|409@wha|威海|WKK|

weihai|wh|410@whu|芜湖|WHH|wuhu|wh|411@whx|乌海西|WXC|wuhaixi|whx|412@wjt|吴家屯|WJT|wujiatun|

wjt|413@wlo|武隆|WLW|wulong|wl|414@wlt|乌兰浩特|WWT|wulanhaote|wlht|415@wna|渭南|WNY|weinan|

wn|416@wsh|威舍|WSM|weishe|ws|417@wts|歪头山|WIT|waitoushan|wts|418@wwe|武威|WUJ|wuwei|ww|

419@wwn|武威南|WWJ|wuweinan|wwn|420@wxi|无锡|WXH|wuxi|wx|421@wxi|乌西|WXR|wuxi|wx|422@wyl|乌伊

岭|WPB|wuyiling|wyl|423@wys|武夷山|WAS|wuyishan|wys|424@wyu|万源|WYY|wanyuan|wy|425@wzh|万州|

WYW|wanzhou|wz|426@wzh|梧州|WZZ|wuzhou|wz|427@wzh|温州|RZH|wenzhou|wz|428@wzn|温州南|VRH|

wenzhounan|wzn|429@xch|西昌|ECW|xichang|xc|430@xch|许昌|XCF|xuchang|xc|431@xcn|西昌南|ENW|

xichangnan|xcn|432@xfa|香坊|XFB|xiangfang|xf|433@xga|轩岗|XGV|xuangang|xg|434@xgu|兴国|EUG|

xingguo|xg|435@xha|宣汉|XHY|xuanhan|xh|436@xhu|新会|EFQ|xinhui|xh|437@xhu|新晃|XLQ|xinhuang|

xh|438@xlt|锡林浩特|XTC|xilinhaote|xlht|439@xlx|兴隆县|EXP|xinglongxian|xlx|440@xmb|厦门北|

XKS|xiamenbei|xmb|441@xme|厦门|XMS|xiamen|xm|442@xmq|厦门高崎|XBS|xiamengaoqi|xmgq|443@xsh|小市

|XST|xiaoshi|xs|444@xsh|秀山|ETW|xiushan|xs|445@xta|向塘|XTG|xiangtang|xt|446@xwe|宣威|XWM|

xuanwei|xw|447@xxi|新乡|XXF|xinxiang|xx|448@xya|信阳|XUN|xinyang|xy|449@xya|咸阳|XYY|xianyang|

xy|450@xya|襄阳|XFN|xiangyang|xy|451@xyc|熊岳城|XYT|xiongyuecheng|xyc|452@xyi|新沂|VIH|xinyi|

xy|453@xyi|兴义|XRZ|xingyi|xy|454@xyu|新余|XUG|xinyu|xy|455@xzh|徐州|XCH|xuzhou|xz|456@yan|延安

|YWY|yanan|ya|457@ybi|宜宾|YBW|yibin|yb|458@ybn|亚布力南|YWB|yabulinan|ybln|459@ybs|叶柏寿|

YBD|yebaishou|ybs|460@ycd|宜昌东|HAN|yichangdong|ycd|461@ych|永川|YCW|yongchuan|yc|462@ych|盐城

|AFH|yancheng|yc|463@ych|宜昌|YCN|yichang|yc|464@ych|运城|YNV|yuncheng|yc|465@ych|伊春|YCB|

yichun|yc|466@yci|榆次|YCV|yuci|yc|467@ycu|杨村|YBP|yangcun|yc|468@ycx|宜春西|YCG|yichunxi|

ycx|469@yes|伊尔施|YET|yiershi|yes|470@yga|燕岗|YGW|yangang|yg|471@yji|永济|YIV|yongji|yj|

472@yji|延吉|YJL|yanji|yj|473@yko|营口|YKT|yingkou|yk|474@yks|牙克石|YKX|yakeshi|yks|475@yli|阎

良|YNY|yanliang|yl|476@yli|玉林|YLZ|yulin|yl|477@yli|榆林|ALY|yulin|yl|478@ylw|亚龙湾|TWQ|

yalongwan|ylw|479@ymp|一面坡|YPB|yimianpo|ymp|480@yni|伊宁|YMR|yining|yn|481@ypg|阳平关|YAY|

yangpingguan|ypg|482@ypi|玉屏|YZW|yuping|yp|483@ypi|原平|YPV|yuanping|yp|484@yqi|延庆|YNP|

yanqing|yq|485@yqq|阳泉曲|YYV|yangquanqu|yqq|486@yqu|玉泉|YQB|yuquan|yq|487@yqu|阳泉|AQP|

yangquan|yq|488@ysh|营山|NUW|yingshan|ys|489@ysh|玉山|YNG|yushan|ys|490@ysh|燕山|AOP|yanshan|

ys|491@ysh|榆树|YRT|yushu|ys|492@yta|鹰潭|YTG|yingtan|yt|493@yta|烟台|YAK|yantai|yt|494@yth|伊

图里河|YEX|yitulihe|ytlh|495@ytx|玉田县|ATP|yutianxian|ytx|496@ywu|义乌|YWH|yiwu|yw|497@yxi|阳

新|YON|yangxin|yx|498@yxi|义县|YXD|yixian|yx|499@yya|益阳|AEQ|yiyang|yy|500@yya|岳阳|YYQ|

yueyang|yy|501@yzh|崖州|YUQ|yazhou|yz|502@yzh|永州|AOQ|yongzhou|yz|503@yzh|扬州|YLH|yangzhou|

yz|504@zbo|淄博|ZBK|zibo|zb|505@zcd|镇城底|ZDV|zhenchengdi|zcd|506@zgo|自贡|ZGW|zigong|zg|

507@zha|珠海|ZHQ|zhuhai|zh|508@zhb|珠海北|ZIQ|zhuhaibei|zhb|509@zji|湛江|ZJZ|zhanjiang|zj|

510@zji|镇江|ZJH|zhenjiang|zj|511@zjj|张家界|DIQ|zhangjiajie|zjj|512@zjk|张家口|ZKP|

zhangjiakou|zjk|513@zjn|张家口南|ZMP|zhangjiakounan|zjkn|514@zko|周口|ZKN|zhoukou|zk|515@zlm|哲

里木|ZLC|zhelimu|zlm|516@zlt|扎兰屯|ZTX|zhalantun|zlt|517@zmd|驻马店|ZDN|zhumadian|zmd|518@zqi|

肇庆|ZVQ|zhaoqing|zq|519@zsz|周水子|ZIT|zhoushuizi|zsz|520@zto|昭通|ZDW|zhaotong|zt|521@zwe|中

卫|ZWJ|zhongwei|zw|522@zya|资阳|ZYW|ziyang|zy|523@zyi|遵义|ZIW|zunyi|zy|524@zzh|枣庄|ZEK|

zaozhuang|zz|525@zzh|资中|ZZW|zizhong|zz|526@zzh|株洲|ZZQ|zhuzhou|zz|527@zzx|枣庄西|ZFK|

zaozhuangxi|zzx|528@aax|昂昂溪|AAX|angangxi|aax|529@ach|阿城|ACB|acheng|ac|530@ada|安达|ADX|

anda|ad|531@ade|安德|ARW|ande|ad|532@adi|安定|ADP|anding|ad|533@agu|安广|AGT|anguang|ag|

534@ahe|艾河|AHP|aihe|ah|535@ahu|安化|PKQ|anhua|ah|536@ajc|艾家村|AJJ|aijiacun|ajc|537@aji|鳌江

|ARH|aojiang|aj|538@aji|安家|AJB|anjia|aj|539@aji|阿金|AJD|ajin|aj|540@akt|阿克陶|AER|aketao|

akt|541@aky|安口窑|AYY|ankouyao|aky|542@alg|敖力布告|ALD|aolibugao|albg|543@alo|安龙|AUZ|

anlong|al|544@als|阿龙山|ASX|alongshan|als|545@alu|安陆|ALN|anlu|al|546@ame|阿木尔|JTX|amuer|

ame|547@anz|阿南庄|AZM|ananzhuang|anz|548@aqx|安庆西|APH|anqingxi|aqx|549@asx|鞍山西|AXT|

anshanxi|asx|550@ata|安塘|ATV|antang|at|551@atb|安亭北|ASH|antingbei|atb|552@ats|阿图什|ATR|

atushi|ats|553@atu|安图|ATL|antu|at|554@axi|安溪|AXS|anxi|ax|555@bao|博鳌|BWQ|boao|ba|556@bbe|

北碚|BPW|beibei|bb|557@bbg|白壁关|BGV|baibiguan|bbg|558@bbn|蚌埠南|BMH|bengbunan|bbn|559@bch|巴

楚|BCR|bachu|bc|560@bch|板城|BUP|bancheng|bc|561@bdh|北戴河|BEP|beidaihe|bdh|562@bdi|保定|BDP|

baoding|bd|563@bdi|宝坻|BPP|baodi|bd|564@bdl|八达岭|ILP|badaling|bdl|565@bdo|巴东|BNN|badong|

bd|566@bgu|柏果|BGM|baiguo|bg|567@bha|布海|BUT|buhai|bh|568@bhd|白河东|BIY|baihedong|bhd|

569@bho|贲红|BVC|benhong|bh|570@bhs|宝华山|BWH|baohuashan|bhs|571@bhx|白河县|BEY|baihexian|

bhx|572@bjg|白芨沟|BJJ|baijigou|bjg|573@bjg|碧鸡关|BJM|bijiguan|bjg|574@bji|北滘|IBQ|beijiao|

bj|575@bji|碧江|BLQ|bijiang|bj|576@bjp|白鸡坡|BBM|baijipo|bjp|577@bjs|笔架山|BSB|bijiashan|

bjs|578@bjt|八角台|BTD|bajiaotai|bjt|579@bka|保康|BKD|baokang|bk|580@bkp|白奎堡|BKB|baikuipu|

bkp|581@bla|白狼|BAT|bailang|bl|582@bla|百浪|BRZ|bailang|bl|583@ble|博乐|BOR|bole|bl|584@blg|宝

拉格|BQC|baolage|blg|585@bli|巴林|BLX|balin|bl|586@bli|宝林|BNB|baolin|bl|587@bli|北流|BOZ|

beiliu|bl|588@bli|勃利|BLB|boli|bl|589@blk|布列开|BLR|buliekai|blk|590@bls|宝龙山|BND|

baolongshan|bls|591@blx|百里峡|AAP|bailixia|blx|592@bmc|八面城|BMD|bamiancheng|bmc|593@bmq|班猫

箐|BNM|banmaoqing|bmq|594@bmt|八面通|BMB|bamiantong|bmt|595@bmz|北马圈子|BRP|beimaquanzi|bmqz|

596@bpn|北票南|RPD|beipiaonan|bpn|597@bqi|白旗|BQP|baiqi|bq|598@bql|宝泉岭|BQB|baoquanling|

bql|599@bqu|白泉|BQL|baiquan|bq|600@bsh|巴山|BAY|bashan|bs|601@bsh|白沙|BSW|baisha|bs|602@bsj|

白水江|BSY|baishuijiang|bsj|603@bsp|白沙坡|BPM|baishapo|bsp|604@bss|白石山|BAL|baishishan|bss|

605@bsz|白水镇|BUM|baishuizhen|bsz|606@btd|包头 东|FDC|baotoudong|btd|607@bti|坂田|BTQ|

bantian|bt|608@bto|泊头|BZP|botou|bt|609@btu|北屯|BYP|beitun|bt|610@bxh|本溪湖|BHT|benxihu|

bxh|611@bxi|博兴|BXK|boxing|bx|612@bxt|八仙筒|VXD|baxiantong|bxt|613@byg|白音察干|BYC|

baiyinchagan|bycg|614@byh|背荫河|BYB|beiyinhe|byh|615@byi|北营|BIV|beiying|by|616@byl|巴彦高

勒|BAC|bayangaole|bygl|617@byl|白音他拉|BID|baiyintala|bytl|618@byq|鲅鱼圈|BYT|bayuquan|byq|

619@bys|白银市|BNJ|baiyinshi|bys|620@bys|白音胡硕|BCD|baiyinhushuo|byhs|621@bzh|巴中|IEW|

bazhong|bz|622@bzh|霸州|RMP|bazhou|bz|623@bzh|北宅|BVP|beizhai|bz|624@cbb|赤壁北|CIN|chibibei|

cbb|625@cbg|查布嘎|CBC|chabuga|cbg|626@cch|长城|CEJ|changcheng|cc|627@cch|长冲|CCM|changchong|

cc|628@cdd|承德东|CCP|chengdedong|cdd|629@cfx|赤峰西|CID|chifengxi|cfx|630@cga|嵯岗|CAX|

cuogang|cg|631@cga|柴岗|CGT|chaigang|cg|632@cge|长葛|CEF|changge|cg|633@cgp|柴沟堡|CGV|

chaigoupu|cgp|634@cgu|城固|CGY|chenggu|cg|635@cgy|陈官营|CAJ|chenguanying|cgy|636@cgz|成高子|

CZB|chenggaozi|cgz|637@cha|草海|WBW|caohai|ch|638@che|柴河|CHB|chaihe|ch|639@che|册亨|CHZ|

ceheng|ch|640@chk|草河口|CKT|caohekou|chk|641@chk|崔黄口|CHP|cuihuangkou|chk|642@chu|巢湖|CIH|

chaohu|ch|643@cjg|蔡家沟|CJT|caijiagou|cjg|644@cjh|成吉思汗|CJX|chengjisihan|cjsh|645@cji|岔

江|CAM|chajiang|cj|646@cjp|蔡家坡|CJY|caijiapo|cjp|647@cle|昌乐|CLK|changle|cl|648@clg|超梁沟|

CYP|chaolianggou|clg|649@cli|慈利|CUQ|cili|cl|650@cli|昌黎|CLP|changli|cl|651@clz|长岭子|CLT|

changlingzi|clz|652@cmi|晨明|CMB|chenming|cm|653@cno|长农|CNJ|changnong|cn|654@cpb|昌平北|VBP|

changpingbei|cpb|655@cpi|常平|DAQ|changping|cp|656@cpl|长坡岭|CPM|changpoling|cpl|657@cqi|辰

清|CQB|chenqing|cq|658@csh|蔡山|CON|caishan|cs|659@csh|楚山|CSB|chushan|cs|660@csh|长寿|EFW|

changshou|cs|661@csh|磁山|CSP|cishan|cs|662@csh|苍石|CST|cangshi|cs|663@csh|草市|CSL|caoshi|

cs|664@csq|察素齐|CSC|chasuqi|csq|665@cst|长山屯|CVT|changshantun|cst|666@cti|长汀|CES|

changting|ct|667@ctx|昌图西|CPT|changtuxi|ctx|668@cwa|春湾|CQQ|chunwan|cw|669@cxi|磁县|CIP|

cixian|cx|670@cxi|岑溪|CNZ|cenxi|cx|671@cxi|辰溪|CXQ|chenxi|cx|672@cxi|磁西|CRP|cixi|cx|

673@cxn|长兴南|CFH|changxingnan|cxn|674@cya|磁窑|CYK|ciyao|cy|675@cya|朝阳|CYD|chaoyang|cy|

676@cya|春阳|CAL|chunyang|cy|677@cya|城阳|CEK|chengyang|cy|678@cyc|创业村|CEX|chuangyecun|cyc|

679@cyc|朝阳川|CYL|chaoyangchuan|cyc|680@cyd|朝阳地|CDD|chaoyangdi|cyd|681@cyu|长垣|CYF|

changyuan|cy|682@cyz|朝阳镇|CZL|chaoyangzhen|cyz|683@czb|滁州北|CUH|chuzhoubei|czb|684@czb|常州

北|ESH|changzhoubei|czb|685@czh|滁州|CXH|chuzhou|cz|686@czh|潮州|CKQ|chaozhou|cz|687@czh|常庄|

CVK|changzhuang|cz|688@czl|曹子里|CFP|caozili|czl|689@czw|车转湾|CWM|chezhuanwan|czw|690@czx|郴

州西|ICQ|chenzhouxi|czx|691@czx|沧州西|CBP|cangzhouxi|czx|692@dan|德安|DAG|dean|da|693@dan|大安

|RAT|daan|da|694@dba|大坝|DBJ|daba|db|695@dba|大板|DBC|daban|db|696@dba|大巴|DBD|daba|db|

697@dba|到保|RBT|daobao|db|698@dbi|定边|DYJ|dingbian|db|699@dbj|东边井|DBB|dongbianjing|dbj|

700@dbs|德伯斯|RDT|debosi|dbs|701@dcg|打柴沟|DGJ|dachaigou|dcg|702@dch|德昌|DVW|dechang|dc|

703@dda|滴道|DDB|didao|dd|704@ddg|大磴沟|DKJ|dadenggou|ddg|705@ded|刀尔登|DRD|daoerdeng|ded|

706@dee|得耳布尔|DRX|deerbuer|debe|707@dfa|东方|UFQ|dongfang|df|708@dfe|丹凤|DGY|danfeng|df|

709@dfe|东丰|DIL|dongfeng|df|710@dge|都格|DMM|duge|dg|711@dgt|大官屯|DTT|daguantun|dgt|712@dgu|

大关|RGW|daguan|dg|713@dgu|东光|DGP|dongguang|dg|714@dha|东海|DHB|donghai|dh|715@dhc|大灰厂|

DHP|dahuichang|dhc|716@dhq|大红旗|DQD|dahongqi|dhq|717@dht|大禾塘|SOQ|shaodong|dh|718@dhx|东海

县|DQH|donghaixian|dhx|719@dhx|德惠西|DXT|dehuixi|dhx|720@djg|达家沟|DJT|dajiagou|djg|721@dji|

东津|DKB|dongjin|dj|722@dji|杜家|DJL|dujia|dj|723@dkt|大口屯|DKP|dakoutun|dkt|724@dla|东来|

RVD|donglai|dl|725@dlh|德令哈|DHO|delingha|dlh|726@dlh|大陆号|DLC|daluhao|dlh|727@dli|带岭|

DLB|dailing|dl|728@dli|大林|DLD|dalin|dl|729@dlq|达拉特旗|DIC|dalateqi|dltq|730@dlt|独立屯|

DTX|dulitun|dlt|731@dlu|豆罗|DLV|douluo|dl|732@dlx|达拉特西|DNC|dalatexi|dltx|733@dmc|东明村|

DMD|dongmingcun|dmc|734@dmh|洞庙河|DEP|dongmiaohe|dmh|735@dmx|东明县|DNF|dongmingxian|dmx|

736@dni|大拟|DNZ|dani|dn|737@dpf|大平房|DPD|dapingfang|dpf|738@dps|大盘石|RPP|dapanshi|dps|

739@dpu|大埔|DPI|dapu|dp|740@dpu|大堡|DVT|dapu|dp|741@dqd|大庆东|LFX|daqingdong|dqd|742@dqh|大

其拉哈|DQX|daqilaha|dqlh|743@dqi|道清|DML|daoqing|dq|744@dqs|对青山|DQB|duiqingshan|dqs|

745@dqx|德清西|MOH|deqingxi|dqx|746@dqx|大庆西|RHX|daqingxi|dqx|747@dsh|东升|DRQ|dongsheng|ds|

748@dsh|砀山|DKH|dangshan|ds|749@dsh|独山|RWW|dushan|ds|750@dsh|登沙河|DWT|dengshahe|dsh|

751@dsp|读书铺|DPM|dushupu|dsp|752@dst|大石头|DSL|dashitou|dst|753@dsx|东胜西|DYC|dongshengxi|

dsx|754@dsz|大石寨|RZT|dashizhai|dsz|755@dta|东台|DBH|dongtai|dt|756@dta|定陶|DQK|dingtao|dt|

757@dta|灯塔|DGT|dengta|dt|758@dtb|大田边|DBM|datianbian|dtb|759@dth|东通化|DTL|dongtonghua|

dth|760@dtu|丹徒|RUH|dantu|dt|761@dtu|大屯|DNT|datun|dt|762@dwa|东湾|DRJ|dongwan|dw|763@dwk|大

武口|DFJ|dawukou|dwk|764@dwp|低窝铺|DWJ|diwopu|dwp|765@dwt|大王滩|DZZ|dawangtan|dwt|766@dwz|大

湾子|DFM|dawanzi|dwz|767@dxg|大兴沟|DXL|daxinggou|dxg|768@dxi|大兴|DXX|daxing|dx|769@dxi|定西|

DSJ|dingxi|dx|770@dxi|甸心|DXM|dianxin|dx|771@dxi|东乡|DXG|dongxiang|dx|772@dxi|代县|DKV|

daixian|dx|773@dxi|定襄|DXV|dingxiang|dx|774@dxu|东戌|RXP|dongxu|dx|775@dxz|东辛庄|DXD|

dongxinzhuang|dxz|776@dya|丹阳|DYH|danyang|dy|777@dya|德阳|DYW|deyang|dy|778@dya|大雁|DYX|

dayan|dy|779@dya|当阳|DYN|dangyang|dy|780@dyb|丹阳北|EXH|danyangbei|dyb|781@dyd|大英东|IAW|

dayingdong|dyd|782@dyd|东淤地|DBV|dongyudi|dyd|783@dyi|大营|DYV|daying|dy|784@dyu|定远|EWH|

dingyuan|dy|785@dyu|岱岳|RYV|daiyue|dy|786@dyu|大元|DYZ|dayuan|dy|787@dyz|大营镇|DJP|

dayingzhen|dyz|788@dyz|大营子|DZD|dayingzi|dyz|789@dzc|大战场|DTJ|dazhanchang|dzc|790@dzd|德州

东|DIP|dezhoudong|dzd|791@dzh|东至|DCH|dongzhi|dz|792@dzh|低庄|DVQ|dizhuang|dz|793@dzh|东镇|

DNV|dongzhen|dz|794@dzh|道州|DFZ|daozhou|dz|795@dzh|东庄|DZV|dongzhuang|dz|796@dzh|兑镇|DWV|

duizhen|dz|797@dzh|豆庄|ROP|douzhuang|dz|798@dzh|定州|DXP|dingzhou|dz|799@dzy|大竹园|DZY|

dazhuyuan|dzy|800@dzz|大杖子|DAP|dazhangzi|dzz|801@dzz|豆张庄|RZP|douzhangzhuang|dzz|802@ebi|峨

边|EBW|ebian|eb|803@edm|二道沟门|RDP|erdaogoumen|edgm|804@edw|二道湾|RDX|erdaowan|edw|805@ees|

鄂尔多斯|EEC|eerduosi|eeds|806@elo|二龙|RLD|erlong|el|807@elt|二龙山屯|ELA|erlongshantun|elst|

808@eme|峨眉|EMW|emei|em|809@emh|二密河|RML|ermihe|emh|810@eyi|二营|RYJ|erying|ey|811@ezh|鄂

州|ECN|ezhou|ez|812@fan|福安|FAS|fuan|fa|813@fch|丰城|FCG|fengcheng|fc|814@fcn|丰城南|FNG|

fengchengnan|fcn|815@fdo|肥东|FIH|feidong|fd|816@fer|发耳|FEM|faer|fe|817@fha|富海|FHX|fuhai|

fh|818@fha|福海|FHR|fuhai|fh|819@fhc|凤凰城|FHT|fenghuangcheng|fhc|820@fhe|汾河|FEV|fenhe|fh|

821@fhu|奉化|FHH|fenghua|fh|822@fji|富锦|FIB|fujin|fj|823@fjt|范家屯|FTT|fanjiatun|fjt|824@flq|

福利区|FLJ|fuliqu|flq|825@flt|福利屯|FTB|fulitun|flt|826@flz|丰乐镇|FZB|fenglezhen|flz|827@fna|

阜南|FNH|funan|fn|828@fni|阜宁|AKH|funing|fn|829@fni|抚宁|FNP|funing|fn|830@fqi|福清|FQS|

fuqing|fq|831@fqu|福泉|VMW|fuquan|fq|832@fsc|丰水村|FSJ|fengshuicun|fsc|833@fsh|丰顺|FUQ|

fengshun|fs|834@fsh|繁峙|FSV|fanshi|fs|835@fsh|抚顺|FST|fushun|fs|836@fsk|福山口|FKP|

fushankou|fsk|837@fsu|扶绥|FSZ|fusui|fs|838@ftu|冯屯|FTX|fengtun|ft|839@fty|浮图峪|FYP|futuyu|

fty|840@fxd|富县东|FDY|fuxiandong|fxd|841@fxi|凤县|FXY|fengxian|fx|842@fxi|富县|FEY|fuxian|fx|

843@fxi|费县|FXK|feixian|fx|844@fya|凤阳|FUH|fengyang|fy|845@fya|汾阳|FAV|fenyang|fy|846@fyb|扶

余北|FBT|fuyubei|fyb|847@fyi|分宜|FYG|fenyi|fy|848@fyu|富源|FYM|fuyuan|fy|849@fyu|扶余|FYT|

fuyu|fy|850@fyu|富裕|FYX|fuyu|fy|851@fzb|抚州北|FBG|fuzhoubei|fzb|852@fzh|凤州|FZY|fengzhou|

fz|853@fzh|丰镇|FZC|fengzhen|fz|854@fzh|范镇|VZK|fanzhen|fz|855@gan|固安|GFP|guan|ga|856@gan|广

安|VJW|guangan|ga|857@gbd|高碑店|GBP|gaobeidian|gbd|858@gbz|沟帮子|GBD|goubangzi|gbz|859@gcd|甘

草店|GDJ|gancaodian|gcd|860@gch|谷城|GCN|gucheng|gc|861@gch|藁城|GEP|gaocheng|gc|862@gcu|高村|

GCV|gaocun|gc|863@gcz|古城镇|GZB|guchengzhen|gcz|864@gde|广德|GRH|guangde|gd|865@gdi|贵定|GTW|

guiding|gd|866@gdn|贵定南|IDW|guidingnan|gdn|867@gdo|古东|GDV|gudong|gd|868@gga|贵港|GGZ|

guigang|gg|869@gga|官高|GVP|guangao|gg|870@ggm|葛根庙|GGT|gegenmiao|ggm|871@ggo|干沟|GGL|

gangou|gg|872@ggu|甘谷|GGJ|gangu|gg|873@ggz|高各庄|GGP|gaogezhuang|ggz|874@ghe|甘河|GAX|ganhe|

gh|875@ghe|根河|GEX|genhe|gh|876@gjd|郭家店|GDT|guojiadian|gjd|877@gjz|孤家子|GKT|gujiazi|gjz|

878@gla|古浪|GLJ|gulang|gl|879@gla|皋兰|GEJ|gaolan|gl|880@glf|高楼房|GFM|gaoloufang|glf|

881@glh|归流河|GHT|guiliuhe|glh|882@gli|关林|GLF|guanlin|gl|883@glu|甘洛|VOW|ganluo|gl|884@glz|

郭磊庄|GLP|guoleizhuang|glz|885@gmi|高密|GMK|gaomi|gm|886@gmz|公庙子|GMC|gongmiaozi|gmz|

887@gnh|工农湖|GRT|gongnonghu|gnh|888@gnn|广宁寺南|GNT|guangningsinan|gnn|889@gnw|广南卫|GNM|

guangnanwei|gnw|890@gpi|高平|GPF|gaoping|gp|891@gqb|甘泉北|GEY|ganquanbei|gqb|892@gqc|共青城|

GAG|gongqingcheng|gqc|893@gqk|甘旗卡|GQD|ganqika|gqk|894@gqu|甘泉|GQY|ganquan|gq|895@gqz|高桥镇

|GZD|gaoqiaozhen|gqz|896@gsh|灌水|GST|guanshui|gs|897@gsh|赶水|GSW|ganshui|gs|898@gsk|孤山口|

GSP|gushankou|gsk|899@gso|果松|GSL|guosong|gs|900@gsz|高山子|GSD|gaoshanzi|gsz|901@gsz|嘎什甸子

|GXD|gashidianzi|gsdz|902@gta|高台|GTJ|gaotai|gt|903@gta|高滩|GAY|gaotan|gt|904@gti|古田|GTS|

gutian|gt|905@gti|官厅|GTP|guanting|gt|906@gtx|官厅西|KEP|guantingxi|gtx|907@gxi|贵溪|GXG|

guixi|gx|908@gya|涡阳|GYH|guoyang|gy|909@gyi|巩义|GXF|gongyi|gy|910@gyi|高邑|GIP|gaoyi|gy|

911@gyn|巩义南|GYF|gongyinan|gyn|912@gyn|广元南|GAW|guangyuannan|gyn|913@gyu|固原|GUJ|guyuan|

gy|914@gyu|菇园|GYL|guyuan|gy|915@gyz|公营子|GYD|gongyingzi|gyz|916@gze|光泽|GZS|guangze|gz|

917@gzh|古镇|GNQ|guzhen|gz|918@gzh|固镇|GEH|guzhen|gz|919@gzh|虢镇|GZY|guozhen|gz|920@gzh|瓜

州|GZJ|guazhou|gz|921@gzh|高州|GSQ|gaozhou|gz|922@gzh|盖州|GXT|gaizhou|gz|923@gzj|官字井|GOT|

guanzijing|gzj|924@gzp|革镇堡|GZT|gezhenpu|gzp|925@gzs|冠豸山|GSS|guanzhaishan|gzs|926@gzx|盖州

西|GAT|gaizhouxi|gzx|927@han|淮安南|AMH|huaiannan|han|928@han|红安|HWN|hongan|ha|929@hax|海安县

|HIH|haianxian|hax|930@hax|红安西|VXN|honganxi|hax|931@hba|黄柏|HBL|huangbai|hb|932@hbe|海北|

HEB|haibei|hb|933@hbi|鹤壁|HAF|hebi|hb|934@hcb|会昌北|XEG|huichangbei|hcb|935@hch|华城|VCQ|

huacheng|hc|936@hch|河唇|HCZ|hechun|hc|937@hch|汉川|HCN|hanchuan|hc|938@hch|海城|HCT|haicheng|

hc|939@hch|合川|WKW|hechuan|hc|940@hct|黑冲滩|HCJ|heichongtan|hct|941@hcu|黄村|HCP|huangcun|

hc|942@hcx|海城西|HXT|haichengxi|hcx|943@hde|化德|HGC|huade|hd|944@hdo|洪洞|HDV|hongtong|hd|

945@hes|霍尔果斯|HFR|huoerguosi|hegs|946@hfe|横峰|HFG|hengfeng|hf|947@hfw|韩府湾|HXJ|hanfuwan|

hfw|948@hgu|汉沽|HGP|hangu|hg|949@hgy|黄瓜园|HYM|huangguayuan|hgy|950@hgz|红光镇|IGW|

hongguangzhen|hgz|951@hhe|浑河|HHT|hunhe|hh|952@hhg|红花沟|VHD|honghuagou|hhg|953@hht|黄花筒|

HUD|huanghuatong|hht|954@hjd|贺家店|HJJ|hejiadian|hjd|955@hji|和静|HJR|hejing|hj|956@hji|红江|

HFM|hongjiang|hj|957@hji|黑井|HIM|heijing|hj|958@hji|获嘉|HJF|huojia|hj|959@hji|河津|HJV|

hejin|hj|960@hji|涵江|HJS|hanjiang|hj|961@hji|华家|HJT|huajia|hj|962@hjq|杭锦后旗|HDC|

hangjinhouqi|hjhq|963@hjx|河间西|HXP|hejianxi|hjx|964@hjz|花家庄|HJM|huajiazhuang|hjz|965@hkn|

河口南|HKJ|hekounan|hkn|966@hko|黄口|KOH|huangkou|hk|967@hko|湖口|HKG|hukou|hk|968@hla|呼兰|

HUB|hulan|hl|969@hlb|葫芦岛北|HPD|huludaobei|hldb|970@hlh|浩良河|HHB|haolianghe|hlh|971@hlh|哈

拉海|HIT|halahai|hlh|972@hli|鹤立|HOB|heli|hl|973@hli|桦林|HIB|hualin|hl|974@hli|黄陵|ULY|

huangling|hl|975@hli|海林|HRB|hailin|hl|976@hli|虎林|VLB|hulin|hl|977@hli|寒岭|HAT|hanling|hl|

978@hlo|和龙|HLL|helong|hl|979@hlo|海龙|HIL|hailong|hl|980@hls|哈拉苏|HAX|halasu|hls|981@hlt|呼

鲁斯太|VTJ|hulusitai|hlst|982@hlz|火连寨|HLT|huolianzhai|hlz|983@hme|黄梅|VEH|huangmei|hm|

984@hmy|韩麻营|HYP|hanmaying|hmy|985@hnh|黄泥河|HHL|huangnihe|hnh|986@hni|海宁|HNH|haining|hn|

987@hno|惠农|HMJ|huinong|hn|988@hpi|和平|VAQ|heping|hp|989@hpz|花棚子|HZM|huapengzi|hpz|

990@hqi|花桥|VQH|huaqiao|hq|991@hqi|宏庆|HEY|hongqing|hq|992@hre|怀仁|HRV|huairen|hr|993@hro|华

容|HRN|huarong|hr|994@hsb|华山北|HDY|huashanbei|hsb|995@hsd|黄松甸|HDL|huangsongdian|hsd|

996@hsg|和什托洛盖|VSR|heshituoluogai|hstlg|997@hsh|红山|VSB|hongshan|hs|998@hsh|汉寿|VSQ|

hanshou|hs|999@hsh|衡山|HSQ|hengshan|hs|1000@hsh|黑水|HOT|heishui|hs|1001@hsh|惠山|VCH|

huishan|hs|1002@hsh|虎什哈|HHP|hushiha|hsh|1003@hsp|红寺堡|HSJ|hongsipu|hsp|1004@hst|虎石台|

HUT|hushitai|hst|1005@hsw|海石湾|HSO|haishiwan|hsw|1006@hsx|衡山西|HEQ|hengshanxi|hsx|1007@hsx|

红砂岘|VSJ|hongshaxian|hsx|1008@hta|黑台|HQB|heitai|ht|1009@hta|桓台|VTK|huantai|ht|1010@hti|和

田|VTR|hetian|ht|1011@hto|会同|VTQ|huitong|ht|1012@htz|海坨子|HZT|haituozi|htz|1013@hwa|黑旺|

HWK|heiwang|hw|1014@hwa|海湾|RWH|haiwan|hw|1015@hxi|红星|VXB|hongxing|hx|1016@hxi|徽县|HYY|

huixian|hx|1017@hxl|红兴隆|VHB|hongxinglong|hxl|1018@hxt|换新天|VTB|huanxintian|hxt|1019@hxt|红

岘台|HTJ|hongxiantai|hxt|1020@hya|红彦|VIX|hongyan|hy|1021@hya|合阳|HAY|heyang|hy|1022@hya|海阳

|HYK|haiyang|hy|1023@hyd|衡阳东|HVQ|hengyangdong|hyd|1024@hyi|华蓥|HUW|huaying|hy|1025@hyi|汉阴

|HQY|hanyin|hy|1026@hyt|黄羊滩|HGJ|huangyangtan|hyt|1027@hyu|汉源|WHW|hanyuan|hy|1028@hyu|河

源|VIQ|heyuan|hy|1029@hyu|花园|HUN|huayuan|hy|1030@hyu|湟源|HNO|huangyuan|hy|1031@hyz|黄羊镇|

HYJ|huangyangzhen|hyz|1032@hzh|湖州|VZH|huzhou|hz|1033@hzh|化州|HZZ|huazhou|hz|1034@hzh|黄州|

VON|huangzhou|hz|1035@hzh|霍州|HZV|huozhou|hz|1036@hzx|惠州西|VXQ|huizhouxi|hzx|1037@jba|巨宝|

JRT|jubao|jb|1038@jbi|靖边|JIY|jingbian|jb|1039@jbt|金宝屯|JBD|jinbaotun|jbt|1040@jcb|晋城北|

JEF|jinchengbei|jcb|1041@jch|金昌|JCJ|jinchang|jc|1042@jch|鄄城|JCK|juancheng|jc|1043@jch|交

城|JNV|jiaocheng|jc|1044@jch|建昌|JFD|jianchang|jc|1045@jde|峻德|JDB|junde|jd|1046@jdi|井店|

JFP|jingdian|jd|1047@jdo|鸡东|JOB|jidong|jd|1048@jdu|江都|UDH|jiangdu|jd|1049@jgs|鸡冠山|JST|

jiguanshan|jgs|1050@jgt|金沟屯|VGP|jingoutun|jgt|1051@jha|静海|JHP|jinghai|jh|1052@jhe|金河|

JHX|jinhe|jh|1053@jhe|锦河|JHB|jinhe|jh|1054@jhe|精河|JHR|jinghe|jh|1055@jhn|精河南|JIR|

jinghenan|jhn|1056@jhu|江华|JHZ|jianghua|jh|1057@jhu|建湖|AJH|jianhu|jh|1058@jjg|纪家沟|VJD|

jijiagou|jjg|1059@jji|晋江|JJS|jinjiang|jj|1060@jji|姜家|JJB|jiangjia|jj|1061@jji|江津|JJW|

jiangjin|jj|1062@jke|金坑|JKT|jinkeng|jk|1063@jli|芨岭|JLJ|jiling|jl|1064@jmc|金马村|JMM|

jinmacun|jmc|1065@jmd|江门东|JWQ|jiangmendong|jmd|1066@jme|角美|JES|jiaomei|jm|1067@jna|莒南|

JOK|junan|jn|1068@jna|井南|JNP|jingnan|jn|1069@jou|建瓯|JVS|jianou|jo|1070@jpe|经棚|JPC|

jingpeng|jp|1071@jqi|江桥|JQX|jiangqiao|jq|1072@jsa|九三|SSX|jiusan|js|1073@jsb|金山北|EGH|

jinshanbei|jsb|1074@jsh|嘉善|JSH|jiashan|js|1075@jsh|京山|JCN|jingshan|js|1076@jsh|建始|JRN|

jianshi|js|1077@jsh|稷山|JVV|jishan|js|1078@jsh|吉舒|JSL|jishu|js|1079@jsh|建设|JET|jianshe|

js|1080@jsh|甲山|JOP|jiashan|js|1081@jsj|建三江|JIB|jiansanjiang|jsj|1082@jsn|嘉善南|EAH|

jiashannan|jsn|1083@jst|金山屯|JTB|jinshantun|jst|1084@jst|江所田|JOM|jiangsuotian|jst|

1085@jta|景泰|JTJ|jingtai|jt|1086@jtn|九台南|JNL|jiutainan|jtn|1087@jwe|吉文|JWX|jiwen|jw|

1088@jxi|进贤|JUG|jinxian|jx|1089@jxi|莒县|JKK|juxian|jx|1090@jxi|嘉祥|JUK|jiaxiang|jx|

1091@jxi|介休|JXV|jiexiu|jx|1092@jxi|嘉兴|JXH|jiaxing|jx|1093@jxi|井陉|JJP|jingxing|jx|

1094@jxn|嘉兴南|EPH|jiaxingnan|jxn|1095@jxz|夹心子|JXT|jiaxinzi|jxz|1096@jya|姜堰|UEH|

jiangyan|jy|1097@jya|揭阳|JRQ|jieyang|jy|1098@jya|建阳|JYS|jianyang|jy|1099@jya|简阳|JYW|

jianyang|jy|1100@jye|巨野|JYK|juye|jy|1101@jyo|江永|JYZ|jiangyong|jy|1102@jyu|缙云|JYH|jinyun|

jy|1103@jyu|靖远|JYJ|jingyuan|jy|1104@jyu|江源|SZL|jiangyuan|jy|1105@jyu|济源|JYF|jiyuan|jy|

1106@jyx|靖远西|JXJ|jingyuanxi|jyx|1107@jzb|胶州北|JZK|jiaozhoubei|jzb|1108@jzd|焦作东|WEF|

jiaozuodong|jzd|1109@jzh|金寨|JZH|jinzhai|jz|1110@jzh|靖州|JEQ|jingzhou|jz|1111@jzh|荆州|JBN|

jingzhou|jz|1112@jzh|胶州|JXK|jiaozhou|jz|1113@jzh|晋州|JXP|jinzhou|jz|1114@jzn|锦州南|JOD|

jinzhounan|jzn|1115@jzu|焦作|JOF|jiaozuo|jz|1116@jzw|旧庄窝|JVP|jiuzhuangwo|jzw|1117@jzz|金杖子

|JYD|jinzhangzi|jzz|1118@kan|开安|KAT|kaian|ka|1119@kch|库车|KCR|kuche|kc|1120@kch|康城|KCP|

kangcheng|kc|1121@kde|库都尔|KDX|kuduer|kde|1122@kdi|宽甸|KDT|kuandian|kd|1123@kdo|克东|KOB|

kedong|kd|1124@kdz|昆都仑召|KDC|kundulunzhao|kdlz|1125@kji|开江|KAW|kaijiang|kj|1126@kjj|康金井

|KJB|kangjinjing|kjj|1127@klq|喀喇其|KQX|kalaqi|klq|1128@klu|开鲁|KLC|kailu|kl|1129@kly|克拉玛

依|KHR|kelamayi|klmy|1130@kqi|口前|KQL|kouqian|kq|1131@ksh|昆山|KSH|kunshan|ks|1132@ksh|奎山|

KAB|kuishan|ks|1133@ksh|克山|KSB|keshan|ks|1134@kto|开通|KTT|kaitong|kt|1135@kxl|康熙岭|KXZ|

kangxiling|kxl|1136@kya|昆阳|KAM|kunyang|ky|1137@kyh|克一河|KHX|keyihe|kyh|1138@kyx|开原西|

KXT|kaiyuanxi|kyx|1139@kzh|康庄|KZP|kangzhuang|kz|1140@lbi|来宾|UBZ|laibin|lb|1141@lbi|老边|

LLT|laobian|lb|1142@lbx|灵宝西|LPF|lingbaoxi|lbx|1143@lch|龙川|LUQ|longchuan|lc|1144@lch|乐昌|

LCQ|lechang|lc|1145@lch|黎城|UCP|licheng|lc|1146@lch|聊城|UCK|liaocheng|lc|1147@lcu|蓝村|LCK|

lancun|lc|1148@lda|两当|LDY|liangdang|ld|1149@ldo|林东|LRC|lindong|ld|1150@ldu|乐都|LDO|ledu|

ld|1151@ldx|梁底下|LDP|liangdixia|ldx|1152@ldz|六道河子|LVP|liudaohezi|ldhz|1153@lfa|鲁番|LVM|

lufan|lf|1154@lfa|廊坊|LJP|langfang|lf|1155@lfa|落垡|LOP|luofa|lf|1156@lfb|廊坊北|LFP|

langfangbei|lfb|1157@lfu|老府|UFD|laofu|lf|1158@lga|兰岗|LNB|langang|lg|1159@lgd|龙骨甸|LGM|

longgudian|lgd|1160@lgo|芦沟|LOM|lugou|lg|1161@lgo|龙沟|LGJ|longgou|lg|1162@lgu|拉古|LGB|lagu|

lg|1163@lha|临海|UFH|linhai|lh|1164@lha|林海|LXX|linhai|lh|1165@lha|拉哈|LHX|laha|lh|1166@lha|

凌海|JID|linghai|lh|1167@lhe|柳河|LNL|liuhe|lh|1168@lhe|六合|KLH|liuhe|lh|1169@lhu|龙华|LHP|

longhua|lh|1170@lhy|滦河沿|UNP|luanheyan|lhy|1171@lhz|六合镇|LEX|liuhezhen|lhz|1172@ljd|亮甲

店|LRT|liangjiadian|ljd|1173@ljd|刘家店|UDT|liujiadian|ljd|1174@ljh|刘家河|LVT|liujiahe|ljh|

1175@lji|连江|LKS|lianjiang|lj|1176@lji|庐江|UJH|lujiang|lj|1177@lji|李家|LJB|lijia|lj|

1178@lji|罗江|LJW|luojiang|lj|1179@lji|廉江|LJZ|lianjiang|lj|1180@lji|两家|UJT|liangjia|lj|

1181@lji|龙江|LJX|longjiang|lj|1182@lji|龙嘉|UJL|longjia|lj|1183@ljk|莲江口|LHB|lianjiangkou|

ljk|1184@ljl|蔺家楼|ULK|linjialou|ljl|1185@ljp|李家坪|LIJ|lijiaping|ljp|1186@lka|兰考|LKF|

lankao|lk|1187@lko|林口|LKB|linkou|lk|1188@lkp|路口铺|LKQ|lukoupu|lkp|1189@lla|老莱|LAX|

laolai|ll|1190@lli|拉林|LAB|lalin|ll|1191@lli|陆良|LRM|luliang|ll|1192@lli|龙里|LLW|longli|ll|

1193@lli|临澧|LWQ|linli|ll|1194@lli|兰棱|LLB|lanling|ll|1195@lli|零陵|UWZ|lingling|ll|1196@llo|

卢龙|UAP|lulong|ll|1197@lmd|喇嘛甸|LMX|lamadian|lmd|1198@lmd|里木店|LMB|limudian|lmd|1199@lme|

洛门|LMJ|luomen|lm|1200@lna|龙南|UNG|longnan|ln|1201@lpi|梁平|UQW|liangping|lp|1202@lpi|罗平|

LPM|luoping|lp|1203@lpl|落坡岭|LPP|luopoling|lpl|1204@lps|六盘山|UPJ|liupanshan|lps|1205@lps|乐

平市|LPG|lepingshi|lps|1206@lqi|临清|UQK|linqing|lq|1207@lqs|龙泉寺|UQJ|longquansi|lqs|

1208@lsb|乐山北|UTW|leshanbei|ls|1209@lsc|乐善村|LUM|leshancun|lsc|1210@lsd|冷水江东|UDQ|

lengshuijiangdong|lsjd|1211@lsg|连山关|LGT|lianshanguan|lsg|1212@lsg|流水沟|USP|liushuigou|

lsg|1213@lsh|陵水|LIQ|lingshui|ls|1214@lsh|丽水|USH|lishui|ls|1215@lsh|罗山|LRN|luoshan|ls|

1216@lsh|鲁山|LAF|lushan|ls|1217@lsh|梁山|LMK|liangshan|ls|1218@lsh|灵石|LSV|lingshi|ls|

1219@lsh|露水河|LUL|lushuihe|lsh|1220@lsh|庐山|LSG|lushan|ls|1221@lsp|林盛堡|LBT|linshengpu|

lsp|1222@lst|柳树屯|LSD|liushutun|lst|1223@lsz|龙山镇|LAS|longshanzhen|lsz|1224@lsz|梨树镇|

LSB|lishuzhen|lsz|1225@lsz|李石寨|LET|lishizhai|lsz|1226@lta|黎塘|LTZ|litang|lt|1227@lta|轮台|

LAR|luntai|lt|1228@lta|芦台|LTP|lutai|lt|1229@ltb|龙塘坝|LBM|longtangba|ltb|1230@ltu|濑湍|LVZ|

laituan|lt|1231@ltx|骆驼巷|LTJ|luotuoxiang|ltx|1232@lwa|李旺|VLJ|liwang|lw|1233@lwd|莱芜东|

LWK|laiwudong|lwd|1234@lws|狼尾山|LRJ|langweishan|lws|1235@lwu|灵武|LNJ|lingwu|lw|1236@lwx|莱芜

西|UXK|laiwuxi|lwx|1237@lxi|朗乡|LXB|langxiang|lx|1238@lxi|陇县|LXY|longxian|lx|1239@lxi|临湘|

LXQ|linxiang|lx|1240@lxi|芦溪|LUG|luxi|lx|1241@lxi|莱西|LXK|laixi|lx|1242@lxi|林西|LXC|linxi|

lx|1243@lxi|滦县|UXP|luanxian|lx|1244@lya|略阳|LYY|lueyang|ly|1245@lya|莱阳|LYK|laiyang|ly|

1246@lya|辽阳|LYT|liaoyang|ly|1247@lyb|临沂北|UYK|linyibei|lyb|1248@lyd|凌源东|LDD|

lingyuandong|lyd|1249@lyg|连云港|UIH|lianyungang|lyg|1250@lyi|临颍|LNF|linying|ly|1251@lyi|老营

|LXL|laoying|ly|1252@lyo|龙游|LMH|longyou|ly|1253@lyu|罗源|LVS|luoyuan|ly|1254@lyu|林源|LYX|

linyuan|ly|1255@lyu|涟源|LAQ|lianyuan|ly|1256@lyu|涞源|LYP|laiyuan|ly|1257@lyx|耒阳西|LPQ|

leiyangxi|lyx|1258@lze|临泽|LEJ|linze|lz|1259@lzg|龙爪沟|LZT|longzhuagou|lzg|1260@lzh|雷州|

UAQ|leizhou|lz|1261@lzh|六枝|LIW|liuzhi|lz|1262@lzh|鹿寨|LIZ|luzhai|lz|1263@lzh|来舟|LZS|

laizhou|lz|1264@lzh|龙镇|LZA|longzhen|lz|1265@lzh|拉鲊|LEM|lazha|lz|1266@lzq|兰州新区|LQJ|

lanzhouxinqu|lzxq|1267@mas|马鞍山|MAH|maanshan|mas|1268@mba|毛坝|MBY|maoba|mb|1269@mbg|毛坝关|

MGY|maobaguan|mbg|1270@mcb|麻城北|MBN|machengbei|mcb|1271@mch|渑池|MCF|mianchi|mc|1272@mch|明城

|MCL|mingcheng|mc|1273@mch|庙城|MAP|miaocheng|mc|1274@mcn|渑池南|MNF|mianchinan|mcn|1275@mcp|茅

草坪|KPM|maocaoping|mcp|1276@mdh|猛洞河|MUQ|mengdonghe|mdh|1277@mds|磨刀石|MOB|modaoshi|mds|

1278@mdu|弥渡|MDF|midu|md|1279@mes|帽儿山|MRB|maoershan|mes|1280@mga|明港|MGN|minggang|mg|

1281@mhk|梅河口|MHL|meihekou|mhk|1282@mhu|马皇|MHZ|mahuang|mh|1283@mjg|孟家岗|MGB|mengjiagang|

mjg|1284@mla|美兰|MHQ|meilan|ml|1285@mld|汨罗东|MQQ|miluodong|mld|1286@mlh|马莲河|MHB|

malianhe|mlh|1287@mli|茅岭|MLZ|maoling|ml|1288@mli|庙岭|MLL|miaoling|ml|1289@mli|茂林|MLD|

maolin|ml|1290@mli|穆棱|MLB|muling|ml|1291@mli|马林|MID|malin|ml|1292@mlo|马龙|MGM|malong|ml|

1293@mlt|木里图|MUD|mulitu|mlt|1294@mlu|汨罗|MLQ|miluo|ml|1295@mnh|玛纳斯湖|MNR|manasihu|mnsh|

1296@mni|冕宁|UGW|mianning|mn|1297@mpa|沐滂|MPQ|mupang|mp|1298@mqh|马桥河|MQB|maqiaohe|mqh|

1299@mqi|闽清|MQS|minqing|mq|1300@mqu|民权|MQF|minquan|mq|1301@msh|明水河|MUT|mingshuihe|msh|

1302@msh|麻山|MAB|mashan|ms|1303@msh|眉山|MSW|meishan|ms|1304@msw|漫水湾|MKW|manshuiwan|msw|

1305@msz|茂舍祖|MOM|maoshezu|msz|1306@msz|米沙子|MST|mishazi|msz|1307@mxi|美溪|MEB|meixi|mx|

1308@mxi|勉县|MVY|mianxian|mx|1309@mya|麻阳|MVQ|mayang|my|1310@myb|密云北|MUP|miyunbei|myb|

1311@myi|米易|MMW|miyi|my|1312@myu|麦园|MYS|maiyuan|my|1313@myu|墨玉|MUR|moyu|my|1314@mzh|庙

庄|MZJ|miaozhuang|mz|1315@mzh|米脂|MEY|mizhi|mz|1316@mzh|明珠|MFQ|mingzhu|mz|1317@nan|宁安|

NAB|ningan|na|1318@nan|农安|NAT|nongan|na|1319@nbs|南博山|NBK|nanboshan|nbs|1320@nch|南仇|NCK|

nanqiu|nc|1321@ncs|南城司|NSP|nanchengsi|ncs|1322@ncu|宁村|NCZ|ningcun|nc|1323@nde|宁德|NES|

ningde|nd|1324@ngc|南观村|NGP|nanguancun|ngc|1325@ngd|南宫东|NFP|nangongdong|ngd|1326@ngl|南关

岭|NLT|nanguanling|ngl|1327@ngu|宁国|NNH|ningguo|ng|1328@nha|宁海|NHH|ninghai|nh|1329@nhc|南河

川|NHJ|nanhechuan|nhc|1330@nhu|南华|NHS|nanhua|nh|1331@nhz|泥河子|NHD|nihezi|nhz|1332@nji|宁

家|NVT|ningjia|nj|1333@nji|南靖|NJS|nanjing|nj|1334@nji|牛家|NJB|niujia|nj|1335@nji|能家|NJD|

nengjia|nj|1336@nko|南口|NKP|nankou|nk|1337@nkq|南口前|NKT|nankouqian|nkq|1338@nla|南朗|NNQ|

nanlang|nl|1339@nli|乃林|NLD|nailin|nl|1340@nlk|尼勒克|NIR|nileke|nlk|1341@nlu|那罗|ULZ|naluo|

nl|1342@nlx|宁陵县|NLF|ninglingxian|nlx|1343@nma|奈曼|NMD|naiman|nm|1344@nmi|宁明|NMZ|

ningming|nm|1345@nmu|南木|NMX|nanmu|nm|1346@npn|南平南|NNS|nanpingnan|npn|1347@npu|那铺|NPZ|

napu|np|1348@nqi|南桥|NQD|nanqiao|nq|1349@nqu|那曲|NQO|naqu|nq|1350@nqu|暖泉|NQJ|nuanquan|nq|

1351@nta|南台|NTT|nantai|nt|1352@nto|南头|NOQ|nantou|nt|1353@nwu|宁武|NWV|ningwu|nw|1354@nwz|南

湾子|NWP|nanwanzi|nwz|1355@nxb|南翔北|NEH|nanxiangbei|nxb|1356@nxi|宁乡|NXQ|ningxiang|nx|

1357@nxi|内乡|NXF|neixiang|nx|1358@nxt|牛心台|NXT|niuxintai|nxt|1359@nyu|南峪|NUP|nanyu|ny|

1360@nzg|娘子关|NIP|niangziguan|nzg|1361@nzh|南召|NAF|nanzhao|nz|1362@nzm|南杂木|NZT|nanzamu|

nzm|1363@pan|蓬安|PAW|pengan|pa|1364@pan|平安|PAL|pingan|pa|1365@pay|平安驿|PNO|pinganyi|pay|

1366@paz|磐安镇|PAJ|pananzhen|paz|1367@paz|平安镇|PZT|pinganzhen|paz|1368@pcd|蒲城东|PEY|

puchengdong|pcd|1369@pch|蒲城|PCY|pucheng|pc|1370@pde|裴德|PDB|peide|pd|1371@pdi|偏店|PRP|

piandian|pd|1372@pdx|平顶山西|BFF|pingdingshanxi|pdsx|1373@pdx|坡底下|PXJ|podixia|pdx|1374@pet|

瓢儿屯|PRT|piaoertun|pet|1375@pfa|平房|PFB|pingfang|pf|1376@pga|平岗|PGL|pinggang|pg|1377@pgu|

平关|PGM|pingguan|pg|1378@pgu|盘关|PAM|panguan|pg|1379@pgu|平果|PGZ|pingguo|pg|1380@phb|徘徊

北|PHP|paihuaibei|phb|1381@phk|平河口|PHM|pinghekou|phk|1382@phu|平湖|PHQ|pinghu|ph|1383@pjb|盘

锦北|PBD|panjinbei|pjb|1384@pjd|潘家店|PDP|panjiadian|pjd|1385@pkn|皮口南|PKT|pikounan|pk|

1386@pld|普兰店|PLT|pulandian|pld|1387@pli|偏岭|PNT|pianling|pl|1388@psh|平山|PSB|pingshan|ps|

1389@psh|彭山|PSW|pengshan|ps|1390@psh|皮山|PSR|pishan|ps|1391@psh|磐石|PSL|panshi|ps|1392@psh|

平社|PSV|pingshe|ps|1393@psh|彭水|PHW|pengshui|ps|1394@pta|平台|PVT|pingtai|pt|1395@pti|平田|

PTM|pingtian|pt|1396@pti|莆田|PTS|putian|pt|1397@ptq|葡萄菁|PTW|putaojing|ptq|1398@pwa|普湾|

PWT|puwan|pw|1399@pwa|平旺|PWV|pingwang|pw|1400@pxg|平型关|PGV|pingxingguan|pxg|1401@pxi|普雄|

POW|puxiong|px|1402@pxi|郫县|PWW|pixian|px|1403@pya|平洋|PYX|pingyang|py|1404@pya|彭阳|PYJ|

pengyang|py|1405@pya|平遥|PYV|pingyao|py|1406@pyi|平邑|PIK|pingyi|py|1407@pyp|平原堡|PPJ|

pingyuanpu|pyp|1408@pyu|平原|PYK|pingyuan|py|1409@pyu|平峪|PYP|pingyu|py|1410@pze|彭泽|PZG|

pengze|pz|1411@pzh|邳州|PJH|pizhou|pz|1412@pzh|平庄|PZD|pingzhuang|pz|1413@pzi|泡子|POD|paozi|

pz|1414@pzn|平庄南|PND|pingzhuangnan|pzn|1415@qan|乾安|QOT|qianan|qa|1416@qan|庆安|QAB|qingan|

qa|1417@qan|迁安|QQP|qianan|qa|1418@qdb|祁东北|QRQ|qidongbei|qd|1419@qdi|七甸|QDM|qidian|qd|

1420@qfd|曲阜东|QAK|qufudong|qfd|1421@qfe|庆丰|QFT|qingfeng|qf|1422@qft|奇峰塔|QVP|qifengta|

qft|1423@qfu|曲阜|QFK|qufu|qf|1424@qha|琼海|QYQ|qionghai|qh|1425@qhd|秦皇岛|QTP|qinhuangdao|

qhd|1426@qhe|千河|QUY|qianhe|qh|1427@qhe|清河|QIP|qinghe|qh|1428@qhm|清河门|QHD|qinghemen|qhm|

1429@qhy|清华园|QHP|qinghuayuan|qhy|1430@qji|全椒|INH|quanjiao|qj|1431@qji|渠旧|QJZ|qujiu|qj|

1432@qji|潜江|QJN|qianjiang|qj|1433@qji|秦家|QJB|qinjia|qj|1434@qji|綦江|QJW|qijiang|qj|

1435@qjp|祁家堡|QBT|qijiapu|qjp|1436@qjx|清涧县|QNY|qingjianxian|qjx|1437@qjz|秦家庄|QZV|

qinjiazhuang|qjz|1438@qlh|七里河|QLD|qilihe|qlh|1439@qli|秦岭|QLY|qinling|ql|1440@qli|渠黎|

QLZ|quli|ql|1441@qlo|青龙|QIB|qinglong|ql|1442@qls|青龙山|QGH|qinglongshan|qls|1443@qme|祁门|

QIH|qimen|qm|1444@qmt|前磨头|QMP|qianmotou|qmt|1445@qsh|青山|QSB|qingshan|qs|1446@qsh|确山|

QSN|queshan|qs|1447@qsh|前山|QXQ|qianshan|qs|1448@qsh|清水|QUJ|qingshui|qs|1449@qsy|戚墅堰|

QYH|qishuyan|qsy|1450@qti|青田|QVH|qingtian|qt|1451@qto|桥头|QAT|qiaotou|qt|1452@qtx|青铜峡|

QTJ|qingtongxia|qtx|1453@qwe|前卫|QWD|qianwei|qw|1454@qwt|前苇塘|QWP|qianweitang|qwt|1455@qxi|

渠县|QRW|quxian|qx|1456@qxi|祁县|QXV|qixian|qx|1457@qxi|青县|QXP|qingxian|qx|1458@qxi|桥西|

QXJ|qiaoxi|qx|1459@qxu|清徐|QUV|qingxu|qx|1460@qxy|旗下营|QXC|qixiaying|qxy|1461@qya|千阳|QOY|

qianyang|qy|1462@qya|沁阳|QYF|qinyang|qy|1463@qya|泉阳|QYL|quanyang|qy|1464@qyb|祁阳北|QVQ|

qiyangbei|qy|1465@qyi|七营|QYJ|qiying|qy|1466@qys|庆阳山|QSJ|qingyangshan|qys|1467@qyu|清远|

QBQ|qingyuan|qy|1468@qyu|清原|QYT|qingyuan|qy|1469@qzd|钦州东|QDZ|qinzhoudong|qzd|1470@qzh|钦州

|QRZ|qinzhou|qz|1471@qzs|青州市|QZK|qingzhoushi|qzs|1472@ran|瑞安|RAH|ruian|ra|1473@rch|荣昌|

RCW|rongchang|rc|1474@rch|瑞昌|RCG|ruichang|rc|1475@rga|如皋|RBH|rugao|rg|1476@rgu|容桂|RUQ|

ronggui|rg|1477@rqi|任丘|RQP|renqiu|rq|1478@rsh|乳山|ROK|rushan|rs|1479@rsh|融水|RSZ|rongshui|

rs|1480@rsh|热水|RSD|reshui|rs|1481@rxi|容县|RXZ|rongxian|rx|1482@rya|饶阳|RVP|raoyang|ry|

1483@rya|汝阳|RYF|ruyang|ry|1484@ryh|绕阳河|RHD|raoyanghe|ryh|1485@rzh|汝州|ROF|ruzhou|rz|

1486@sba|石坝|OBJ|shiba|sb|1487@sbc|上板城|SBP|shangbancheng|sbc|1488@sbi|施秉|AQW|shibing|sb|

1489@sbn|上板城南|OBP|shangbanchengnan|sbcn|1490@sby|世博园|ZWT|shiboyuan|sby|1491@scb|双城北|

SBB|shuangchengbei|scb|1492@sch|舒城|OCH|shucheng|sc|1493@sch|商城|SWN|shangcheng|sc|1494@sch|

莎车|SCR|shache|sc|1495@sch|顺昌|SCS|shunchang|sc|1496@sch|神池|SMV|shenchi|sc|1497@sch|沙城|

SCP|shacheng|sc|1498@sch|石城|SCT|shicheng|sc|1499@scz|山城镇|SCL|shanchengzhen|scz|1500@sda|山

丹|SDJ|shandan|sd|1501@sde|顺德|ORQ|shunde|sd|1502@sde|绥德|ODY|suide|sd|1503@sdo|水洞|SIL|

shuidong|sd|1504@sdu|商都|SXC|shangdu|sd|1505@sdu|十渡|SEP|shidu|sd|1506@sdw|四道湾|OUD|

sidaowan|sdw|1507@sdy|顺德学院|OJQ|shundexueyuan|sdxy|1508@sfa|绅坊|OLH|shenfang|sf|1509@sfe|双

丰|OFB|shuangfeng|sf|1510@sft|四方台|STB|sifangtai|sft|1511@sfu|水富|OTW|shuifu|sf|1512@sgk|三

关口|OKJ|sanguankou|sgk|1513@sgl|桑根达来|OGC|sanggendalai|sgdl|1514@sgu|韶关|SNQ|shaoguan|sg|

1515@sgz|上高镇|SVK|shanggaozhen|sgz|1516@sha|上杭|JBS|shanghang|sh|1517@sha|沙海|SED|shahai|

sh|1518@she|松河|SBM|songhe|sh|1519@she|沙河|SHP|shahe|sh|1520@shk|沙河口|SKT|shahekou|shk|

1521@shl|赛汗塔拉|SHC|saihantala|shtl|1522@shs|沙河市|VOP|shaheshi|shs|1523@shs|沙后所|SSD|

shahousuo|shs|1524@sht|山河屯|SHL|shanhetun|sht|1525@shx|三河县|OXP|sanhexian|shx|1526@shy|四合

永|OHD|siheyong|shy|1527@shz|三汇镇|OZW|sanhuizhen|shz|1528@shz|双河镇|SEL|shuanghezhen|shz|

1529@shz|石河子|SZR|shihezi|shz|1530@shz|三合庄|SVP|sanhezhuang|shz|1531@sjd|三家店|ODP|

sanjiadian|sjd|1532@sjh|水家湖|SQH|shuijiahu|sjh|1533@sjh|沈家河|OJJ|shenjiahe|sjh|1534@sjh|松

江河|SJL|songjianghe|sjh|1535@sji|尚家|SJB|shangjia|sj|1536@sji|孙家|SUB|sunjia|sj|1537@sji|沈

家|OJB|shenjia|sj|1538@sji|双吉|SML|shuangji|sj|1539@sji|松江|SAH|songjiang|sj|1540@sjk|三江

口|SKD|sanjiangkou|sjk|1541@sjl|司家岭|OLK|sijialing|sjl|1542@sjn|松江南|IMH|songjiangnan|sjn|

1543@sjn|石景山南|SRP|shijingshannan|sjsn|1544@sjt|邵家堂|SJJ|shaojiatang|sjt|1545@sjx|三江县|

SOZ|sanjiangxian|sjx|1546@sjz|三家寨|SMM|sanjiazhai|sjz|1547@sjz|十家子|SJD|shijiazi|sjz|

1548@sjz|松江镇|OZL|songjiangzhen|sjz|1549@sjz|施家嘴|SHM|shijiazui|sjz|1550@sjz|深井子|SWT|

shenjingzi|sjz|1551@sld|什里店|OMP|shilidian|sld|1552@sle|疏勒|SUR|shule|sl|1553@slh|疏勒河|

SHJ|shulehe|slh|1554@slh|舍力虎|VLD|shelihu|slh|1555@sli|石磷|SPB|shilin|sl|1556@sli|双辽|ZJD|

shuangliao|sl|1557@sli|绥棱|SIB|suiling|sl|1558@sli|石岭|SOL|shiling|sl|1559@sli|石林|SLM|

shilin|sl|1560@sln|石林南|LNM|shilinnan|sln|1561@slo|石龙|SLQ|shilong|sl|1562@slq|萨拉齐|SLC|

salaqi|slq|1563@slu|索伦|SNT|suolun|sl|1564@slu|商洛|OLY|shangluo|sl|1565@slz|沙岭子|SLP|

shalingzi|slz|1566@smb|石门县北|VFQ|shimenxianbei|smxb|1567@smn|三门峡南|SCF|sanmenxianan|

smxn|1568@smx|三门县|OQH|sanmenxian|smx|1569@smx|石门县|OMQ|shimenxian|smx|1570@smx|三门峡西|

SXF|sanmenxiaxi|smxx|1571@sni|肃宁|SYP|suning|sn|1572@son|宋|SOB|song|son|1573@spa|双牌|SBZ|

shuangpai|sp|1574@spd|四平东|PPT|sipingdong|spd|1575@spi|遂平|SON|suiping|sp|1576@spt|沙坡头|

SFJ|shapotou|spt|1577@sqi|沙桥|SQM|shaqiao|sq|1578@sqn|商丘南|SPF|shangqiunan|sqn|1579@squ|水泉

|SID|shuiquan|sq|1580@sqx|石泉县|SXY|shiquanxian|sqx|1581@sqz|石桥子|SQT|shiqiaozi|sqz|

1582@src|石人城|SRB|shirencheng|src|1583@sre|石人|SRL|shiren|sr|1584@ssh|山市|SQB|shanshi|ss|

1585@ssh|神树|SWB|shenshu|ss|1586@ssh|鄯善|SSR|shanshan|ss|1587@ssh|三水|SJQ|sanshui|ss|

1588@ssh|泗水|OSK|sishui|ss|1589@ssh|石山|SAD|shishan|ss|1590@ssh|松树|SFT|songshu|ss|1591@ssh|

首山|SAT|shoushan|ss|1592@ssj|三十家|SRD|sanshijia|ssj|1593@ssp|三十里堡|SST|sanshilipu|sslp|

1594@ssz|松树镇|SSL|songshuzhen|ssz|1595@sta|松桃|MZQ|songtao|st|1596@sth|索图罕|SHX|suotuhan|

sth|1597@stj|三堂集|SDH|santangji|stj|1598@sto|石头|OTB|shitou|st|1599@sto|神头|SEV|shentou|

st|1600@stu|沙沱|SFM|shatuo|st|1601@swa|上万|SWP|shangwan|sw|1602@swu|孙吴|SKB|sunwu|sw|

1603@swx|沙湾县|SXR|shawanxian|swx|1604@sxi|歙县|OVH|shexian|sx|1605@sxi|遂溪|SXZ|suixi|sx|

1606@sxi|沙县|SAS|shaxian|sx|1607@sxi|绍兴|SOH|shaoxing|sx|1608@sxi|石岘|SXL|shixian|sx|

1609@sxp|上西铺|SXM|shangxipu|sxp|1610@sxz|石峡子|SXJ|shixiazi|sxz|1611@sya|沭阳|FMH|shuyang|

sy|1612@sya|绥阳|SYB|suiyang|sy|1613@sya|寿阳|SYV|shouyang|sy|1614@sya|水洋|OYP|shuiyang|sy|

1615@syc|三阳川|SYJ|sanyangchuan|syc|1616@syd|上腰墩|SPJ|shangyaodun|syd|1617@syi|三营|OEJ|

sanying|sy|1618@syi|顺义|SOP|shunyi|sy|1619@syj|三义井|OYD|sanyijing|syj|1620@syp|三源浦|SYL|

sanyuanpu|syp|1621@syu|上虞|BDH|shangyu|sy|1622@syu|三原|SAY|sanyuan|sy|1623@syu|上园|SUD|

shangyuan|sy|1624@syu|水源|OYJ|shuiyuan|sy|1625@syz|桑园子|SAJ|sangyuanzi|syz|1626@szb|绥中北|

SND|suizhongbei|szb|1627@szb|苏州北|OHH|suzhoubei|szb|1628@szd|宿州东|SRH|suzhoudong|szd|

1629@szd|深圳东|BJQ|shenzhendong|szd|1630@szh|深州|OZP|shenzhou|sz|1631@szh|孙镇|OZY|sunzhen|

sz|1632@szh|绥中|SZD|suizhong|sz|1633@szh|尚志|SZB|shangzhi|sz|1634@szh|师庄|SNM|shizhuang|sz|

1635@szi|松滋|SIN|songzi|sz|1636@szo|师宗|SEM|shizong|sz|1637@szq|苏州园区|KAH|suzhouyuanqu|

szyq|1638@szq|苏州新区|ITH|suzhouxinqu|szxq|1639@tan|泰安|TMK|taian|ta|1640@tan|台安|TID|

taian|ta|1641@tay|通安驿|TAJ|tonganyi|tay|1642@tba|桐柏|TBF|tongbai|tb|1643@tbe|通北|TBB|

tongbei|tb|1644@tch|桐城|TTH|tongcheng|tc|1645@tch|汤池|TCX|tangchi|tc|1646@tch|郯城|TZK|

tancheng|tc|1647@tch|铁厂|TCL|tiechang|tc|1648@tcu|桃村|TCK|taocun|tc|1649@tda|通道|TRQ|

tongdao|td|1650@tdo|田东|TDZ|tiandong|td|1651@tga|天岗|TGL|tiangang|tg|1652@tgl|土贵乌拉|TGC|

tuguiwula|tgwl|1653@tgo|通沟|TOL|tonggou|tg|1654@tgu|太谷|TGV|taigu|tg|1655@tha|塔哈|THX|taha|

th|1656@tha|棠海|THM|tanghai|th|1657@the|唐河|THF|tanghe|th|1658@the|泰和|THG|taihe|th|

1659@thu|太湖|TKH|taihu|th|1660@tji|团结|TIX|tuanjie|tj|1661@tjj|谭家井|TNJ|tanjiajing|tjj|

1662@tjt|陶家屯|TOT|taojiatun|tjt|1663@tjw|唐家湾|PDQ|tangjiawan|tjw|1664@tjz|统军庄|TZP|

tongjunzhuang|tjz|1665@tka|泰康|TKX|taikang|tk|1666@tld|吐列毛杜|TMD|tuliemaodu|tlmd|1667@tlh|

图里河|TEX|tulihe|tlh|1668@tli|铜陵|TJH|tongling|tl|1669@tli|田林|TFZ|tianlin|tl|1670@tli|亭

亮|TIZ|tingliang|tl|1671@tli|铁力|TLB|tieli|tl|1672@tlx|铁岭西|PXT|tielingxi|tlx|1673@tmb|图们

北|QSL|tumenbei|tmb|1674@tme|天门|TMN|tianmen|tm|1675@tmn|天门南|TNN|tianmennan|tmn|1676@tms|太

姥山|TLS|taimushan|tms|1677@tmt|土牧尔台|TRC|tumuertai|tmet|1678@tmz|土门子|TCJ|tumenzi|tmz|

1679@tna|洮南|TVT|taonan|tn|1680@tna|潼南|TVW|tongnan|tn|1681@tpc|太平川|TIT|taipingchuan|tpc|

1682@tpz|太平镇|TEB|taipingzhen|tpz|1683@tqi|图强|TQX|tuqiang|tq|1684@tqi|台前|TTK|taiqian|tq|

1685@tql|天桥岭|TQL|tianqiaoling|tql|1686@tqz|土桥子|TQJ|tuqiaozi|tqz|1687@tsc|汤山城|TCT|

tangshancheng|tsc|1688@tsh|桃山|TAB|taoshan|ts|1689@tsz|塔石嘴|TIM|tashizui|tsz|1690@ttu|通途|

TUT|tongtu|tt|1691@twh|汤旺河|THB|tangwanghe|twh|1692@txi|同心|TXJ|tongxin|tx|1693@txi|土溪|

TSW|tuxi|tx|1694@txi|桐乡|TCH|tongxiang|tx|1695@tya|田阳|TRZ|tianyang|ty|1696@tyi|天义|TND|

tianyi|ty|1697@tyi|汤阴|TYF|tangyin|ty|1698@tyl|驼腰岭|TIL|tuoyaoling|tyl|1699@tys|太阳山|TYJ|

taiyangshan|tys|1700@tyu|汤原|TYB|tangyuan|ty|1701@tyy|塔崖驿|TYP|tayayi|tyy|1702@tzd|滕州东|

TEK|tengzhoudong|tzd|1703@tzh|台州|TZH|taizhou|tz|1704@tzh|天祝|TZJ|tianzhu|tz|1705@tzh|滕州|

TXK|tengzhou|tz|1706@tzh|天镇|TZV|tianzhen|tz|1707@tzl|桐子林|TEW|tongzilin|tzl|1708@tzs|天柱山

|QWH|tianzhushan|tzs|1709@wan|文安|WBP|wenan|wa|1710@wan|武安|WAP|wuan|wa|1711@waz|王安镇|WVP|

wanganzhen|waz|1712@wca|旺苍|WEW|wangcang|wc|1713@wcg|五叉沟|WCT|wuchagou|wcg|1714@wch|文昌|

WEQ|wenchang|wc|1715@wch|温春|WDB|wenchun|wc|1716@wdc|五大连池|WRB|wudalianchi|wdlc|1717@wde|文

登|WBK|wendeng|wd|1718@wdg|五道沟|WDL|wudaogou|wdg|1719@wdh|五道河|WHP|wudaohe|wdh|1720@wdi|文

地|WNZ|wendi|wd|1721@wdo|卫东|WVT|weidong|wd|1722@wds|武当山|WRN|wudangshan|wds|1723@wdu|望都|

WDP|wangdu|wd|1724@weh|乌尔旗汗|WHX|wuerqihan|weqh|1725@wfa|潍坊|WFK|weifang|wf|1726@wft|万发屯

|WFB|wanfatun|wft|1727@wfu|王府|WUT|wangfu|wf|1728@wfx|瓦房店西|WXT|wafangdianxi|wfdx|1729@wga|

王岗|WGB|wanggang|wg|1730@wgo|武功|WGY|wugong|wg|1731@wgo|湾沟|WGL|wangou|wg|1732@wgt|吴官田|

WGM|wuguantian|wgt|1733@wha|乌海|WVC|wuhai|wh|1734@whe|苇河|WHB|weihe|wh|1735@whu|卫辉|WHF|

weihui|wh|1736@wjc|吴家川|WCJ|wujiachuan|wjc|1737@wji|五家|WUB|wujia|wj|1738@wji|威箐|WAM|

weiqing|wj|1739@wji|午汲|WJP|wuji|wj|1740@wji|渭津|WJL|weijin|wj|1741@wjw|王家湾|WJJ|

wangjiawan|wjw|1742@wke|倭肯|WQB|woken|wk|1743@wks|五棵树|WKT|wukeshu|wks|1744@wlb|五龙背|WBT|

wulongbei|wlb|1745@wld|乌兰哈达|WLC|wulanhada|wlhd|1746@wle|万乐|WEB|wanle|wl|1747@wlg|瓦拉干|

WVX|walagan|wlg|1748@wli|温岭|VHH|wenling|wl|1749@wli|五莲|WLK|wulian|wl|1750@wlq|乌拉特前旗|

WQC|wulateqianqi|wltqq|1751@wls|乌拉山|WSC|wulashan|wls|1752@wlt|卧里屯|WLX|wolitun|wlt|

1753@wnb|渭南北|WBY|weinanbei|wnb|1754@wne|乌奴耳|WRX|wunuer|wne|1755@wni|万宁|WNQ|wanning|wn|

1756@wni|万年|WWG|wannian|wn|1757@wnn|渭南南|WVY|weinannan|wnn|1758@wnz|渭南镇|WNJ|weinanzhen|

wnz|1759@wpi|沃皮|WPT|wopi|wp|1760@wpu|吴堡|WUY|wupu|wp|1761@wqi|吴桥|WUP|wuqiao|wq|1762@wqi|汪

清|WQL|wangqing|wq|1763@wqi|武清|WWP|wuqing|wq|1764@wsh|武山|WSJ|wushan|ws|1765@wsh|文水|WEV|

wenshui|ws|1766@wsz|魏善庄|WSP|weishanzhuang|wsz|1767@wto|王瞳|WTP|wangtong|wt|1768@wts|五台

山|WSV|wutaishan|wts|1769@wtz|王团庄|WZJ|wangtuanzhuang|wtz|1770@wwu|五五|WVR|wuwu|ww|1771@wxd|

无锡东|WGH|wuxidong|wxd|1772@wxi|卫星|WVB|weixing|wx|1773@wxi|闻喜|WXV|wenxi|wx|1774@wxi|武乡|

WVV|wuxiang|wx|1775@wxq|无锡新区|IFH|wuxixinqu|wxxq|1776@wxu|武穴|WXN|wuxue|wx|1777@wxu|吴圩|

WYZ|wuxu|wx|1778@wya|王杨|WYB|wangyang|wy|1779@wyi|武义|RYH|wuyi|wy|1780@wyi|五营|WWB|wuying|

wy|1781@wyt|瓦窑田|WIM|wayaotian|wyt|1782@wyu|五原|WYC|wuyuan|wy|1783@wzg|苇子沟|WZL|weizigou|

wzg|1784@wzh|韦庄|WZY|weizhuang|wz|1785@wzh|五寨|WZV|wuzhai|wz|1786@wzt|王兆屯|WZB|

wangzhaotun|wzt|1787@wzz|微子镇|WQP|weizizhen|wzz|1788@wzz|魏杖子|WKD|weizhangzi|wzz|1789@xan|

新安|EAM|xinan|xa|1790@xan|兴安|XAZ|xingan|xa|1791@xax|新安县|XAF|xinanxian|xax|1792@xba|新保安

|XAP|xinbaoan|xba|1793@xbc|下板城|EBP|xiabancheng|xbc|1794@xbl|西八里|XLP|xibali|xbl|1795@xch|

宣城|ECH|xuancheng|xc|1796@xch|兴城|XCD|xingcheng|xc|1797@xcu|小村|XEM|xiaocun|xc|1798@xcy|新绰

源|XRX|xinchuoyuan|xcy|1799@xcz|下城子|XCB|xiachengzi|xcz|1800@xcz|新城子|XCT|xinchengzi|xcz|

1801@xde|喜德|EDW|xide|xd|1802@xdj|小得江|EJM|xiaodejiang|xdj|1803@xdm|西大庙|XMP|xidamiao|

xdm|1804@xdo|小董|XEZ|xiaodong|xd|1805@xdo|小东|XOD|xiaodong|xd|1806@xfe|信丰|EFG|xinfeng|xf|

1807@xfe|襄汾|XFV|xiangfen|xf|1808@xfe|息烽|XFW|xifeng|xf|1809@xga|新干|EGG|xingan|xg|1810@xga|

孝感|XGN|xiaogan|xg|1811@xgc|西固城|XUJ|xigucheng|xgc|1812@xgu|西固|XIJ|xigu|xg|1813@xgy|夏官营

|XGJ|xiaguanying|xgy|1814@xgz|西岗子|NBB|xigangzi|xgz|1815@xhe|襄河|XXB|xianghe|xh|1816@xhe|新

和|XIR|xinhe|xh|1817@xhe|宣和|XWJ|xuanhe|xh|1818@xhj|斜河涧|EEP|xiehejian|xhj|1819@xht|新华屯|

XAX|xinhuatun|xht|1820@xhu|新华|XHB|xinhua|xh|1821@xhu|新化|EHQ|xinhua|xh|1822@xhu|宣化|XHP|

xuanhua|xh|1823@xhx|兴和西|XEC|xinghexi|xhx|1824@xhy|小河沿|XYD|xiaoheyan|xhy|1825@xhy|下花园|

XYP|xiahuayuan|xhy|1826@xhz|小河镇|EKY|xiaohezhen|xhz|1827@xji|徐家|XJB|xujia|xj|1828@xji|峡

江|EJG|xiajiang|xj|1829@xji|新绛|XJV|xinjiang|xj|1830@xji|辛集|ENP|xinji|xj|1831@xji|新江|XJM|

xinjiang|xj|1832@xjk|西街口|EKM|xijiekou|xjk|1833@xjt|许家屯|XJT|xujiatun|xjt|1834@xjt|许家台|

XTJ|xujiatai|xjt|1835@xjz|谢家镇|XMT|xiejiazhen|xjz|1836@xka|兴凯|EKB|xingkai|xk|1837@xla|小

榄|EAQ|xiaolan|xl|1838@xla|香兰|XNB|xianglan|xl|1839@xld|兴隆店|XDD|xinglongdian|xld|1840@xle|

新乐|ELP|xinle|xl|1841@xli|新林|XPX|xinlin|xl|1842@xli|小岭|XLB|xiaoling|xl|1843@xli|新李|XLJ|

xinli|xl|1844@xli|西林|XYB|xilin|xl|1845@xli|西柳|GCT|xiliu|xl|1846@xli|仙林|XPH|xianlin|xl|

1847@xlt|新立屯|XLD|xinlitun|xlt|1848@xlz|兴隆镇|XZB|xinglongzhen|xlz|1849@xlz|新立镇|XGT|

xinlizhen|xlz|1850@xmi|新民|XMD|xinmin|xm|1851@xms|西麻山|XMB|ximashan|xms|1852@xmt|下马塘|

XAT|xiamatang|xmt|1853@xna|孝南|XNV|xiaonan|xn|1854@xnb|咸宁北|XRN|xianningbei|xnb|1855@xni|兴

宁|ENQ|xingning|xn|1856@xni|咸宁|XNN|xianning|xn|1857@xpd|犀浦东|XAW|xipudong|xpd|1858@xpi|西平

|XPN|xiping|xp|1859@xpi|兴平|XPY|xingping|xp|1860@xpt|新坪田|XPM|xinpingtian|xpt|1861@xpu|霞

浦|XOS|xiapu|xp|1862@xpu|溆浦|EPQ|xupu|xp|1863@xpu|犀浦|XIW|xipu|xp|1864@xqi|新青|XQB|xinqing|

xq|1865@xqi|新邱|XQD|xinqiu|xq|1866@xqp|兴泉堡|XQJ|xingquanbu|xqp|1867@xrq|仙人桥|XRL|

xianrenqiao|xrq|1868@xsg|小寺沟|ESP|xiaosigou|xsg|1869@xsh|杏树|XSB|xingshu|xs|1870@xsh|浠水|

XZN|xishui|xs|1871@xsh|下社|XSV|xiashe|xs|1872@xsh|徐水|XSP|xushui|xs|1873@xsh|夏石|XIZ|

xiashi|xs|1874@xsh|小哨|XAM|xiaoshao|xs|1875@xsp|新松浦|XOB|xinsongpu|xsp|1876@xst|杏树屯|XDT|

xingshutun|xst|1877@xsw|许三湾|XSJ|xusanwan|xsw|1878@xta|湘潭|XTQ|xiangtan|xt|1879@xta|邢台|

XTP|xingtai|xt|1880@xtx|仙桃西|XAN|xiantaoxi|xtx|1881@xtz|下台子|EIP|xiataizi|xtz|1882@xwe|徐闻

|XJQ|xuwen|xw|1883@xwp|新窝铺|EPD|xinwopu|xwp|1884@xwu|修武|XWF|xiuwu|xw|1885@xxi|新县|XSN|

xinxian|xx|1886@xxi|息县|ENN|xixian|xx|1887@xxi|西乡|XQY|xixiang|xx|1888@xxi|湘乡|XXQ|

xiangxiang|xx|1889@xxi|西峡|XIF|xixia|xx|1890@xxi|孝西|XOV|xiaoxi|xx|1891@xxj|小新街|XXM|

xiaoxinjie|xxj|1892@xxx|新兴县|XGQ|xinxingxian|xxx|1893@xxz|西小召|XZC|xixiaozhao|xxz|1894@xxz|

小西庄|XXP|xiaoxizhuang|xxz|1895@xya|向阳|XDB|xiangyang|xy|1896@xya|旬阳|XUY|xunyang|xy|

1897@xyb|旬阳北|XBY|xunyangbei|xyb|1898@xyd|襄阳东|XWN|xiangyangdong|xyd|1899@xye|兴业|SNZ|

xingye|xy|1900@xyg|小雨谷|XHM|xiaoyugu|xyg|1901@xyi|信宜|EEQ|xinyi|xy|1902@xyj|小月旧|XFM|

xiaoyuejiu|xyj|1903@xyq|小扬气|XYX|xiaoyangqi|xyq|1904@xyu|祥云|EXM|xiangyun|xy|1905@xyu|襄垣|

EIF|xiangyuan|xy|1906@xyx|夏邑县|EJH|xiayixian|xyx|1907@xyy|新友谊|EYB|xinyouyi|xyy|1908@xyz|新

阳镇|XZJ|xinyangzhen|xyz|1909@xzd|徐州东|UUH|xuzhoudong|xzd|1910@xzf|新帐房|XZX|xinzhangfang|

xzf|1911@xzh|悬钟|XRP|xuanzhong|xz|1912@xzh|新肇|XZT|xinzhao|xz|1913@xzh|忻州|XXV|xinzhou|xz|

1914@xzi|汐子|XZD|xizi|xz|1915@xzm|西哲里木|XRD|xizhelimu|xzlm|1916@xzz|新杖子|ERP|xinzhangzi|

xzz|1917@yan|姚安|YAC|yaoan|ya|1918@yan|依安|YAX|yian|ya|1919@yan|永安|YAS|yongan|ya|1920@yax|

永安乡|YNB|yonganxiang|yax|1921@ybl|亚布力|YBB|yabuli|ybl|1922@ybs|元宝山|YUD|yuanbaoshan|ybs|

1923@yca|羊草|YAB|yangcao|yc|1924@ycd|秧草地|YKM|yangcaodi|ycd|1925@ych|阳澄湖|AIH|

yangchenghu|ych|1926@ych|迎春|YYB|yingchun|yc|1927@ych|叶城|YER|yecheng|yc|1928@ych|盐池|YKJ|

yanchi|yc|1929@ych|砚川|YYY|yanchuan|yc|1930@ych|阳春|YQQ|yangchun|yc|1931@ych|宜城|YIN|

yicheng|yc|1932@ych|应城|YHN|yingcheng|yc|1933@ych|禹城|YCK|yucheng|yc|1934@ych|晏城|YEK|

yancheng|yc|1935@ych|羊场|YED|yangchang|yc|1936@ych|阳城|YNF|yangcheng|yc|1937@ych|阳岔|YAL|

yangcha|yc|1938@ych|郓城|YPK|yuncheng|yc|1939@ych|雁翅|YAP|yanchi|yc|1940@ycl|云彩岭|ACP|

yuncailing|ycl|1941@ycx|虞城县|IXH|yuchengxian|ycx|1942@ycz|营城子|YCT|yingchengzi|ycz|

1943@yde|英德|YDQ|yingde|yd|1944@yde|永登|YDJ|yongdeng|yd|1945@ydi|尹地|YDM|yindi|yd|1946@ydi|

永定|YGS|yongding|yd|1947@yds|雁荡山|YGH|yandangshan|yds|1948@ydu|于都|YDG|yudu|yd|1949@ydu|园

墩|YAJ|yuandun|yd|1950@ydx|英德西|IIQ|yingdexi|ydx|1951@yfy|永丰营|YYM|yongfengying|yfy|

1952@yga|杨岗|YRB|yanggang|yg|1953@yga|阳高|YOV|yanggao|yg|1954@ygu|阳谷|YIK|yanggu|yg|

1955@yha|友好|YOB|youhao|yh|1956@yha|余杭|EVH|yuhang|yh|1957@yhc|沿河城|YHP|yanhecheng|yhc|

1958@yhu|岩会|AEP|yanhui|yh|1959@yjh|羊臼河|YHM|yangjiuhe|yjh|1960@yji|永嘉|URH|yongjia|yj|

1961@yji|营街|YAM|yingjie|yj|1962@yji|盐津|AEW|yanjin|yj|1963@yji|余江|YHG|yujiang|yj|1964@yji|

燕郊|AJP|yanjiao|yj|1965@yji|姚家|YAT|yaojia|yj|1966@yjj|岳家井|YGJ|yuejiajing|yjj|1967@yjp|一

间堡|YJT|yijianpu|yjp|1968@yjs|英吉沙|YIR|yingjisha|yjs|1969@yjs|云居寺|AFP|yunjusi|yjs|

1970@yjz|燕家庄|AZK|yanjiazhuang|yjz|1971@yka|永康|RFH|yongkang|yk|1972@ykd|营口东|YGT|

yingkoudong|ykd|1973@yla|银浪|YJX|yinlang|yl|1974@yla|永郎|YLW|yonglang|yl|1975@ylb|宜良北|

YSM|yiliangbei|ylb|1976@yld|永乐店|YDY|yongledian|yld|1977@ylh|伊拉哈|YLX|yilaha|ylh|1978@yli|

伊林|YLB|yilin|yl|1979@yli|杨陵|YSY|yangling|yl|1980@yli|彝良|ALW|yiliang|yl|1981@yli|杨林|

YLM|yanglin|yl|1982@ylp|余粮堡|YLD|yuliangpu|ylp|1983@ylq|杨柳青|YQP|yangliuqing|ylq|1984@ylt|

月亮田|YUM|yueliangtian|ylt|1985@yma|义马|YMF|yima|ym|1986@ymb|阳明堡|YVV|yangmingbu|ymb|

1987@yme|玉门|YXJ|yumen|ym|1988@yme|云梦|YMN|yunmeng|ym|1989@ymo|元谋|YMM|yuanmou|ym|1990@yms|

一面山|YST|yimianshan|yms|1991@yna|沂南|YNK|yinan|yn|1992@yna|宜耐|YVM|yinai|yn|1993@ynd|伊宁东

|YNR|yiningdong|ynd|1994@yps|营盘水|YZJ|yingpanshui|yps|1995@ypu|羊堡|ABM|yangpu|yp|1996@yqb|阳

泉北|YPP|yangquanbei|yqb|1997@yqi|乐清|UPH|yueqing|yq|1998@yqi|焉耆|YSR|yanqi|yq|1999@yqi|源

迁|AQK|yuanqian|yq|2000@yqt|姚千户屯|YQT|yaoqianhutun|yqht|2001@yqu|阳曲|YQV|yangqu|yq|

2002@ysg|榆树沟|YGP|yushugou|ysg|2003@ysh|月山|YBF|yueshan|ys|2004@ysh|玉石|YSJ|yushi|ys|

2005@ysh|玉舍|AUM|yushe|ys|2006@ysh|偃师|YSF|yanshi|ys|2007@ysh|沂水|YUK|yishui|ys|2008@ysh|榆

社|YSV|yushe|ys|2009@ysh|颍上|YVH|yingshang|ys|2010@ysh|窑上|ASP|yaoshang|ys|2011@ysh|元氏|

YSP|yuanshi|ys|2012@ysl|杨树岭|YAD|yangshuling|ysl|2013@ysp|野三坡|AIP|yesanpo|ysp|2014@yst|榆

树屯|YSX|yushutun|yst|2015@yst|榆树台|YUT|yushutai|yst|2016@ysz|鹰手营子|YIP|yingshouyingzi|

ysyz|2017@yta|源潭|YTQ|yuantan|yt|2018@ytp|牙屯堡|YTZ|yatunpu|ytp|2019@yts|烟筒山|YSL|

yantongshan|yts|2020@ytt|烟筒屯|YUX|yantongtun|ytt|2021@yws|羊尾哨|YWM|yangweishao|yws|

2022@yxi|越西|YHW|yuexi|yx|2023@yxi|攸县|YOG|youxian|yx|2024@yxi|永修|ACG|yongxiu|yx|2025@yxx|

玉溪西|YXM|yuxixi|yxx|2026@yya|弋阳|YIG|yiyang|yy|2027@yya|余姚|YYH|yuyao|yy|2028@yya|酉阳|

AFW|youyang|yy|2029@yyd|岳阳东|YIQ|yueyangdong|yyd|2030@yyi|阳邑|ARP|yangyi|yy|2031@yyu|鸭园|

YYL|yayuan|yy|2032@yyz|鸳鸯镇|YYJ|yuanyangzhen|yyz|2033@yzb|燕子砭|YZY|yanzibian|yzb|2034@yzh|

仪征|UZH|yizheng|yz|2035@yzh|宜州|YSZ|yizhou|yz|2036@yzh|兖州|YZK|yanzhou|yz|2037@yzi|迤资|

YQM|yizi|yz|2038@yzw|羊者窝|AEM|yangzhewo|yzw|2039@yzz|杨杖子|YZD|yangzhangzi|yzz|2040@zan|镇安

|ZEY|zhenan|za|2041@zan|治安|ZAD|zhian|za|2042@zba|招柏|ZBP|zhaobai|zb|2043@zbw|张百湾|ZUP|

zhangbaiwan|zbw|2044@zcc|中川机场|ZJJ|zhongchuanjichang|zcjc|2045@zch|枝城|ZCN|zhicheng|zc|

2046@zch|子长|ZHY|zichang|zc|2047@zch|诸城|ZQK|zhucheng|zc|2048@zch|邹城|ZIK|zoucheng|zc|

2049@zch|赵城|ZCV|zhaocheng|zc|2050@zda|章党|ZHT|zhangdang|zd|2051@zdi|正定|ZDP|zhengding|zd|

2052@zdo|肇东|ZDB|zhaodong|zd|2053@zfp|照福铺|ZFM|zhaofupu|zfp|2054@zgt|章古台|ZGD|zhanggutai|

zgt|2055@zgu|赵光|ZGB|zhaoguang|zg|2056@zhe|中和|ZHX|zhonghe|zh|2057@zhm|中华门|VNH|

zhonghuamen|zhm|2058@zjb|枝江北|ZIN|zhijiangbei|zjb|2059@zjc|钟家村|ZJY|zhongjiacun|zjc|

2060@zjg|朱家沟|ZUB|zhujiagou|zjg|2061@zjg|紫荆关|ZYP|zijingguan|zjg|2062@zji|周家|ZOB|

zhoujia|zj|2063@zji|诸暨|ZDH|zhuji|zj|2064@zjn|镇江南|ZEH|zhenjiangnan|zjn|2065@zjt|周家屯|

ZOD|zhoujiatun|zjt|2066@zjw|褚家湾|CWJ|zhujiawan|zjw|2067@zjx|湛江西|ZWQ|zhanjiangxi|zjx|

2068@zjy|朱家窑|ZUJ|zhujiayao|zjy|2069@zjz|曾家坪子|ZBW|zengjiapingzi|zjpz|2070@zla|张兰|ZLV|

zhanglan|zl|2071@zla|镇赉|ZLT|zhenlai|zl|2072@zli|枣林|ZIV|zaolin|zl|2073@zlt|扎鲁特|ZLD|

zhalute|zlt|2074@zlx|扎赉诺尔西|ZXX|zhalainuoerxi|zlrex|2075@zmt|樟木头|ZOQ|zhangmutou|zmt|

2076@zmu|中牟|ZGF|zhongmu|zm|2077@znd|中宁东|ZDJ|zhongningdong|znd|2078@zni|中宁|VNJ|

zhongning|zn|2079@znn|中宁南|ZNJ|zhongningnan|znn|2080@zpi|镇平|ZPF|zhenping|zp|2081@zpi|漳平|

ZPS|zhangping|zp|2082@zpu|泽普|ZPR|zepu|zp|2083@zqi|枣强|ZVP|zaoqiang|zq|2084@zqi|张桥|ZQY|

zhangqiao|zq|2085@zqi|章丘|ZTK|zhangqiu|zq|2086@zrh|朱日和|ZRC|zhurihe|zrh|2087@zrl|泽润里|

ZLM|zerunli|zrl|2088@zsb|中山北|ZGQ|zhongshanbei|zsb|2089@zsd|樟树东|ZOG|zhangshudong|zsd|

2090@zsh|中山|ZSQ|zhongshan|zs|2091@zsh|柞水|ZSY|zhashui|zs|2092@zsh|钟山|ZSZ|zhongshan|zs|

2093@zsh|樟树|ZSG|zhangshu|zs|2094@zwo|珠窝|ZOP|zhuwo|zw|2095@zwt|张维屯|ZWB|zhangweitun|zwt|

2096@zwu|彰武|ZWD|zhangwu|zw|2097@zxi|棕溪|ZOY|zongxi|zx|2098@zxi|钟祥|ZTN|zhongxiang|zx|

2099@zxi|资溪|ZXS|zixi|zx|2100@zxi|镇西|ZVT|zhenxi|zx|2101@zxi|张辛|ZIP|zhangxin|zx|2102@zxq|正

镶白旗|ZXC|zhengxiangbaiqi|zxbq|2103@zya|紫阳|ZVY|ziyang|zy|2104@zya|枣阳|ZYN|zaoyang|zy|

2105@zyb|竹园坝|ZAW|zhuyuanba|zyb|2106@zye|张掖|ZYJ|zhangye|zy|2107@zyu|镇远|ZUW|zhenyuan|zy|

2108@zyx|朱杨溪|ZXW|zhuyangxi|zyx|2109@zzd|漳州东|GOS|zhangzhoudong|zzd|2110@zzh|漳州|ZUS|

zhangzhou|zz|2111@zzh|壮志|ZUX|zhuangzhi|zz|2112@zzh|子洲|ZZY|zizhou|zz|2113@zzh|中寨|ZZM|

zhongzhai|zz|2114@zzh|涿州|ZXP|zhuozhou|zz|2115@zzi|咋子|ZAL|zhazi|zz|2116@zzs|卓资山|ZZC|

zhuozishan|zzs|2117@zzx|株洲西|ZAQ|zhuzhouxi|zzx|2118@zzx|郑州西|XPF|zhengzhouxi|zzx|2119@abq|

阿巴嘎旗|AQC|abagaqi|abgq|2120@aeb|阿尔山北|ARX|aershanbei|aesb|2121@alt|阿勒泰|AUR|aletai|

alt|2122@are|安仁|ARG|anren|ar|2123@asx|安顺西|ASE|anshunxi|asx|2124@atx|安图西|AXL|antuxi|

atx|2125@ayd|安阳东|ADF|anyangdong|ayd|2126@bba|博白|BBZ|bobai|bb|2127@bbu|八步|BBE|babu|bb|

2128@bch|栟茶|FWH|bencha|bc|2129@bdd|保定东|BMP|baodingdong|bdd|2130@bgo|白沟|FEP|baigou|bg|

2131@bha|滨海|FHP|binhai|bh|2132@bhb|滨海北|FCP|binhaibei|bhb|2133@bjn|宝鸡南|BBY|baojinan|

bjn|2134@bjz|北井子|BRT|beijingzi|bjz|2135@bmj|白马井|BFQ|baimajing|bmj|2136@bqi|宝清|BUB|

baoqing|bq|2137@bsh|璧山|FZW|bishan|bs|2138@bsp|白沙铺|BSN|baishapu|bsp|2139@bsx|白水县|BGY|

baishuixian|bsx|2140@bta|板塘|NGQ|bantang|bt|2141@bxc|本溪新城|BVT|benxixincheng|bxxc|2142@bxi|

彬县|BXY|binxian|bx|2143@bya|宾阳|UKZ|binyang|by|2144@byd|白洋淀|FWP|baiyangdian|byd|2145@byi|

百宜|FHW|baiyi|by|2146@byn|白音华南|FNC|baiyinhuanan|byhn|2147@bzd|巴中东|BDE|bazhongdong|bzd|

2148@bzh|滨州|BIK|binzhou|bz|2149@bzx|霸州西|FOP|bazhouxi|bzx|2150@cch|澄城|CUY|chengcheng|cc|

2151@chd|巢湖东|GUH|chaohudong|chd|2152@cji|从江|KNW|congjiang|cj|2153@cka|茶卡|CVO|chaka|ck|

2154@clh|长临河|FVH|changlinhe|clh|2155@cln|茶陵南|CNG|chalingnan|cln|2156@cpd|常平东|FQQ|

changpingdong|cpd|2157@cqq|长庆桥|CQJ|changqingqiao|cqq|2158@csb|长寿北|COW|changshoubei|csb|

2159@csh|长寿湖|CSE|changshouhu|csh|2160@csh|潮汕|CBQ|chaoshan|cs|2161@ctn|长汀南|CNS|

changtingnan|ctn|2162@cwu|长武|CWY|changwu|cw|2163@cxi|长兴|CBH|changxing|cx|2164@cxi|苍溪|

CXE|cangxi|cx|2165@cya|长阳|CYN|changyang|cy|2166@cya|潮阳|CNQ|chaoyang|cy|2167@czt|城子坦|

CWT|chengzitan|czt|2168@dad|东安东|DCZ|dongandong|dad|2169@dba|德保|RBZ|debao|db|2170@ddh|东戴

河|RDD|dongdaihe|ddh|2171@ddx|丹东西|RWT|dandongxi|ddx|2172@deh|东二道河|DRB|dongerdaohe|dedh|

2173@dfe|大丰|KRQ|dafeng|df|2174@dfn|大方南|DNE|dafangnan|dfn|2175@dgb|东港北|RGT|donggangbei|

dgb|2176@dgs|大孤山|RMT|dagushan|dgs|2177@dgu|东莞|RTQ|dongguan|dg|2178@dhd|鼎湖东|UWQ|

dinghudong|dhd|2179@dhs|鼎湖山|NVQ|dinghushan|dhs|2180@dji|洞井|FWQ|dongjing|dj|2181@dji|垫江|

DJE|dianjiang|dj|2182@dju|大苴|DIM|daju|dj|2183@dli|大荔|DNY|dali|dl|2184@dqg|大青沟|DSD|

daqinggou|dqg|2185@dqi|德清|DRH|deqing|dq|2186@dsn|砀山南|PRH|dangshannan|dsn|2187@dsn|大石头南

|DAL|dashitounan|dstn|2188@dtd|当涂东|OWH|dangtudong|dtd|2189@dtx|大通西|DTO|datongxi|dtx|

2190@dwa|大旺|WWQ|dawang|dw|2191@dxi|德兴|DWG|dexing|dx|2192@dxs|丹霞山|IRQ|danxiashan|dxs|

2193@dyb|大冶北|DBN|dayebei|dyb|2194@dyd|都匀东|KJW|duyundong|dyd|2195@dyn|东营南|DOK|

dongyingnan|dyn|2196@dyu|大余|DYG|dayu|dy|2197@dzd|定州东|DOP|dingzhoudong|dzd|2198@dzh|端州|

WZQ|duanzhou|dz|2199@dzn|大足南|FQW|dazunan|dzn|2200@ems|峨眉山|IXW|emeishan|ems|2201@ezd|鄂州

东|EFN|ezhoudong|ezd|2202@fcb|防城港北|FBZ|fangchenggangbei|fcgb|2203@fcd|凤城东|FDT|

fengchengdong|fcd|2204@fch|富川|FDZ|fuchuan|fc|2205@fcx|繁昌西|PUH|fanchangxi|fcx|2206@fdu|丰都

|FUW|fengdu|fd|2207@flb|涪陵北|FEW|fulingbei|flb|2208@fni|富宁|FNM|funing|fn|2209@fqi|法启|

FQE|faqi|fq|2210@frn|芙蓉南|KCQ|furongnan|frn|2211@fsh|复盛|FAW|fusheng|fs|2212@fso|抚松|FSL|

fusong|fs|2213@fsz|福山镇|FZQ|fushanzhen|fsz|2214@fti|福田|NZQ|futian|ft|2215@fyb|富源北|FBM|

fuyuanbei|fyb|2216@fyu|抚远|FYB|fuyuan|fy|2217@fzd|抚州东|FDG|fuzhoudong|fzd|2218@fzh|抚州|

FZG|fuzhou|fz|2219@gan|高安|GCG|gaoan|ga|2220@gan|广安南|VUW|guangannan|gan|2221@gan|贵安|GAE|

guian|ga|2222@gbd|高碑店东|GMP|gaobeidiandong|gbdd|2223@gch|恭城|GCZ|gongcheng|gc|2224@gdb|贵定

北|FMW|guidingbei|gdb|2225@gdn|葛店南|GNN|gediannan|gdn|2226@gdx|贵定县|KIW|guidingxian|gdx|

2227@ghb|广汉北|GVW|guanghanbei|ghb|2228@gju|革居|GEM|geju|gj|2229@gli|关岭|GLE|guanling|gl|

2230@glx|桂林西|GEZ|guilinxi|glx|2231@gmc|光明城|IMQ|guangmingcheng|gmc|2232@gni|广宁|FBQ|

guangning|gn|2233@gns|广宁寺|GQT|guangningsi|gns|2234@gnx|广南县|GXM|guangnanxian|gnx|2235@gpi|

桂平|GAZ|guiping|gp|2236@gpz|弓棚子|GPT|gongpengzi|gpz|2237@gsh|光山|GUN|guangshan|gs|2238@gtb|

古田北|GBS|gutianbei|gtb|2239@gtb|广通北|GPM|guangtongbei|gtb|2240@gtn|高台南|GAJ|gaotainan|

gtn|2241@gtz|古田会址|STS|gutianhuizhi|gthz|2242@gyb|贵阳北|KQW|guiyangbei|gyb|2243@gyx|高邑

西|GNP|gaoyixi|gyx|2244@han|惠安|HNS|huian|ha|2245@hbd|鹤壁东|HFF|hebidong|hbd|2246@hcg|寒葱

沟|HKB|hanconggou|hcg|2247@hch|霍城|SER|huocheng|hc|2248@hch|珲春|HUL|hunchun|hc|2249@hdd|邯郸

东|HPP|handandong|hdd|2250@hdo|惠东|KDQ|huidong|hd|2251@hdp|哈达铺|HDJ|hadapu|hdp|2252@hdx|海东

西|HDO|haidongxi|hdx|2253@hdx|洪洞西|HTV|hongtongxi|hdx|2254@heb|哈尔滨北|HTB|haerbinbei|hebb|

2255@hfc|合肥北城|COH|hefeibeicheng|hfbc|2256@hfn|合肥南|ENH|hefeinan|hfn|2257@hga|黄冈|KGN|

huanggang|hg|2258@hgd|黄冈东|KAN|huanggangdong|hgd|2259@hgd|横沟桥东|HNN|henggouqiaodong|hgqd|

2260@hgx|黄冈西|KXN|huanggangxi|hgx|2261@hhe|洪河|HPB|honghe|hh|2262@hhn|怀化南|KAQ|

huaihuanan|hhn|2263@hhq|黄河景区|HCF|huanghejingqu|hhjq|2264@hhu|花湖|KHN|huahu|hh|2265@hhu|惠

环|KHQ|huihuan|hh|2266@hhu|后湖|IHN|houhu|hh|2267@hji|怀集|FAQ|huaiji|hj|2268@hkb|河口北|HBM|

hekoubei|hkb|2269@hli|黄流|KLQ|huangliu|hl|2270@hln|黄陵南|VLY|huanglingnan|hln|2271@hme|鲘门|

KMQ|houmen|hm|2272@hme|虎门|IUQ|humen|hm|2273@hmx|侯马西|HPV|houmaxi|hmx|2274@hna|衡南|HNG|

hengnan|hn|2275@hnd|淮南东|HOH|huainandong|hnd|2276@hpu|合浦|HVZ|hepu|hp|2277@hqi|霍邱|FBH|

huoqiu|hq|2278@hrd|怀仁东|HFV|huairendong|hrd|2279@hrd|华容东|HPN|huarongdong|hrd|2280@hrn|华容

南|KRN|huarongnan|hrn|2281@hsb|黄石北|KSN|huangshibei|hsb|2282@hsb|黄山北|NYH|huangshanbei|

hsb|2283@hsd|贺胜桥东|HLN|heshengqiaodong|hsqd|2284@hsh|和硕|VUR|heshuo|hs|2285@hsn|花山南|

KNN|huashannan|hsn|2286@hta|荷塘|KXQ|hetang|ht|2287@hyb|合阳北|HTY|heyangbei|hyb|2288@hyb|海阳

北|HEK|haiyangbei|hyb|2289@hyi|槐荫|IYN|huaiyin|hy|2290@hyk|花园口|HYT|huayuankou|hyk|2291@hzd|

霍州东|HWV|huozhoudong|hzd|2292@hzn|惠州南|KNQ|huizhounan|hzn|2293@jch|泾川|JAJ|jingchuan|jc|

2294@jde|旌德|NSH|jingde|jd|2295@jfe|尖峰|PFQ|jianfeng|jf|2296@jhx|蛟河西|JOL|jiaohexi|jhx|

2297@jlb|军粮城北|JMP|junliangchengbei|jlcb|2298@jle|将乐|JLS|jiangle|jl|2299@jlh|贾鲁河|JLF|

jialuhe|jlh|2300@jls|九郎山|KJQ|jiulangshan|jls|2301@jmb|即墨北|JVK|jimobei|jmb|2302@jnb|建宁县

北|JCS|jianningxianbei|jnxb|2303@jni|江宁|JJH|jiangning|jn|2304@jnx|江宁西|OKH|jiangningxi|

jnx|2305@jox|建瓯西|JUS|jianouxi|jox|2306@jqn|酒泉南|JNJ|jiuquannan|jqn|2307@jrx|句容西|JWH|

jurongxi|jrx|2308@jsh|建水|JSM|jianshui|js|2309@jss|界首市|JUN|jieshoushi|jss|2310@jxb|绩溪北|

NRH|jixibei|jxb|2311@jxd|介休东|JDV|jiexiudong|jxd|2312@jxi|泾县|LOH|jingxian|jx|2313@jxi|靖

西|JMZ|jingxi|jx|2314@jxn|进贤南|JXG|jinxiannan|jxn|2315@jyn|嘉峪关南|JBJ|jiayuguannan|jygn|

2316@jyn|简阳南|JOW|jianyangnan|jyn|2317@jyt|金银潭|JTN|jinyintan|jyt|2318@jyu|靖宇|JYL|

jingyu|jy|2319@jyw|金月湾|PYQ|jinyuewan|jyw|2320@jyx|缙云西|PYH|jinyunxi|jyx|2321@jzh|晋中|

JZV|jinzhong|jz|2322@kfb|开封北|KBF|kaifengbei|kfb|2323@kln|凯里南|QKW|kailinan|kln|2324@klu|库

伦|KLD|kulun|kl|2325@kmn|昆明南|KOM|kunmingnan|kmn|2326@kta|葵潭|KTQ|kuitan|kt|2327@kya|开阳|

KVW|kaiyang|ky|2328@lad|隆安东|IDZ|longandong|lad|2329@lbb|来宾北|UCZ|laibinbei|lbb|2330@lbi|灵

璧|GMH|lingbi|lb|2331@lby|绿博园|LCF|lvboyuan|lby|2332@lcb|隆昌北|NWW|longchangbei|lcb|

2333@lcd|乐昌东|ILQ|lechangdong|lcd|2334@lch|临城|UUP|lincheng|lc|2335@lch|罗城|VCZ|luocheng|

lc|2336@lch|陵城|LGK|lingcheng|lc|2337@lcz|老城镇|ACQ|laochengzhen|lcz|2338@ldb|龙洞堡|FVW|

longdongbao|ldb|2339@ldn|乐都南|LVO|ledunan|ldn|2340@ldn|娄底南|UOQ|loudinan|ldn|2341@ldo|乐

东|UQQ|ledong|ld|2342@ldy|离堆公园|INW|liduigongyuan|ldgy|2343@lfe|陆丰|LLQ|lufeng|lf|2344@lfe|

龙丰|KFQ|longfeng|lf|2345@lfn|禄丰南|LQM|lufengnan|lfn|2346@lfx|临汾西|LXV|linfenxi|lfx|

2347@lgn|临高南|KGQ|lingaonan|lgn|2348@lhe|滦河|UDP|luanhe|lh|2349@lhx|漯河西|LBN|luohexi|lhx|

2350@ljd|罗江东|IKW|luojiangdong|ljd|2351@lji|柳江|UQZ|liujiang|lj|2352@ljn|利津南|LNK|

lijinnan|ljn|2353@lkn|兰考南|LUF|lankaonan|lkn|2354@llb|兰陵北|COK|lanlingbei|llb|2355@llb|龙里

北|KFW|longlibei|llb|2356@llb|沥林北|KBQ|lilinbei|llb|2357@lld|醴陵东|UKQ|lilingdong|lld|

2358@lna|陇南|INJ|longnan|ln|2359@lpn|梁平南|LPE|liangpingnan|lpn|2360@lqu|礼泉|LGY|liquan|lq|

2361@lsd|灵石东|UDV|lingshidong|lsd|2362@lsh|乐山|IVW|leshan|ls|2363@lsh|龙市|LAG|longshi|ls|

2364@lsh|溧水|LDH|lishui|ls|2365@lwj|洛湾三江|KRW|luowansanjiang|lwsj|2366@lxb|莱西北|LBK|

laixibei|lxb|2367@lya|溧阳|LEH|liyang|ly|2368@lyi|临邑|LUK|linyi|ly|2369@lyn|柳园南|LNR|

liuyuannan|lyn|2370@lzb|鹿寨北|LSZ|luzhaibei|lzb|2371@lzh|阆中|LZE|langzhong|lz|2372@lzn|临泽南

|LDJ|linzenan|lzn|2373@mad|马鞍山东|OMH|maanshandong|masd|2374@mch|毛陈|MHN|maochen|mc|

2375@mgd|明港东|MDN|minggangdong|mgd|2376@mhn|民和南|MNO|minhenan|mhn|2377@mji|闵集|MJN|minji|

mj|2378@mla|马兰|MLR|malan|ml|2379@mle|民乐|MBJ|minle|ml|2380@mle|弥勒|MLM|mile|ml|2381@mns|玛

纳斯|MSR|manasi|mns|2382@mpi|牟平|MBK|muping|mp|2383@mqb|闽清北|MBS|minqingbei|mqb|2384@mqb|民

权北|MIF|minquanbei|mqb|2385@msd|眉山东|IUW|meishandong|msd|2386@msh|庙山|MSN|miaoshan|ms|

2387@mxi|岷县|MXJ|minxian|mx|2388@myu|门源|MYO|menyuan|my|2389@myu|暮云|KIQ|muyun|my|2390@mzb|

蒙自北|MBM|mengzibei|mzb|2391@mzh|孟庄|MZF|mengzhuang|mz|2392@mzi|蒙自|MZM|mengzi|mz|2393@nbu|

南部|NBE|nanbu|nb|2394@nca|南曹|NEF|nancao|nc|2395@ncb|南充北|NCE|nanchongbei|ncb|2396@nch|南城

|NDG|nancheng|nc|2397@ncx|南昌西|NXG|nanchangxi|ncx|2398@ndn|宁东南|NDJ|ningdongnan|ndn|

2399@ndo|宁东|NOJ|ningdong|nd|2400@nfb|南芬北|NUT|nanfenbei|nfb|2401@nfe|南丰|NFG|nanfeng|nf|

2402@nhd|南湖东|NDN|nanhudong|nhd|2403@njb|内江北|NKW|neijiangbei|njb|2404@nji|南江|FIW|

nanjiang|nj|2405@njk|南江口|NDQ|nanjiangkou|njk|2406@nli|南陵|LLH|nanling|nl|2407@nmu|尼木|

NMO|nimu|nm|2408@nnd|南宁东|NFZ|nanningdong|nnd|2409@nnx|南宁西|NXZ|nanningxi|nnx|2410@npb|南平

北|NBS|nanpingbei|npb|2411@nxi|南雄|NCQ|nanxiong|nx|2412@nyo|纳雍|NYE|nayong|ny|2413@nyz|南阳寨

|NYF|nanyangzhai|nyz|2414@pan|普安|PAN|puan|pa|2415@pax|普安县|PUE|puanxian|pax|2416@pbi|屏边|

PBM|pingbian|pb|2417@pbn|平坝南|PBE|pingbanan|pbn|2418@pch|平昌|PCE|pingchang|pc|2419@pdi|普

定|PGW|puding|pd|2420@pdu|平度|PAK|pingdu|pd|2421@pko|皮口|PUT|pikou|pk|2422@plc|盘龙城|PNN|

panlongcheng|plc|2423@pni|普宁|PEQ|puning|pn|2424@pnn|平南南|PAZ|pingnannan|pnn|2425@psb|彭山北

|PPW|pengshanbei|psb|2426@psh|坪上|PSK|pingshang|ps|2427@pxb|萍乡北|PBG|pingxiangbei|pxb|

2428@pya|濮阳|PYF|puyang|py|2429@pyc|平遥古城|PDV|pingyaogucheng|pygc|2430@pzh|普者黑|PZM|

puzhehei|pzh|2431@pzh|盘州|PAE|panzhou|pz|2432@pzh|彭州|PMW|pengzhou|pz|2433@qbd|青白江东|QFW|

qingbaijiangdong|qbjd|2434@qdb|青岛北|QHK|qingdaobei|qdb|2435@qdo|祁东|QMQ|qidong|qd|2436@qdu|

青堆|QET|qingdui|qd|2437@qfe|前锋|QFB|qianfeng|qf|2438@qjb|曲靖北|QBM|qujingbei|qjb|2439@qji|曲

江|QIM|qujiang|qj|2440@qli|青莲|QEW|qinglian|ql|2441@qqn|齐齐哈尔南|QNB|qiqihaernan|qqhen|

2442@qsb|清水北|QEJ|qingshuibei|qsb|2443@qsh|青神|QVW|qingshen|qs|2444@qsh|岐山|QAY|qishan|qs|

2445@qsh|庆盛|QSQ|qingsheng|qs|2446@qsx|曲水县|QSO|qushuixian|qsx|2447@qxd|祁县东|QGV|

qixiandong|qxd|2448@qxi|乾县|QBY|qianxian|qx|2449@qya|祁阳|QWQ|qiyang|qy|2450@qzn|全州南|QNZ|

quanzhounan|qzn|2451@qzw|棋子湾|QZQ|qiziwan|qzw|2452@rbu|仁布|RUO|renbu|rb|2453@rcb|荣昌北|

RQW|rongchangbei|rcb|2454@rch|荣成|RCK|rongcheng|rc|2455@rdo|如东|RIH|rudong|rd|2456@rji|榕江|

RVW|rongjiang|rj|2457@rkz|日喀则|RKO|rikaze|rkz|2458@rpi|饶平|RVQ|raoping|rp|2459@scl|宋城路|

SFF|songchenglu|scl|2460@sdh|三道湖|SDL|sandaohu|sdh|2461@sdo|邵东|FIQ|shaodong|sd|2462@sdx|三

都县|KKW|sanduxian|sdx|2463@sfa|胜芳|SUP|shengfang|sf|2464@sfb|双峰北|NFQ|shuangfengbei|sfb|

2465@she|商河|SOK|shanghe|sh|2466@sho|泗洪|GQH|sihong|sh|2467@shu|四会|AHQ|sihui|sh|2468@sjn|三

江南|SWZ|sanjiangnan|sjn|2469@sjz|三井子|OJT|sanjingzi|sjz|2470@slc|双流机场|IPW|

shuangliujichang|sljc|2471@slx|双流西|IQW|shuangliuxi|slx|2472@slx|石林西|SYM|shilinxi|slx|

2473@smb|三明北|SHS|sanmingbei|smb|2474@smi|嵩明|SVM|songming|sm|2475@sml|树木岭|FMQ|

shumuling|sml|2476@snq|苏尼特左旗|ONC|sunitezuoqi|sntzq|2477@spd|山坡东|SBN|shanpodong|spd|

2478@sqi|石桥|SQE|shiqiao|sq|2479@sqi|沈丘|SQN|shenqiu|sq|2480@ssb|鄯善北|SMR|shanshanbei|ssb|

2481@ssb|狮山北|NSQ|shishanbei|ssb|2482@ssb|三水北|ARQ|sanshuibei|ssb|2483@ssh|狮山|KSQ|

shishan|ss|2484@ssn|三水南|RNQ|sanshuinan|ssn|2485@ssn|韶山南|INQ|shaoshannan|ssn|2486@ssu|三穗

|QHW|sansui|ss|2487@sti|石梯|STE|shiti|st|2488@swe|汕尾|OGQ|shanwei|sw|2489@sxb|歙县北|NPH|

shexianbei|sxb|2490@sxb|绍兴北|SLH|shaoxingbei|sxb|2491@sxd|绍兴东|SSH|shaoxingdong|sxd|

2492@sxi|泗县|GPH|sixian|sx|2493@sxi|始兴|IPQ|shixing|sx|2494@sya|泗阳|MPH|siyang|sy|2495@syb|

邵阳北|OVQ|shaoyangbei|syb|2496@syb|松原北|OCT|songyuanbei|syb|2497@syi|山阴|SNV|shanyin|sy|

2498@syn|沈阳南|SOT|shenyangnan|syn|2499@szb|深圳北|IOQ|shenzhenbei|szb|2500@szh|神州|SRQ|

shenzhou|sz|2501@szs|深圳坪山|IFQ|shenzhenpingshan|szps|2502@szs|石嘴山|QQJ|shizuishan|szs|

2503@szx|石柱县|OSW|shizhuxian|szx|2504@tcb|桃村北|TOK|taocunbei|tcb|2505@tdb|田东北|TBZ|

tiandongbei|tdb|2506@tdd|土地堂东|TTN|tuditangdong|tdtd|2507@tgx|太谷西|TIV|taiguxi|tgx|

2508@tha|吐哈|THR|tuha|th|2509@tha|通海|TAM|tonghai|th|2510@thc|天河机场|TJN|tianhejichang|

thjc|2511@thj|天河街|TEN|tianhejie|thj|2512@thx|通化县|TXL|tonghuaxian|thx|2513@tji|同江|TJB|

tongjiang|tj|2514@tlb|铜陵北|KXH|tonglingbei|tlb|2515@tlb|吐鲁番北|TAR|tulufanbei|tlfb|

2516@tni|泰宁|TNS|taining|tn|2517@trn|铜仁南|TNW|tongrennan|trn|2518@txd|田心东|KQQ|

tianxindong|txd|2519@txh|汤逊湖|THN|tangxunhu|txh|2520@txi|藤县|TAZ|tengxian|tx|2521@tyn|太原南

|TNV|taiyuannan|tyn|2522@tyx|通远堡西|TST|tongyuanpuxi|typx|2523@wdd|文登东|WGK|wendengdong|

wdd|2524@wfs|五府山|WFG|wufushan|wfs|2525@whb|威虎岭北|WBL|weihulingbei|whlb|2526@whb|威海北|

WHK|weihaibei|whb|2527@wld|五龙背东|WMT|wulongbeidong|wlbd|2528@wln|乌龙泉南|WFN|

wulongquannan|wlqn|2529@wlq|乌鲁木齐|WAR|wulumuqi|wlmq|2530@wns|五女山|WET|wunvshan|wns|

2531@wsh|武胜|WSE|wusheng|ws|2532@wwe|无为|IIH|wuwei|ww|2533@wws|瓦屋山|WAH|wawushan|wws|

2534@wxx|闻喜西|WOV|wenxixi|wxx|2535@wyb|武义北|WDH|wuyibei|wyb|2536@wyb|武夷山北|WBS|

wuyishanbei|wysb|2537@wyd|武夷山东|WCS|wuyishandong|wysd|2538@wyu|婺源|WYG|wuyuan|wy|2539@wyu|

渭源|WEJ|weiyuan|wy|2540@wzb|万州北|WZE|wanzhoubei|wzb|2541@wzh|武陟|WIF|wuzhi|wz|2542@wzn|梧州

南|WBZ|wuzhounan|wzn|2543@xab|兴安北|XDZ|xinganbei|xab|2544@xcd|许昌东|XVF|xuchangdong|xcd|

2545@xch|项城|ERN|xiangcheng|xc|2546@xdd|新都东|EWW|xindudong|xdd|2547@xfe|西丰|XFT|xifeng|xf|

2548@xfe|先锋|NQQ|xianfeng|xf|2549@xfl|湘府路|FVQ|xiangfulu|xfl|2550@xfx|襄汾西|XTV|

xiangfenxi|xfx|2551@xgb|孝感北|XJN|xiaoganbei|xgb|2552@xgd|孝感东|GDN|xiaogandong|xgd|2553@xhd|

西湖东|WDQ|xihudong|xhd|2554@xhn|新化南|EJQ|xinhuanan|xhn|2555@xhx|新晃西|EWQ|xinhuangxi|xhx|

2556@xji|新津|IRW|xinjin|xj|2557@xjk|小金口|NKQ|xiaojinkou|xjk|2558@xjn|新津南|ITW|xinjinnan|

xjn|2559@xnd|咸宁东|XKN|xianningdong|xnd|2560@xnn|咸宁南|UNN|xianningnan|xnn|2561@xpn|溆浦南|

EMQ|xupunan|xpn|2562@xtb|湘潭北|EDQ|xiangtanbei|xtb|2563@xtd|邢台东|EDP|xingtaidong|xtd|

2564@xwq|西乌旗|XWC|xiwuqi|xwq|2565@xwx|修武西|EXF|xiuwuxi|xwx|2566@xxb|萧县北|QSH|

xiaoxianbei|xxb|2567@xxd|新乡东|EGF|xinxiangdong|xxd|2568@xyb|新余北|XBG|xinyubei|xyb|2569@xyc|

西阳村|XQF|xiyangcun|xyc|2570@xyd|信阳东|OYN|xinyangdong|xyd|2571@xyd|咸阳秦都|XOY|

xianyangqindu|xyqd|2572@xyo|仙游|XWS|xianyou|xy|2573@xzc|新郑机场|EZF|xinzhengjichang|xzjc|

2574@xzl|香樟路|FNQ|xiangzhanglu|xzl|2575@ybl|迎宾路|YFW|yingbinlu|ybl|2576@ycb|永城北|RGH|

yongchengbei|ycb|2577@ycb|运城北|ABV|yunchengbei|ycb|2578@ycd|永川东|WMW|yongchuandong|ycd|

2579@ych|宜春|YEG|yichun|yc|2580@ych|岳池|AWW|yuechi|yc|2581@ydh|云东海|NAQ|yundonghai|ydh|

2582@ydu|姚渡|AOJ|yaodu|yd|2583@yfd|云浮东|IXQ|yunfudong|yfd|2584@yfn|永福南|YBZ|yongfunan|

yfn|2585@yge|雨格|VTM|yuge|yg|2586@yhe|洋河|GTH|yanghe|yh|2587@yjb|永济北|AJV|yongjibei|yjb|

2588@yji|弋江|RVH|yijiang|yj|2589@yjp|于家堡|YKP|yujiapu|yjp|2590@yjx|延吉西|YXL|yanjixi|yjx|

2591@ykn|永康南|QUH|yongkangnan|ykn|2592@ylh|运粮河|YEF|yunlianghe|ylh|2593@yli|炎陵|YAG|

yanling|yl|2594@yln|杨陵南|YEY|yanglingnan|yln|2595@ymi|伊敏|YMX|yimin|ym|2596@yna|郁南|YKQ|

yunan|yn|2597@ypi|银瓶|KPQ|yinping|yp|2598@ysh|永寿|ASY|yongshou|ys|2599@ysh|阳朔|YCZ|

yangshuo|ys|2600@ysh|云山|KZQ|yunshan|ys|2601@ysn|玉山南|YGG|yushannan|ysn|2602@yta|永泰|YTS|

yongtai|yt|2603@yta|银滩|CTQ|yintan|yt|2604@ytb|鹰潭北|YKG|yingtanbei|ytb|2605@ytn|烟台南|YLK|

yantainan|ytn|2606@yxi|尤溪|YXS|youxi|yx|2607@yxi|云霄|YBS|yunxiao|yx|2608@yxi|宜兴|YUH|

yixing|yx|2609@yxi|玉溪|AXM|yuxi|yx|2610@yxi|阳信|YVK|yangxin|yx|2611@yxi|应县|YZV|yingxian|

yx|2612@yxn|攸县南|YXG|youxiannan|yxn|2613@yyb|余姚北|CTH|yuyaobei|yyb|2614@zan|诏安|ZDS|

zhaoan|za|2615@zdc|正定机场|ZHP|zhengdingjichang|zdjc|2616@zfd|纸坊东|ZMN|zhifangdong|zfd|

2617@zhb|庄河北|ZUT|zhuanghebei|zhb|2618@zhu|昭化|ZHW|zhaohua|zh|2619@zjb|织金北|ZJE|

zhijinbei|zjb|2620@zji|芷江|ZPQ|zhijiang|zj|2621@zji|织金|IZW|zhijin|zj|2622@zka|仲恺|KKQ|

zhongkai|zk|2623@zko|曾口|ZKE|zengkou|zk|2624@zli|左岭|ZSN|zuoling|zl|2625@zmd|樟木头东|ZRQ|

zhangmutoudong|zmtd|2626@zmx|驻马店西|ZLN|zhumadianxi|zmdx|2627@zpu|漳浦|ZCS|zhangpu|zp|

2628@zqd|肇庆东|FCQ|zhaoqingdong|zqd|2629@zqi|庄桥|ZQH|zhuangqiao|zq|2630@zsh|昭山|KWQ|

zhaoshan|zs|2631@zsx|钟山西|ZAZ|zhongshanxi|zsx|2632@zxi|漳县|ZXJ|zhangxian|zx|2633@zyb|资阳

北|FYW|ziyangbei|zyb|2634@zyx|张掖西|ZEJ|zhangyexi|zyx|2635@zzb|资中北|WZW|zizhongbei|zzb|

2636@zzd|涿州东|ZAP|zhuozhoudong|zzd|2637@zzd|枣庄东|ZNK|zaozhuangdong|zzd|2638@zzd|卓资东|

ZDC|zhuozidong|zzd|2639@zzd|郑州东|ZAF|zhengzhoudong|zzd|2640@zzn|株洲南|KVQ|zhuzhounan|zzn|

2641';
'''

'''
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.baidu.com/")
'''

'''
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.baidu.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("Nirvana")
driver.find_element_by_id("search_button_homepage").click()
print(driver.current_url)
driver.quit()
'''

'''
from selenium import webdriver
import time
 
browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/#signin')
browser.find_element_by_name("account").send_keys("input your account")
browser.find_element_by_name("password").send_keys("input your password")
time.sleep(7)
browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/form/div[2]/button").click()
'''
'''
import urllib.request as ur
import random

url=r'http://www.bilibili.com/'
proxy='27.222.106.22:80'

proxy_support=ur.ProxyHandler({'http:':proxy})#使用代理ip
opener=ur.build_opener(proxy_support)#私人订制ip
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]

ur.install_opener(opener)
response =ur.urlopen(url)

html=response.read().decode('utf-8')
print(html)
'''

import cv2
from PIL import Image
import os
os.chdir(r'C:\Users\Administrator\Desktop\新建文件夹 (5)')

def video_to_frame(videofile):
    video_cap = cv2.VideoCapture(videofile)
    frame_count = 0
    while (video_cap.isOpened()):
        print('frame %d' % frame_count)
        ret, frame = video_cap.read()
        if ret is False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        cv2.imwrite("frame%d.png" % frame_count, frame)
        frame_count += 1
    return frame_count

def resize_frame(img):
    return Image.open(img, 'r').convert("L").resize(size)

def frame_to_char(frame_num):
    gray_char=['@','#','$','%','&','?','*','o','/','{','[','(',
               '|','!','^','~','-','_',':',';',',','.','`',' ']
    text = open("text1.txt", "w")
    for i in range(frame_num):
        frame = resize_frame('frame%d.png' % i)
        for y in range(size[1]):
            for x in range(size[0]):
                gray = frame.getpixel((x,y))
                char = gray_char[int(gray/(255/(len(gray_char)-1)))]
                text.write(char)
            text.write("\n")
        print("writing frame %d"%i)
    text.close()
    print('Done!')

if __name__ == '__main__':
    size = (236, 61) #size of output frame (x,y)
    nframe = video_to_frame(r'C:\Users\Administrator\Desktop\HTML视频\42.flv') #video to convert
    frame_to_char(nframe)

import time
import colorconsole.terminal
import os
os.chdir(r'C:\Users\Administrator\Desktop\新建文件夹 (5)')

text = open(r"text1.txt", "r")
size = (236, 61)
line_count = 1
frame = ""
for line in text:
    frame = frame + line
    if line_count % size[1] == 0:
        print(frame)
        frame = ""
        time.sleep(0.0278) # interval per frame
        colorconsole.terminal.get_terminal().gotoXY(0,0)
    line_count += 1
