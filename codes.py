import pyzbar.pyzbar as pyz
import cv2

    img = cv2.imread('C:/Users/samue/Desktop/Code/vossbc.png')

barcodes = pyz.decode(img)

for barcode in barcodes:
    x,y,w,h = barcode.rect
    cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 2)

    bdata = barcode.data.decode('utf-8')

cv2.imshow('',img)
cv2.waitKey(0)
print(bdata)
