import os

filePath2 = r'D:/downloads/cungudafa-keras-yolo3-master/keras-yolo3/dataset/phonts'
filePath1 = r'D:/downloads/cungudafa-keras-yolo3-master/keras-yolo3/dataset/Annotations'

list1 = os.listdir(filePath1)
file_list1 = [] #annotations中的文件名列表 不带后缀
for i in list1:
    file_list1.append(os.path.splitext(i)[0])
# print(file_list1)

list2 = os.listdir(filePath2)
file_list2 = [] #image中的文件名列表 不带后缀
for i in list2:
    file_list2.append(os.path.splitext(i)[0])
# print(file_list2)
#找出没有标注的图片名称列表
b = [y for y in file_list2 if y not in file_list1]
#把这些列表加上扩展名 然后将其删除
path = r'D:/downloads/cungudafa-keras-yolo3-master/keras-yolo3/dataset/phonts'
for i in b:
    os.remove(os.path.join(path, i+'.jpg'))