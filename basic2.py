import cv2 as cv # type: ignore

# Use raw string (r'...') to avoid backslash issues
img = cv.imread(r'C:\Users\Nadhu\OneDrive\Pictures\CAT.jpg')
 cv.imshow('Cat', img)

