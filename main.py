import cv2
vcap = cv2.VideoCapture("rtsp://admin:admin@172.30.2.6/H264?ch=0&subtype=0")

while(1):

    ret, frame = vcap.read()
    if not ret:
        break
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)

vcap.release()
cv2.destroyAllWindows()
