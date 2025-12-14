import cv2 as cv
img=cv.imread(r'C:\Users\Nadhu\OneDrive\Pictures\CAT.jpg')
cv.imshow('cat',img)

#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge Cascode
canny=cv.Canny(img,125,175)
cv.imshow('canny Edges',canny)

#Dialating image
dialated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dialated',dialated)

#Eroading
eroded=cv.erode(dialated,(3,3),iterations=1)
cv.imshow('eroaded',eroded)

#Resize

Resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',Resized)

#Croping

croped=img[50:200,200:400]
cv.imshow('croped',croped)


cv.waitKey(0)