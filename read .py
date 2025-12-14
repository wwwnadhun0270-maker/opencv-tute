import cv2 as cv # type: ignore

# Use raw string (r'...') to avoid backslash issues
img = cv.imread(r'C:\Users\Nadhu\OneDrive\Pictures\CAT.jpg')

if img is None:
    print("Image not found. Check the path!")
else:
    cv.imshow('Cat', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
