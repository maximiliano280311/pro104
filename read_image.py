import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Mostrar image",img)

print(img)

cv2.waitKey(5000)