import cv2
 
# 读取图像
image = cv2.imread('.\images\idol.png')
 
# 指定新的分辨率大小
width = 192
height = 192
 
# 修改图像分辨率
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
 
# 保存修改后的图像
cv2.imwrite('.\images\idol_192.png', resized_image)