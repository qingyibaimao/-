import cv2
url = "rtsp://admin:TH-my@002714.com@172.17.14.242"
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()