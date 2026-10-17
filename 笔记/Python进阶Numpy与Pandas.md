# 1 NumPy 核心知识

## 简介与安装

**NumPy（Numerical Python）**：Python数值计算基础库，提供高性能多维数组、线性代数、傅里叶变换、随机数工具，底层C实现，运算速度远快于原生Python列表。

安装命令

```python
pip install numpy
```

导入约定

```python
import numpy as np
```

## 核心对象 ndarray

ndarray：N维同类型数组。

核心属性：

| 属性      | 说明                                 |
| --------- | ------------------------------------ |
| .ndim     | 数组维度                             |
| .shape    | 各维度长度，返回元组                 |
| .size     | 元素总个数                           |
| .dtype    | 元素数据类型（int32/float64/bool等） |
| .itemsize | 单个元素字节大小                     |
| .data     | 数组内存缓冲区                       |

特点：数组内**所有元素类型必须一致**；内存连续，向量化运算，避免Python循环。

## 数组创建

```python
# 1. 从python列表创建
arr1 = np.array([1,2,3,4], dtype=np.int64)
arr2 = np.array([[1,2],[3,4]])  # 二维数组

# 2. 初始化特殊数组
np.zeros((2,3))        # 全0数组
np.ones((3,2))         # 全1数组
np.full((2,2), fill_value=9) # 填充指定值
np.eye(3)              # 单位矩阵
np.empty((2,2))        # 空数组（内存残留值，不初始化）

# 3. 序列数组
np.arange(0,10,2)      # [0,2,4,6,8]，左闭右开
np.linspace(0,1,5)     # 0~1均匀生成5个点

# 4. 随机数组
np.random.seed(42)     # 设置随机种子，结果可复现
np.random.rand(2,3)    # [0,1)均匀分布
np.random.randn(3,3)   # 标准正态分布
np.random.randint(0,10, size=(2,2)) # 整数随机
```

## 索引、切片

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 基础索引
arr[0]          # 第0行
arr[0,1]        # 第0行第1列
arr[0][1]       # 等价写法

# 切片 arr[行切片, 列切片]
arr[0:2, 1:]    # 行0~1，列1到末尾
arr[:, 0]       # 所有行，第0列

# 布尔索引
mask = arr > 5
arr[mask]

# 花式索引
arr[[0,2], [1,0]]
```

⚠️ numpy切片返回**视图view**，不是副本，修改会影响原数组；`.copy()`显式复制。

## 数组运算与广播机制

向量化运算：直接数组运算，不需要循环。

```python
def broad_cast():
    a = np.array([1,2,3])
    b = np.array([4,5,6])

    # 逐个元素计算
    print(f'a + b: {a + b}')
    print(f'a * b: {a * b}')
    print(f'a / b: {a / b}')
    print(f'a // b: {a // b}')
    print(f'a - b: {a - b}')
    print(f'a ** 2: {a ** 2}')
    '''
    1. `*`：**元素对元素**，形状必须一模一样；
    2. `@`：
       - 一维向量：**点积求和**，长度相等即可；
       - 二维矩阵：**标准矩阵乘法**，前列 = 后行。
    '''
    # 矩阵乘法
    print(f'a @ b: {a @ b}')
    # shape(2,3)
    c = np.array([[1,2,3],[4,5,6]])
    # shape(2,3)
    d = np.array([[1,2,3],[4,5,6]])
    # 对于2维数组，无法进行矩阵相乘，因为形状不匹配
    # print(f'c @ d: {c @ d}')
    d2 = d.reshape(3,2)
    print(f'd2:\n{d2}')
    # 矩阵相乘, shape(2,3) @ shape(3,2) = shape(2,2)
    print(f'c@d2: {c@d2}')

    # shape(2,3)
    arr1 = np.array([[1,2,3],[4,5,6]], dtype = np.int64)
    # shape(1,3)
    arr2 = np.array([[1,2,3]],dtype = np.int64)
    print(f'arr1+arr2: {arr1+arr2}')
```

**广播（Broadcasting）**

规则：两个数组维度兼容时自动扩展，不用复制数据

- 维度从右往左比较，相等或者其中一个为1，满足广播
- 例：`(3,2)` + `(1,2)` → 可以广播

## 形状操作

```python
def reshape_array():
    arr = np.arange(6)
    print(f'arr: {arr}')
    print(f'arr.shape: {arr.shape}')
    print(f'arr.reshape((2,3)):\n{arr.reshape((2,3))}')
    arr1 = arr.reshape((2,3))
    print(f'arr1: {arr1}')
    arr2 = arr1.flatten()
    print(f'arr2: {arr2}')
    arr3 = arr1.ravel()
    print(f'arr3: {arr3}')

    # 转置
    arr4 = arr1.T
    arr5 = np.transpose(arr4)
    print(f'arr5: {arr5}')
    print(f'arr4: {arr4}')

    # 拼接

    a = np.array([[1,2],[3,4]])
    print(f'a: {a}')
    b = np.array([[5,6]])
    # 按照第0维拼接，相当于按照行拼接
    c = np.concatenate((a,b),axis = 0)
    print(f'c: {c}')
    # 按照第1维度拼接，相当于按照列拼接
    d = np.concatenate((a,b.T), axis = 1)
    print(f'd: {d}')

    # 按照none展平后拼接
    e = np.concatenate((a,b), axis = None)
    print(f'e: {e}')

    # 垂直堆叠
    f = np.vstack((a,b))
    print(f'f: {f}')

    # 水平堆叠
    g = np.hstack((a,b.T))
    print(f'g: {g}')

    # 分割
    h = np.split(arr,3)
    print(f'h: {h}')
```

## 常用数学函数

```python
def math_array():
    arr = np.array([[1, 2], [3, 4]])
    # 按照第0维求和
    arr1 = np.sum(arr, axis = 0)
    print(f'arr1: {arr1}')

    # 按照列求和，第1维求和
    arr2 = np.sum(arr, axis = 1)
    print(f'arr2: {arr2}')

    # 求均值
    # 先按照第0维度求和，也就是垂直相加再求平均值
    arr3 = np.mean(arr, axis = 0)
    print(f'arr3: {arr3}')
    # 按照列求平均值
    arr4 = np.mean(arr, axis = 1)
    print(f'arr4: {arr4}')

    # 求所有元素的平均值
    arr5 = np.mean(arr)
    print(f'arr5: {arr5}')

    print(f'np.std(arr):{np.std(arr)}')  # 标准差
    print(f'np.var(arr):{np.var(arr)}')
    print(f'np.max(arr)/np.min(arr):{np.max(arr)/np.min(arr)}')
    print(f'np.argmax(arr):{np.argmax(arr)}')
    print(f'np.argmin(arr):{np.argmin(arr)}')
    np.var(arr)  # 方差
    np.max(arr) / np.min(arr)
    np.argmax(arr)  # 最大值索引
    np.argmin(arr)
```

## 文件读写

```python
def save_load():
    arr = np.array([[1, 2], [3, 4]])
    # 保存读取二进制npy
    np.save("data.npy", arr)
    arr_load = np.load("data.npy")
    print(f'arr_load: {arr_load}')
    # 文本csv
    np.savetxt("arr.txt", arr, delimiter=",")
    arr_txt = np.loadtxt("arr.txt", delimiter=",")
    print(f'arr_txt: {arr_txt}')
```

## NumPy完整示例

```python
import numpy as np

# 设置随机种子
np.random.seed(2026)
# 创建2行4列正态分布数组
data = np.random.randn(2,4)
print("原始数组：\n", data)
print("shape", data.shape)
print("均值：", np.mean(data))

# 广播运算，所有元素+10
data2 = data + 10
# 布尔筛选，取出大于10的值
filter_data = data2[data2 > 10]
print("大于10的数据：", filter_data)
```

## 进阶实战案例：数据标准化与异常值处理

**案例场景**：数据分析预处理核心操作，对随机生成的多维特征数据，完成标准化、异常值筛选与剔除，适配机器学习数据预处理场景。

**实现思路**：1.生成模拟特征数据；2.均值方差标准化；3.通过3σ原则筛选异常值；4.剔除异常数据并输出统计结果。

```python
import numpy as np

# 1. 固定随机种子，生成100行3列的模拟特征数据（3个特征、100条样本）
np.random.seed(42)
feature_data = np.random.randn(100, 3) * 5 + 10  # 均值10，标准差5
print(f'feature_data:\n {feature_data}')
# 2. 数据标准化（Z-Score标准化，机器学习通用预处理）
mean = np.mean(feature_data, axis=0)  # 按列求均值（每个特征单独标准化）
std = np.std(feature_data, axis=0)    # 按列求标准差
norm_data = (feature_data - mean) / std
print(f'norm_data.shape: {norm_data.shape}')
print(f'norm_data: \n{norm_data}')

print("标准化后数据均值：", np.round(np.mean(norm_data, axis=0), 2))
print("标准化后数据标准差：", np.round(np.std(norm_data, axis=0), 2))

# 3. 3σ原则筛选异常值（绝对值大于3为异常）
outlier_mask = np.abs(norm_data) > 3
print(f'outlier_mask:\n {outlier_mask}')
outlier_count = np.sum(outlier_mask)
print(f"\n检测到异常值数量：{outlier_count}")

# 4. 剔除含异常值的样本
# any按照行或者列统计，只要有一个元素为True，结果就为True
row_outlier_mask = np.any(outlier_mask, axis=1)
'''
row_outlier_mask = 
     [False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False  True False False
 False False False False False False False False False False False False
 False False False  True False False False False False False False False
 False False False False]

统计outlier_mask每一行的每个特征，只要有一个特征为True，结果为True,否则为False
目的就是筛选出每个样本到底是异常样本还是正常样本
row_outlier_mask是一个100个元的一维列表，每个元素代表对应的样本是否异常。
比如row_outlier_mask[0]为True，那么第一个样本就是异常样本，将来要做清洗，将来要删掉样本
'''
print(f'row_outlier_mask.shape:\n {row_outlier_mask.shape}')
print(f'row_outlier_mask:\n {row_outlier_mask}')
# 对bool类型的数组取反，False变为True,True变为False
# 目的，将bool数组改为筛选数组(异常样本对应的bool值为False,正常的样本变为True)
# 将来这个筛选数组作为下标，去筛选样本，只保留正常样本，也就是为True的样本
row_outlier_mask = ~row_outlier_mask
'''
 [ True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True False  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True False  True  True  True  True  True  True  True  True
  True  True  True  True]
'''
print(f'row_outlier_mask:\n {row_outlier_mask}')
# 进行筛选，选出正常的样本，异常样本被过滤掉
clean_data = feature_data[row_outlier_mask]
print(f'clean_data.shape:\n {clean_data.shape}')
print(f"原始样本数：{feature_data.shape[0]}，清洗后样本数：{clean_data.shape[0]}")

# 5. 输出清洗后数据统计信息
print("\n清洗后数据统计：")
print(f"均值：{np.round(np.mean(clean_data, axis=0), 2)}")
print(f"最大值：{np.round(np.max(clean_data, axis=0), 2)}")
print(f"最小值：{np.round(np.min(clean_data, axis=0), 2)}")
```

**解释说明**

![image-20260920132547165](https://cdn.nlark.com/yuque/0/2026/png/27211935/1789881969949-044c9466-f86b-46b4-ba8e-ba015a547785.png)

------

**核心知识点总结**：

1. `axis=0` 按列运算，适配特征数据维度处理；
2. 布尔掩码向量化筛选，替代循环遍历，效率极高；
3. 3σ异常值检测是工业级通用数据清洗规则。

# 2 Pandas 核心技术

## 简介与安装

**Pandas**：基于NumPy构建的结构化数据分析库，专门处理表格型数据（Excel/CSV），提供Series（一维）、DataFrame（二维表）。

安装

```python
pip install pandas
```

导入约定

```python
import pandas as pd
```

## 核心数据结构

### Series 一维带标签数组

索引 + 一组值，底层是numpy数组

```python
s = pd.Series([10,20,30], index=["a","b","c"], name="value")
print(s["a"])
```

### DataFrame 二维表格（最常用）

行索引(index)，列索引(columns)，每一列是Series

```python
df = pd.DataFrame({
    "name":["Alice","Bob"],
    "age":[22,25],
    "score":[88,92]
})
```

DataFrame核心属性

| 属性        | 说明                           |
| ----------- | ------------------------------ |
| .index      | 行索引                         |
| .columns    | 列名                           |
| .values     | 返回底层numpy数组              |
| .shape      | (行数,列数)                    |
| .dtypes     | 每一列数据类型                 |
| .info()     | 数据概览、缺失值、类型         |
| .describe() | 统计描述（均值/标准差/分位数） |

## 数据创建

```python
# 字典创建
df1 = pd.DataFrame({
    "id":[1,2,3],
    "product":["A","B","C"]
})

# numpy数组创建
arr = np.random.rand(3,2)
df2 = pd.DataFrame(arr, columns=["col1","col2"])

# 列表嵌套
df3 = pd.DataFrame([[1,2],[3,4]], columns=["x","y"])
```

## 数据读取与导出

```python
# 读取
pd.read_csv("data.csv", encoding="utf-8", sep=",", header=0)
pd.read_excel("data.xlsx", sheet_name="Sheet1")
pd.read_sql(sql, con=engine) # 数据库读取

# 导出
df.to_csv("out.csv", index=False, encoding="utf-8-sig")
df.to_excel("out.xlsx", index=False)
df.to_parquet("data.parquet") # 高性能列式存储
```

`index=False`：不把pandas行索引写入文件

## 索引与数据筛选

两种索引器：`loc`（标签索引）、`iloc`（位置索引）

```python
# loc 按行标签、列标签
df.loc[0, "name"]
df.loc[df["age"]>23, ["name","age"]]

# iloc 数字位置，从0开始
df.iloc[0:2, 0:2]

# 列选择
df["age"]        # 返回Series
df[["name","age"]] # 返回DataFrame，多列

# 布尔条件
df[ (df["age"]>20) & (df["score"]>80) ]
# 注意：& 和 |，条件括号不能省略，and/or不能用
```

## 数据清洗

```python
# 查看缺失值
df.isna().sum()

# 缺失值处理
df.dropna()                 # 删除含NaN行
df.fillna(0)                # 填充0
df["col"].fillna(df["col"].mean()) # 均值填充

# 去重
df.drop_duplicates(subset=["name"], keep="first")

# 类型转换
df["age"] = df["age"].astype(int)

# 替换值
df["product"].replace("A","Apple")
```

## 分组聚合 groupby

```python
# 分组统计
g = df.groupby("product")
g["score"].agg(["mean","max","count"])

# 自定义聚合
g.agg(avg_score=("score","mean"))
```

## 合并连接 merge / concat

```python
# 表连接（类似SQL join）
pd.merge(left_df, right_df, on="id", how="left")
# how: inner/left/right/outer

# 拼接
pd.concat([df1, df2], axis=0) # 上下堆叠，增加行
pd.concat([df1, df2], axis=1) # 左右拼接，增加列
```

## 时间序列

```python
# 生成时间索引
pd.date_range(start="2026-01-01", periods=10, freq="D")

# 转为datetime类型
df["time"] = pd.to_datetime(df["time"])
df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month
```

## Pandas完整示例

```python
import pandas as pd
import numpy as np

# 构造数据集
data = {
    "name":["张三","李四","王五","赵六"],
    "department":["技术","产品","技术","运营"],
    "salary":[12000,15000,13000,11000],
    "age":[28,32,26,30]
}
df = pd.DataFrame(data)

# 查看基本信息
print(df.info())
print(df.describe())

# 筛选技术部员工
tech_df = df[df["department"]=="技术"]
print("技术部：\n", tech_df)

# 分组求部门平均薪资
dept_salary = df.groupby("department")["salary"].mean()
print("部门平均薪资：\n", dept_salary)
```

## 进阶实战案例：电商订单数据全流程清洗与分析

**案例场景**：模拟真实电商订单数据，完整复现「数据加载-缺失值/重复值清洗-数据转换-分组统计-多维度分析」全流程，贴合企业数据分析实战。

**数据字段**：订单ID、用户ID、下单时间、订单金额、商品品类、支付状态

```python
import pandas as pd
import numpy as np
from datetime import datetime

# 1. 构造模拟电商订单数据（含缺失值、重复数据、异常时间）
np.random.seed(42)
order_data = {
    "order_id": [1001,1002,1003,1004,1001,1005,1006,np.nan],
    "user_id": [2001,2002,2003,2002,2001,2004,2005,2006],
    "order_time": ["2026-08-01","2026-08-01","2026-08-02","2026-08-03",
                   "2026-08-01","2026-08-04",None,"2026-08-05"],
    "order_amount": [99.9,199,49.9,299,99.9,159,89,129],
    "category": ["服饰","数码","家居","数码","服饰","家居","数码","服饰"],
    "pay_status": ["已支付","未支付","已支付","已支付","已支付","未支付","已支付","未支付"]
}
df = pd.DataFrame(order_data)
print("原始数据概览：")
print(df.info())
print("-" * 50)

# 2. 数据清洗
# 2.1 处理缺失值：订单ID、下单时间缺失的订单无效，直接删除
df = df.dropna(subset=["order_id", "order_time"])
# 2.2 去除重复订单（根据订单ID去重，保留首次记录）
df = df.drop_duplicates(subset=["order_id"], keep="first")
# 2.3 数据类型转换：下单时间转为时间格式
df["order_time"] = pd.to_datetime(df["order_time"])

# 3. 新增衍生字段（数据分析常用）
df["order_date"] = df["order_time"].dt.date  # 单独日期列
df["weekday"] = df["order_time"].dt.weekday + 1  # 星期几（1-7）

# 4. 多维度分组聚合分析
# 4.1 各品类订单金额统计
category_analysis = df.groupby("category")["order_amount"].agg(
    订单数量="count",
    总销售额="sum",
    平均订单金额="mean",
    最大订单金额="max"
).round(2)

# 4.2 按支付状态统计
pay_analysis = df.groupby("pay_status")["order_id"].count().rename("订单数量")

# 4.3 每日销售数据
daily_sale = df.groupby("order_date").agg(
    订单量=("order_id", "count"),
    日销售额=("order_amount", "sum")
).round(2)

# 5. 输出分析结果
print("各品类销售统计：\n", category_analysis)
print("-" * 50)
print("支付状态统计：\n", pay_analysis)
print("-" * 50)
print("每日销售数据：\n", daily_sale)

# 6. 筛选高价值订单（金额>100）
high_value_order = df[df["order_amount"] > 100]
print("-" * 50)
print(f"高价值订单（金额>100）数量：{len(high_value_order)}")
```

**实战核心要点**：

1. 针对性清洗：根据业务逻辑删除无效缺失数据，而非统一填充；
2. 衍生字段挖掘：从时间维度拆解业务分析维度；
3. 自定义聚合：一键输出多维度统计指标，适配业务报表需求。

# 3 NumPy + Pandas 联合使用示例

## 基础联合示例

```python
import numpy as np
import pandas as pd

# numpy生成随机数据，传入pandas
np.random.seed(42)
n = 100
arr_data = np.random.randn(n, 3)
df = pd.DataFrame(arr_data, columns=["x1","x2","x3"])

# 使用numpy函数处理pandas列
df["sum_x"] = df["x1"].to_numpy() + df["x2"].to_numpy()
df["is_pos"] = np.where(df["sum_x"]>0, 1, 0)

print(df.head())
```

## 综合实战案例：学生成绩数据分析与等级评定

**案例场景**：结合NumPy高性能数值计算和Pandas表格处理能力，完成学生成绩批量计算、等级划分、数据统计与筛选，是教学、人事考核的通用场景。

**实现流程**：NumPy生成模拟成绩数据 → Pandas构建表格 → 批量计算总分、平均分 → NumPy条件判定成绩等级 → 多维度数据筛选与统计。

```python
import numpy as np
import pandas as pd

# 1. 用NumPy生成50名学生3科成绩（0-100随机整数）
np.random.seed(2026)
score_arr = np.random.randint(50, 100, size=(50, 3))

# 2. 转换为Pandas结构化表格
df_score = pd.DataFrame(score_arr, columns=["语文","数学","英语"])
# 新增学生学号
df_score["学号"] = [f"S{i:03d}" for i in range(1, 51)]

# 3. NumPy批量数值计算（向量化运算，优于Pandas原生循环）
df_score["总分"] = np.sum(score_arr, axis=1)
df_score["平均分"] = np.round(np.mean(score_arr, axis=1), 1)

# 4. NumPy条件判定划分成绩等级
def get_level(avg_score):
    return np.where(avg_score >= 85, "优秀",
                   np.where(avg_score >= 70, "良好",
                   np.where(avg_score >= 60, "及格", "不及格")))

df_score["成绩等级"] = get_level(df_score["平均分"])

# 5. 数据分析统计
# 5.1 各等级人数分布
level_count = df_score["成绩等级"].value_counts()
# 5.2 各科最高分、最低分、平均分
subject_stat = pd.DataFrame({
    "最高分": np.max(score_arr, axis=0),
    "最低分": np.min(score_arr, axis=0),
    "平均分": np.round(np.mean(score_arr, axis=0), 1)
}, index=["语文","数学","英语"])

# 6. 筛选优秀学生、偏科学生（数学<70且总分前20）
excellent_stu = df_score[df_score["成绩等级"] == "优秀"]
unbalanced_stu = df_score[(df_score["数学"] < 70) & (df_score["总分"].rank(ascending=False) <= 20)]

# 输出结果
print("各科成绩统计：\n", subject_stat)
print("-" * 50)
print("成绩等级分布：\n", level_count)
print("-" * 50)
print(f"优秀学生人数：{len(excellent_stu)}")
print(f"高分偏科学生人数：{len(unbalanced_stu)}")
print("\n优秀学生前5名：\n", excellent_stu.head())
```

**联合使用核心优势**：

1. 海量数值计算用**NumPy向量化运算**，速度远超Pandas和Python循环；
2. 数据结构化展示、筛选、统计用**Pandas**，兼顾效率与可读性；
3. `to_numpy()` 实现二者无缝数据流转。