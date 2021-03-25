import os
import random

trainval_percent = 0.1
train_percent = 0.9
VOC_path = 'D:/downloads/cungudafa-keras-yolo3-master/keras-yolo3/VOCdevkit/VOC2007/'
xmlfilepath = os.path.join(VOC_path, 'Annotations')
txtsavepath = os.path.join(VOC_path, 'ImageSets/Main')
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(VOC_path+'ImageSets/Main/trainval.txt', 'w')
ftest = open(VOC_path+'ImageSets/Main/test.txt', 'w')
ftrain = open(VOC_path+'ImageSets/Main/train.txt', 'w')
fval = open(VOC_path+'ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()