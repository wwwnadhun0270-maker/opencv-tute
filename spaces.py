import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread(r'C:\Users\Nadhu\OneDrive\Pictures\CAT.jpg')
cv.imshow('cat',img)

# Convert BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.axis('on')   # axis hide (optional)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# #BGR to HSV
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# #BGR to L*A*V

# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)

# cv.waitKey(0)