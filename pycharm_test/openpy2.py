import cv2


img_color = cv2.imread('cat.png', cv2.IMREAD_COLOR)

# cv2.namedWindow('show img1')
cv2.imshow('show img1', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGRA2GRAY)

cv2.imshow('show img2', img_gray)
cv2.waitKey(0)






