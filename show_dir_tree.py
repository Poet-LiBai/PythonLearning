import os

def fileCntIn(currPath):
    '''汇总当前目录下文件数'''
    return sum([len(files) for root, dirs, files in os.walk(currPath)])

def dirsTree(startPath):
    '''树形打印出目录结构'''
    print(list(os.walk(startPath))[0])
    for root, dirs, files in os.walk(startPath):
        #获取当前目录下文件数
        fileCount = fileCntIn(root)
        #获取当前目录相对输入目录的层级关系,整数类型
        #os.sep是获取目录分隔符 \ ，所以计算 \ 的个数就可以获取层级数
        level = root.replace(startPath, '').count(os.sep)
        #树形结构显示关键语句
        #根据目录的层级关系，重复显示'| '间隔符，
        #第一层 '| '
        #第二层 '| | '
        #第三层 '| | | '
        #依此类推...
        #在每一层结束时，合并输出 '|____'
        indent = '|    ' * 1 * level + '|——'
        print ('%s%s' % (indent, os.path.split(root)[1]))        
        for file_name in files:
            indent = '|    ' * 1 * (level + 1) + '|——'
            print ('%s%s' % (indent, file_name))


if __name__ == '__main__':
    path = u"F:\\AI-sourcecode\\Computer Vision\\Object Detection\\up_yolov3\\yolo3"
    dirsTree(path)
