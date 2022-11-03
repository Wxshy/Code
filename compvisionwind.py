import cv2

faceCascade = cv2.CascadeClassifier('C:/Users/samue/Desktop/Code/haarcascade_frontalface_default.xml')

faceimg = cv2.imread('C:/Users/samue/Downloads/20170625_200858000_iOS.jpg')

faceGood = faceimg
cv2.imshow('faces', faceimg)

grey = cv2.cvtColor(faceGood, cv2.COLOR_BGR2GRAY)

cv2.imshow('face', grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

faces = faceCascade.detectMultiScale(grey, scaleFactor = 1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(faceGood, (x,y), (x+w, y+h), (0,255,0), 3)



cv2.imshow('', img)
