from tkinter import *
from tkinter import messagebox
import sys
from random import randint

#地图类 方块类 蛇类 主函数
class Grid(object):
    def __init__(self,master=None,window_width=500,window_height=400,grid_width=20,offset=10):
        self.width=window_width
        self.height=window_height
        self.grid_width=grid_width#方块大小
        self.offset=offset#偏移
        self.grid_x=int(self.width / self.grid_width)
        self.grid_y=int(self.height / self.grid_width)
        self.grid_list()
        self.bg='white'
        #默认原点在左上角
        self.canvas=Canvas(master,width=self.width+2*self.offset,height=self.height+2*self.offset,bg=self.bg)
        self.canvas.pack()

    def draw(self,pos,color):#显示小方块的位置
        x=pos[0]*self.grid_width+self.offset
        y=pos[1]*self.grid_width+self.offset
        self.canvas.create_rectangle(x,y,x+self.grid_width+self.offset,y+self.grid_width+self.offset,fill=color,outline=self.bg)

    def grid_list(self):
        #获取所有的坐标
        grid_list=[]
        for y in range(0,self.grid_y):
            for x in range(0,self.grid_x):
                grid_list.append((x,y))
        self.grid_list=grid_list

class Food(object):
    def __init__(self,Grid):
        self.grid=Grid
        self.color='black'
        self.set_pos()
        self.display()

    def set_pos(self):
        x=randint(0,self.grid.grid_x-1)
        y=randint(0,self.grid.grid_y-1)
        self.pos=(x,y)

    def display(self):
        #显示方块
        self.grid.draw(self.pos,self.color)

class Snake(object):
    def __init__(self,Grid):
        self.grid=Grid
        self.body=[(10,6),(10,7),(10,8)]
        self.direction='up'#方向
        self.status=['run','stop']#运行状态
        self.speed=1000#运行速度
        self.color='red'
        self.food=Food(self.grid)
        self.gameover=False
        self.score=0

    def available_grid(self):
        #获取所有可用的坐标
        return [i for i in self.grid.grid_list if i not in self.body[2:]]

    def change_direction(self,direction):
        #改变运行方向
        self.direction=direction

    def display(self):
        #显示蛇的位置
        for x,y in self.body:
            self.grid.draw((x,y),self.color)

    def display_food(self):
        #排除食物出现在蛇的位置
        while(self.food.pos in self.body):
            self.food.set_pos()
        self.food.display()

    def move(self):
        head=self.body[0]
        if self.direction=='up':
            new=(head[0],head[1]-1)
        elif self.direction=='down':
            new=(head[0],head[1]-1)
        elif self.direction=='left':
            new=(head[0]-1,head[1])
        else:
            new=(head[0]+1,head[1])

        if not self.food.pos == head:#没有吃的不加长，删除最后一个元素
            pop=self.body.pop()
            self.grid.draw(pop,self.grid.bg)
        else:
            self.display_food()
            self.score+=1

        self.body.insert(0,new)

        if new not in self.available_grid():#如果新的坐标不在可出现位置，游戏结束
            self.status.reverse()
            self.gameover=True
        else:
            self.grid.draw(new,color=self.color)#显示新坐标

class SnakeGame(Frame):
    def __init__(self,master=None,*args,**kwargs):
        Frame.__init__(self,master)
        self.grid=Grid(master=master,*args,**kwargs)
        self.snake=Snake(self.grid)
        self.bind_all('<KeyRelease>',self.key_release)

    def run(self):
        if not self.snake.status[0]=='stop':
            self.snake.move()
        if self.snake.gameover==True:
            message=messagebox.showinfo('GameOver','your score:{}'.format(self.snake.score))
            if message=='ok':
                sys.exit()
        self.after(self.snake.speed)#刷新速度

    def key_release(self,event):
        key=event.keysym
        key_dict={'up':'down','dowm':'up','left':'right','right':'left'}
        #不可控制向正在运行的反方向运动
        if key in key_dict and not key == key_dict[self.snake.direction]:
            self.snake.change_direction(key)
            self.snake.move()
        
if __name__ == '__main__':
    root=Tk()
    root.title('贪吃蛇')
    snakegame=SnakeGame(root)
    snakegame.run()
    snakegame.mainloop()
    
    
