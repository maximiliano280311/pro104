import cv2

img = cv2.imread("poster.jpg")

rocket = img[120:280,400:500]
img[30:190,480:580] = rocket

text_to_show = "Me encanta programar"

cv2.putText(img,
             text_to_show,
             (20,200),
             fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
             fontScale = 1,
             color = (0,0.255)
             )

cv2.imshow("output",img)

cv2.waitKey(0)