import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))

cv2.putText(img,"Mercury",(110,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Venus",(200,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Earth",(300,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mars",(400,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Jupiter",(570,40),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(750,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Uranus",(950,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune",(1100,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("output",img)

cv2.waitKey(0)