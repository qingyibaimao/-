from tensorflow.keras.layers import Input
from PIL import Image

from nets.yolo3 import yolo_body
from yc_yolo import YOLO

yolo = YOLO()

while True:
    img = input('D:/downloads/cungudafa-keras-yolo3-master/keras-yolo3/dataset/phonts/54000.jpg')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image.show()
        
yolo.close_session()
