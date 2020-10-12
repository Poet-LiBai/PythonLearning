import os

path = r"F:\BaiduNetdiskDownload\CCTSDB (CSUST Chinese Traffic Sign Detection Benchmark)\Images\00000~00999"
files = os.listdir(path)

file_delet_list = []
count = 0
for file_name in files:

    if file_name.endswith('(1).png'):

        file_name = os.path.join(path,file_name)
        file_delet_list.append(file_name)
        count += 1
        
    else:
        continue

print(count)

for file_delet in file_delet_list:

    if os.path.exists(file_delet):
        os.remove(file_delet)
    else:
        print('No such file:%s',file_delet)
