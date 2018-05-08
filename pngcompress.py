#
#


import tinify
import os

source_path = "C:\\Users\\zhangfeng\\Desktop\\语音"
target_path = 'C:\\Users\\zhangfeng\\Desktop\\new'
tinify.key = "JiATnFuBlJKsxVEQqje21N9M2wZtZLMT"

def pngCompress(*path):
    """传入可变参数"""
    #1.遍历文件夹下所有图片
    s_paths = path[0]
    t_paths = path[1]
    i = 0
    for s_path in s_paths:
        print(s_path)
        # print("s:", i, n)
        # print("n:", t_names[i])
        source = tinify.from_file(s_path)
        source.to_file(t_paths[i])
        i+=1
        print("一个:"+str(len(s_path))+"; 完成:"+str(i))

def getDirs(s_dir, t_dir):
    """
    传入的s_dir为原路径，t_dir为目标路径
    """
    source_paths = []
    target_paths = []
    for dirpath, dirname, filename in os.walk(s_dir):
        for _file in filename:
            suffix = os.path.splitext(_file)[1][1:]
            if(suffix=="png"):
                s_path = os.path.join(dirpath, _file)
                t_path = os.path.join(t_dir, _file)
                source_paths.append(s_path)
                target_paths.append(t_path)
    return (source_paths, target_paths)

if __name__ == '__main__':
    pngCompress(*getDirs(source_path, target_path))

