import datashape
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#设置图像显示字体为黑体字
plt.rcParams['font.sans-serif']=['SimHei']
#设置负号可以正常显示
plt.rcParams['axes.unicode_minus']=False

#初步验证是否正确导入数据
try:
    # 导入波士顿房价数据集(已放在同一文件夹中)
    boston= r'boston.csv'
    df = pd.read_csv(boston)
    # 打印数据行数和列数
    df.info()
    #将行数和列数分别赋值，判断导入的数据集是否为空
    rows, columns = df.shape
    if rows > 0 and columns > 0:
        print("数据成功导入")
    else:
        print("数据导入失败，请重新导入")

#如果出现找不到地址的报错时
except FileNotFoundError:
    print("文件 {boston} 未找到，请检查文件路径是否正确。")
#如果出现文件格式错误的抱错时
except pd.errors.ParserError:
    print("文件解析错误，请检查文件是否为有效的CSV格式。")

boston= r'boston.csv'
df = pd.read_csv(boston)
#调整图表大小
df.plot(figsize=(15, 6))
#调整最大显示宽度
pd.set_option('display.width', 500)
#调整最大显示列
pd.set_option('display.max_columns', 15)
# 设定列名
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PIRATIO', 'B', 'LSTAT', 'MEDV']
print("部分浏览：")
print(df.head())

# 数据预处理
# 数据类型检查，方便后面的处理
print("数据类型检查：")
print(df.dtypes)

# 判断缺失值
print("缺失值检查：")
print(df.isnull().sum())

#删除有缺失值的行（数据较多的情况）
print("删除缺失值：")
a=df.isnull()
for i in a:
    if i==1:
        df.drop(i,inplace=True)
print('删除结束')
print(df.isnull().sum())


# 基于 Z-score 方法进行异常值处理
print("处理异常值：")
def z_score_outlier_detection(data, threshold=3):
    z_scores = np.abs((data - data.mean()) / data.std())
    return z_scores > threshold
for i in df.columns:
    if i==1:
        df.drop(i,inplace=True)
print("处理完毕")

#数据基本统计分析
print("基本统计信息：")
print(df.describe())

#可视化分析
#1. 绘制房价的直方图，了解房价分布
plt.figure(figsize=(15, 6))
#设置图片清晰度
plt.rcParams['figure.dpi']=300
plt.hist(df['MEDV'], bins=30, edgecolor='k',color='b')
plt.title('波士顿房价分布', fontsize=40)
plt.xlabel('房价', fontsize=20)
plt.ylabel('频数', fontsize=20)
plt.show()

# 查看房价的描述性统计信息
print("房间数量的描述性统计信息：")
print(df['MEDV'].describe())

# 2. 绘制房价与房间数量的散点图，查看两者关系
plt.figure(figsize=(15, 6))
plt.scatter(df['RM'], df['MEDV'])
plt.title('房间数量与房价关系', fontsize=40)
plt.xlabel('房间数量', fontsize=20)
plt.ylabel('房价', fontsize=20)
plt.show()


