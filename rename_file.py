import os, re
from PIL import Image

i=0
path='./nobubble'
newn="/pic"
for filename in os.listdir(path):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    i+=1
    #if file[-2: ] == 'py':
     #   continue   #过滤掉改名的.py文件
    filename=path+"/"+filename
    if i<10:
        new_name = path+newn+"00"+str(i)+".png"
        os.rename(filename, new_name)
    elif i<100:
        new_name = path+newn + "0" + str(i) + ".png"
        os.rename(filename, new_name)
    else:
        new_name = path+newn + str(i) + ".png"
        os.rename(filename, new_name)

