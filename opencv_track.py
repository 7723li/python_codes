import argparse,datetime,imutils,time,cv2

ap= argparse.ArgumentParser()
ap.add_argument("-v","--video",help="path to the video file")#--video，是可选的。它会指定一个路径，指向一个预先录制好的视频文件
ap.add_argument("-a","--min-area",type=int,default=500,help="minimum area size")#它表示一个图像区域被看做实际运动的最小尺寸
args=vars(ap.parse_args())
print(args)

# 如果video参数为None，那么我们从摄像头读取数据
if args.get("video",None) is None:
	camera=cv2.VideoCapture(0)
	time.sleep(0.25)
# 否则我们读取一个视频文件
else:
	camera=cv2.VideoCapture(args["video"])
#频的第一帧不会包含运动，而仅仅是背景——因此我们可以使用第一帧来建立背景模型
firstframe=None

while True:
	grabbed,frame=camera.read()
	text='Unoccupied'#空闲的;空的; 未被占用的;未被占领的
	if not grabbed:
		break

	# 调整该帧的大小，转换为灰阶图像并且对其进行高斯模糊
	frame=imutils.resize(frame,width=500)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#应用高斯平滑对一个21X21的区域的像素强度进行平均。
	#这能帮我们滤除可能使我们运动检测算法失效的高频噪音。
	gray=cv2.GaussianBlur(gray,(21,21),0)

	# 如果第一帧是None，对其进行初始化,初始化后不再改变，是为静止的背景图片
	if firstframe is None:
		firstframe =gray
		continue

	# 计算当前帧和第一帧的不同
	# 计算两帧的不同是一个简单的减法，我们使用两方相应的像素强度差的绝对值。
	# delta = |background_model – current_frame|
	frameDelta = cv2.absdiff(firstframe,gray)
	#对frameDelta进行阀值化来显示图片中像素强度值有显著变化的区域。
	#如果差值小于25，我丢弃该像素将其设置为黑色（例如，背景）。
	#如果差值大于25，我们将其设定为白色（例如，前景）
	thresh = cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]

	# 扩展阀值图像填充孔洞，然后找到阀值图像上的轮廓
	thresh = cv2.dilate(thresh,None,iterations=2)
	#有了这个阀值化的图片，只要简单的进行实施轮廓检测来找到白色区域的外轮廓线
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# 遍历轮廓
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args['min_area']:
			continue
        # and update the text
        # 计算轮廓的边界框，在当前帧中画出该框
        # 如果轮廓面积比我们提供的--min-area值大，我们会在前景和移动区域画边框线
		(x, y, w, h)=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+2,y+h),(0, 255, 0), 2)
		text = "Occupied"

	# 在当前帧上写文字以及时间戳
	cv2.putText(frame,"Room Status: {}".format(text),(10,20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
    	(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) &amp; 0xFF

	# 如果q键被按下，跳出循环
	if key == ord("q"):
		break

# 清理摄像机资源并关闭打开的窗口
camera.release()
cv2.destroyAllWindows()