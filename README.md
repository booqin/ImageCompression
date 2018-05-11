## PNGCompress
该工具通过TinyPNG提供的接口，实现批量图片压缩，可用于app端的资源图片的二次压缩，__使用前请到[tinypng官网](https://tinypng.com/)注册获取key__。

## 依赖

需要python3+环境，mac系统可用。

工具类依赖了tinify包

```
pip install --upgrade tinify
```

## 用法

压缩需要以下三个参数

- tinify_key：[tinypng官方](https://tinypng.com/)提供的key，注册后即可获得，每月有500张免费压缩量。
- source_path：源路径
- target_path：目标路径

其中tinify_key和source_path为必填，target_path空的情况下回默认输出在脚本的同级目录下。

参数可以通过以下两种方式进行配置

### 1.修改目录下的config.json
在目录下通过config.json，提供配置参数将作为默认值，其中defualt_key需要__添加自己的key__，default_source_path为源路径，default_target_path为目标路径，可不填。

```json
{
  "default_key":"tiny_key",
  "default_source_path":"your source path",
  "default_target_path":"your target path"
}
```

然后直接运行即可：

```python

python3 pngcompress.py

```

### 2.在运行时配置路径
执行该脚本时输入源路径和目标路径

```python

python3 pngcompress.py /Users/vito/Desktop/test /Users/vito/Desktop/out_png

```

建议使用方法1。

## TODO

- windows的适配
- python2的适配
- 压缩速度和提示优化




