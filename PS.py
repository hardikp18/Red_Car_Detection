import cv2
import numpy as np
import statistics
import math

# Video given downloaded and saved as video.mp4 in directory 
cap=cv2.VideoCapture("video.mp4")
count=0
valid_counters = []
area_counters=[]
rect_area=[]



j=0
dist=[]

# Loop will run till you press key q
while cap.isOpened():
    success,rframe=cap.read()
    
    if success==0:
        break
    frame=cv2.resize(rframe,(640,480))
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Lower limit of Red
    lower_red=np.array([161,155,60])
    
    #Upper limit of Red
    upper_red=np.array([179,255,255])
    
    # Mask is created from limits and HSV image
    red_mask=cv2.inRange(hsv,lower_red,upper_red)
    red_color=cv2.bitwise_and(frame,frame,mask=red_mask)
    
    gray_color=cv2.cvtColor(red_color,cv2.COLOR_BGR2GRAY)
    
     
    
    # Performing thresholding
    ret,thresh=cv2.threshold(gray_color,30,255,cv2.THRESH_BINARY)
    
    
    # apply image dilation
    kernel = np.ones((3,3),np.uint8)
    dilated = cv2.dilate(thresh,kernel,iterations = 1)
    
    #applying gaussian blur
    blurred_video=cv2.GaussianBlur(dilated,(5,5),0)

    contours,hierarchy=cv2.findContours(blurred_video,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    
    
    
    for i,cntr in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cntr)
        if (x <= 320) & (y >= 240)& (y <= 480)&(cv2.contourArea(cntr) >= 360)& (cv2.contourArea(cntr) <= 480):
            
            valid_counters.append(cntr)
            area_counters.append(cv2.contourArea(cntr))
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            # point=[]
            # point.append([x+(w/2),y+(h/2)])
            # if(len(point)>=1):
            #     dist=math.dist(point[len(point)],point[len(point)-1])
            #     print(dist)
              
                       

            # rect_area.append(w*h)
            count=count+1
              
    
    """
        To find total count we can find the center in each frame and see if that distance between two
        consecutive center of contours are greater than given contour only then increase count
    """
    # cv2.drawContours(frame,cntr,-1,(0,255,0),3)
    # cv2.drawContours(gray_color,contours,-1,(0,255,0),3)
    
    
    
    cv2.line(frame,(320,480),(320,0),(255,0,0),5)
    #To show that red cars are only detected in the green box given
    
    cv2.line(frame,(320,240),(320,480),(0,255,0),3)
    cv2.line(frame,(0,240),(320,240),(0,255,0),3)
    
    cv2.imshow("Original Frame",frame)
    
    
    # cv2.imshow("Gray Frame",gray_color)
    
    
    
     # Stop if q key is pressed
    k=cv2.waitKey(5) & 0xff
    if k==ord('q'):
        break
# print("Max Area-",max(area_counters))
# print("Min Area-",min(area_counters))
print('Total number of cars*number of frames car was detected in-',count)

# print('Median-',statistics.median(area_counters))
# print('Mode-',statistics.mode(area_counters))
# avg=np.average(area_counters)
# print("The average is",avg)

cv2.destroyAllWindows()
   
    
    
    
    
    
    
    