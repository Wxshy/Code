import time, cv2

firstframe = None
video = cv2.VideoCapture(0)


while True:
    #getting the webcam footage
    check, frame = video.read()
    #converts to greyscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gaussian blur
    grey = cv2.GaussianBlur(grey, (21,21),0)
    if firstframe is None:
        firstframe = grey


    delta_frame = cv2.absdiff(firstframe, grey)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),3)

    cv2.imshow('thresh', thresh_delta)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    
