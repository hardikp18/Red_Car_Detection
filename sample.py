import cv2

cap = cv2.VideoCapture('video.mp4')



while cap.isOpened():
    success,frame=cap.read()
    gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not success:
        print("Not Succesful")
        break
    cv2.imshow('Video',gray_frame)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break