import cv2

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()

    if ret == False:
        continue
        
    cv2.imshow("Camera Image",frame)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break




cv2.waitKey(0) 
cv2.destroyAllWindows()
cap.release()









# import cv2

# cap = cv2.VideoCapture(0)


# while True:
#     ret,frame = cap.read()
    
#     if ret == False:
#         continue
    
#     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Video Capture',frame)
#     cv2.imshow('Gray Video Capture',gray_frame)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()
