import numpy as np
from pxr import Usd, UsdGeom

# 创建一个01矩阵迷宫（示例）
maze_data = np.array([
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
[1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1],
[1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1],
[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1],
[1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1],
[1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1],
[1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1],
[1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
[1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1],
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]



])

# 定义迷宫单元的尺寸
cell_size = 10
cell_size2= 10
cell_size3= 5
#定义间隔
wall_padding=10

# 创建一个USD场景
stage = Usd.Stage.CreateNew("maze.usda")

# 创建一个Xform（用于组织模型）
maze_xform = UsdGeom.Xform.Define(stage, "/Maze")

# 循环遍历迷宫数据并创建3D模型
for i in range(maze_data.shape[0]):
    for j in range(maze_data.shape[1]):
        if maze_data[i, j] == 1:
            # 如果是墙（0），创建一个立方体模型
            cube = UsdGeom.Cube.Define(stage, "/Maze/Wall_{0}_{1}".format(i, j))
            # 使用XformCommonAPI接口设置变换
            xformAPI = UsdGeom.XformCommonAPI(cube)
            xformAPI.SetTranslate((i * (cell_size+wall_padding), j * (cell_size+wall_padding), 0.5))
            xformAPI.SetScale((cell_size, cell_size2, cell_size3))
        else:
            # 如果是通道（1），创建一个空的Xform
            xform = UsdGeom.Xform.Define(stage, "/Maze/Cell_{0}_{1}".format(i, j))
            # 使用XformCommonAPI接口设置变换
            xformAPI = UsdGeom.XformCommonAPI(xform)
            xformAPI.SetTranslate((i * (cell_size+wall_padding), j * (cell_size+wall_padding), 0.0))

# 保存USD文件
stage.GetRootLayer().Save()