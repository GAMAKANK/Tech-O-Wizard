#video streaming
#live video will be coming from phone through the given url
import cv2

cap=cv2.VideoCapture("http://10.1.3.19:8080/video")

while True :
    _, frame=cap.read()
    

    cv2.imshow('livestream',frame)

    if cv2.waitKey(1)==ord('q'):  #press q to exit the video streaming
        break

cap.release()
cv2.destroyAllWindows    



