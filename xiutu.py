# import os
# import re
# import sys
# path = r"D:\downloads\cungudafa-keras-yolo3-master\keras-yolo3\VOCdevkit\VOC2007\pngimage"
# fileList = os.listdir(path)  # 待修改文件夹
# print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
# os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
# num = 396  # 名称变量
# for fileName in fileList:  # 遍历文件夹中所有文件
#     pat = ".+\.(jpg|jpeg|JPG)"  # 匹配文件名正则表达式
#     pattern = re.findall(pat, fileName)  # 进行匹配
#     print('pattern[0]:', pattern)
#     print('num：', num, 'filename:', fileName)
#     os.rename(fileName, ('fen' + str(num) + '.jpg' ))  # 文件重新命名
#     num = num + 1  # 改变编号，继续下一项
# print("---------------------------------------------------")
# sys.stdin.flush()  # 刷新
# print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件

#修改图片尺寸大小
import os
from PIL import Image

filename = os.listdir("D:\\downloads\\cungudafa-keras-yolo3-master\\keras-yolo3\\VOCdevkit\\VOC2007\\pngimage")
base_dir = "D:\\downloads\\cungudafa-keras-yolo3-master\\keras-yolo3\\VOCdevkit\\VOC2007\\pngimage\\"
new_dir = "D:\\downloads\\cungudafa-keras-yolo3-master\\keras-yolo3\\VOCdevkit\\VOC2007\\JPEGImages\\"
size_m = 416
size_n = 416

for img in filename:
    image = Image.open(base_dir + img)
    image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
    image_size.save(new_dir + img)