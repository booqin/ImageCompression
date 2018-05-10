#
#


import tinify
import json
import os

source_path_tag = "default_source_path"
target_path_tag = "default_target_path"
tinify_key_tag = "default_key"


def png_compress(*path):
    """传入可变参数"""
    # 1.遍历文件夹下所有图片
    s_paths = path[0]
    t_paths = path[1]
    i = 0
    for s_path in s_paths:
        print(s_path)
        # print("s:", i, n)
        # print("n:", t_names[i])
        source = tinify.from_file(s_path)
        source.to_file(t_paths[i])
        i += 1
        print("一共:"+str(len(s_paths))+"; 完成:"+str(i))


def get_dirs(s_dir, t_dir):
    """
    传入的s_dir为原路径，t_dir为目标路径
    """
    source_paths = []
    target_paths = []
    for dirpath, dirname, filename in os.walk(s_dir):
        for _file in filename:
            suffix = os.path.splitext(_file)[1][1:]
            if suffix == "png":
                s_path = os.path.join(dirpath, _file)
                t_path = os.path.join(t_dir, _file)
                source_paths.append(s_path)
                target_paths.append(t_path)
    return source_paths, target_paths


def load_config():
    with open('./config.json', 'r') as config:
        return json.load(config)

if __name__ == '__main__':
    result = load_config()
    print(result['default_key'])
    tinify.key = result[tinify_key_tag]
    png_compress(*get_dirs(result[source_path_tag], result[target_path_tag]))

