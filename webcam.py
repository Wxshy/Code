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
    faces = faceCascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors=5)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        if key == ord('a'):
            pic(img)
        rndm = str('AGE: ' + str(random.randint(1,100)) + 'YEARS')
        cv2.putText(img, rndm, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 3)

    cv2.imshow('Capturing', img)

    

    if key == ord('q'):
        break

end = time.perf_counter()

video.release()
cv2.destroyAllWindows()
print('Frames Captured:', a)
print('Time Elapsed:', str(end-start)+'s')
time.sleep(30)
