import numpy as np
import cv2
image = cv2.imread("testfile.jpg")
wide = 25
f = float(wide) / image.shape[1]
new_size = (wide,int(image.shape[0] * f))
print(new_size)
res = cv2.resize(image,new_size,interpolation=cv2.INTER_AREA)
cv2.imshow("Resize image",res)
crop = res[50:100, 150:200]
cv2.imshow("CropImage",crop)
cv2.waitKey(0)
