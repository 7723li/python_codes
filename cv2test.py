print(ord('🕊'))
# from VideoCapture import Device
# import time,cv2,sys
# import numpy as np
# def test():
# 	cap=cv2.VideoCapture(0)
# 	video=cv2.VideoWriter('test.mkv',cv2.VideoWriter_fourcc(*'XVID'),10.0,(640,480))
# 	now=time.time()
# 	while time.time()-now<=60:
# 		ret,img=cap.read()
# 		video.write(img)
# 		cv2.imshow('test',img)
# 		key=cv2.waitKey(1)
# 		#cv2.imwrite('%s.jpg' % int(time.time()),img)
# 		if key==ord('q'):
# 			break
# 	video.release()
# 	cv2.destroyAllWindows()

# def face_test():
#         cv2.namedWindow('test')
#         cap=cv2.VideoCapture(0)
#         success,frame=cap.read()
#         #cam=Device()
#         #frame=np.array(cam.getImage())
#         color = (0,0,0)#设置人脸框的颜色
#         classfier=cv2.CascadeClassifier(r"D:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")#定义分类器
#         video=cv2.VideoWriter('test.mkv',cv2.VideoWriter_fourcc(*'XVID'),10.0,(640,480))
#         while True:
#                 success,frame=cap.read()
#                 #frame=cv2.cvtColor(np.array(cam.getImage()),cv2.COLOR_RGB2BGR)
#                 size=frame.shape[:2]#获得当前桢彩色图像的大小
#                 image=np.zeros(size,dtype=np.float16)#定义一个与当前桢图像大小相同的的灰度图像矩阵
#                 image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#将当前桢图像转换成灰度图像（这里有修改）
#                 cv2.equalizeHist(image, image)#灰度图像进行直方图等距化
#                 #如下三行是设定最小图像的大小
#                 divisor=8
#                 h, w = size
#                 minSize=(int(w/divisor), int(h/divisor))#这里加了一个取整函数
#                 faceRects = classfier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)#人脸检测
#                 if len(faceRects)>0:#如果人脸数组长度大于0
#                     for faceRect in faceRects: #对每一个人脸画矩形框
#                             x, y, w, h = faceRect
#                             cv2.rectangle(frame, (x, y), (x+w, y+h), color)
#                 cv2.imshow("test", frame)#显示图像
#                 video.write(frame)
#                 key=cv2.waitKey(10)
#                 c = chr(key & 255)
#                 if c in ['q', 'Q', chr(27)]:
#                     break
#         video.release()
#         cv2.destroyWindow("test")
    
# face_test()
# sys.exit()
