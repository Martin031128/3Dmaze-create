# 3Dmaze-create
建立一个3D的迷宫，并导出为usd文件
主要使用了一个叫pxr的库，这个库不建在windows下面使用（因为环境很难搞）。在linux下面安装时建议安装在虚拟环境中，这样安装比较方便。如果在安装pxr库时出现了什么问题，改成在虚拟环境中安装基本能解决。
本代码生成迷宫是利用01矩阵的，我在里面提前写好了一个01矩阵，如果想随机生成立体迷宫的话，先从随机生成01矩阵入手再导进去就好了。
其实我写了随机生成01矩阵的代码，但是没有整理进去（
在omniverse常用usd的模型，生成的迷宫可以在omniverse里面使用。
