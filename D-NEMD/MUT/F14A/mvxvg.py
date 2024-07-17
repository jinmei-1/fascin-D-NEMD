import os
from shutil import copyfile
path = '/home/jinmei/research/DNEMD/029-mut/029_F14A/1_200ns/PRMSD_5000_1/' #文件的根目录,需要把目录改为双斜杠
files=os.listdir(path) #统计所有文件或文件夹名称
count=0 #用于计数
file_type='.xvg'  #指定需要更改的文件类型,可以根据需要改为其他的后缀名
number=len(files) #文件夹和文件的总数
for f in files:
    if os.path.isfile(os.path.join(path,f))==False:#判断是否为文件夹
        for n in os.listdir(os.path.join(path,f)):
            if os.path.splitext(n)[1] == str(file_type):#判断指定类型文件
                newname=f+file_type  #新的文件名称，即文件夹的名称
                os.rename(os.path.join(path,f,n),os.path.join(path,f,newname)) #改名
                copyfile(os.path.join(path,f,newname),os.path.join(path,newname)) #将文件从文件夹下复制到根目录
                count+=1

print(number)
print(count)
