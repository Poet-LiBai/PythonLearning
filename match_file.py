import os

os.chdir('F:\AIdocument\GitHubSourceCode\Mobilenet-SSD-Essay\logs')
os.getcwd()

list_file = os.listdir()

reg_list = []
h5_list = []
normalconv_list = []
groupconv_list = []
for i in list_file:
    if i.endswith('.h5'):
        h5_list.append(i)

for j in h5_list:
    if not j.endswith('groupconv2d.h5'):
        normalconv_list.append(j)

    if j.endswith('groupconv2d.h5'):
        groupconv_list.append(j)        

print(h5_list)
print(normalconv_list)
print(groupconv_list)
        
