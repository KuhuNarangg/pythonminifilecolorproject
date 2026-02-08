import os
import cv2
ip="images"
if not os.path.exists("bw_images"):
    os.mkdir("bw_images")
# os.mkdir("bw_images") # make directory to store images
for i in os.listdir(ip):
    img=cv2.imread(os.path.join(ip,i))
    gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join("bw_images",i),gry)
