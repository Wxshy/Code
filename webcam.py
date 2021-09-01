import cv2, time, random

faceCascade = cv2.CascadeClassifier('C:/Users/samue/Desktop/Code/haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

def pic(img):
    cv2.putText(img, rndm, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 3)
    cv2.imshow('AGE', img)


a = 1
start = time.perf_counter()
while True:
    a += 1
    check, frame = video.read()
    key = cv2.waitKey(1)

    img = frame
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    grey = cv2.GaussianBlur(grey, (21,21), 0)

    try:
        frameDelta = cv2.absdiff(prev_frame, grey)
    except Exception:
        pass
    
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    prev_frame = grey

    cv2.imshow('hello', grey)

    if key == ord('q'):
        break

end = time.perf_counter()

video.release()
cv2.destroyAllWindows()
print('Frames Captured:', a)
print('Time Elapsed:', str(end-start)+'s')

