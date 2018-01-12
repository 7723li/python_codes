import os
import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

phname = 'adb.png'
shot_path = r'sdcard'
save_path = os.getcwd()

def com_exe(com): # 执行命令行命令
    return subprocess.getoutput(com)

def init():
    os.chdir(save_path)
    print(com_exe('adb start-server'))

def screen_shot():
    print(com_exe('adb shell screencap -p '+'/'+shot_path +'/'+phname))
    print(com_exe('adb pull '+'/'+ shot_path+'/'+phname))
    return Image.open(save_path+'\\'+phname)

def jump(x,y,time):
    com_exe('adb shell input swipe {} {} {} {} {}' .format(x,y,x,y,time))

def count_distance():
    pass

def main():
    fig = plt.figure()
    img = np.array( screen_shot() )
    im = plt.imshow(img, animated = True)

def over():
    print(com_exe('adb kill-server'))
    

if __name__ == "__main__":
    init()
    main()
    over()
