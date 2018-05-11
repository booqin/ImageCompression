# -*- coding:utf-8 -*-
# Create by BoQin on 2018/5/11

import tinify
import json
import os
import sys

source_path_tag = "default_source_path"
target_path_tag = "default_target_path"
tinify_key_tag = "default_key"

DEFAULT_OUT = "out_png"


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
        print("一共:" + str(len(s_paths)) + "; 完成:" + str(i))


def get_all_paths(s_dir, t_dir):
    """
    传入的s_dir为原路径，t_dir为目标路径
    """
    # 不存在文件夹，创建文件夹
    if not os.path.exists(t_dir):
        os.makedirs(t_dir)

    return get_paths(s_dir, t_dir)


def get_paths(root_source_dir, root_target_dir):
    """
    递归生成所有目标路径
    :param root_source_dir:
    :param root_target_dir:
    :return:
    """
    source_paths = []
    target_paths = []

    for filename in os.listdir(root_source_dir):

        if os.path.isdir(os.path.join(root_source_dir, filename)):
            # 路径
            _source_dir = os.path.join(root_source_dir, filename)
            _target_dir = os.path.join(root_target_dir, filename)
            # 创建空文件夹
            make_empty_dir(_target_dir)
            # 递归文件夹下的文件
            (s_paths, t_paths) = get_paths(_source_dir, _target_dir)
            source_paths.extend(s_paths)
            target_paths.extend(t_paths)

        else:
            # 文件的情况判断是否为可压缩图片
            suffix = os.path.splitext(filename)[1][1:]
            if suffix == "png" or suffix == "jpg":
                s_path = os.path.join(root_source_dir, filename)
                t_path = os.path.join(root_target_dir, filename)
                source_paths.append(s_path)
                target_paths.append(t_path)

    return source_paths, target_paths


def make_empty_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def load_config():
    with open('./config.json', 'r') as config:
        return json.load(config)


def get_parm():
    """
    获取参数
    :return:
    """
    _result = load_config()
    source_path = sys.argv[1] if len(sys.argv) > 1 else _result[source_path_tag]
    target_path = sys.argv[2] if len(sys.argv) > 2 else _result[target_path_tag]
    if not target_path:
        target_path = os.path.join(os.getcwd(), DEFAULT_OUT)
    tinify_key = _result[tinify_key_tag]

    return tinify_key, source_path, target_path


if __name__ == '__main__':
    result = get_parm()
    tinify.key = result[0]
    png_compress(*get_all_paths(result[1], result[2]))
