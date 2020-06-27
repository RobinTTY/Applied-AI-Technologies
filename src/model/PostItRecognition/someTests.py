import cv2

img = cv2.imread('test.png', 1)
cv2.imshow("img", img)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(1, 1))
cl = clahe.apply(l)

limg = cv2.merge((cl, a, b))
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
