import os
from shutil import copytree

#设置源路径
src_path = '/home/jinmei/research/DNEMD/029-mut/029_F14A/1_200ns/50frame'

#设置目标路径
dst_path = '/home/jinmei/research/DNEMD/029-mut/029_F14A/1_200ns/PRMSD_5000_4'

#遍历源路径下的所有文件夹
for file in os.listdir(src_path):
# 获取文件夹的绝对路径
    file_path = os.path.join(src_path, file)
# 判断是否为文件夹
    if os.path.isdir(file_path):
# 复制文件夹
        copytree(file_path, os.path.join(dst_path, file))
