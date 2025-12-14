import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#1.paint the image 
#blank[200:300,300:400]=0,0,255
#cv.imshow('green',blank)

#drew rectangle
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,250,0),thickness=-1)
#cv.imshow('rectangle',blank)

#drew cercle
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)

#drew line
#cv.line(blank,(100,250),(300,400),(255,250,255),thickness=3)
#cv.imshow('line',blank)

#text on image
cv.putText(blank,'Hellow I am Nadhun',(0,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),3)
cv.imshow('text',blank)

cv.waitKey(0)
