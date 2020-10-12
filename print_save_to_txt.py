import os

path='F:\\AI-sourcecode\\Self-Driving-Car\\Udacity-Self-Driving-Car'
with open(path + '\\lane_img.txt','w') as f:
    
    img_list = os.listdir(path + '\\original_image')
    img_list.sort(key= lambda x:int(x[:-4]))
    
    for i in img_list:
        print(i, file=f)
