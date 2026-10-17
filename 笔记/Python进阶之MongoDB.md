## MongoDB 核心基础概念

MongoDB 是一款开源、高性能的**文档型 NoSQL 数据库**，数据以 BSON（二进制 JSON）格式存储，完全适配 Python 字典数据结构，无固定表结构，支持动态字段扩展，灵活度远高于传统关系型数据库。

### 核心术语对应关系

| MongoDB 术语       | SQL 对应术语        | 说明                             |
| ------------------ | ------------------- | -------------------------------- |
| Database（数据库） | Database（数据库）  | 数据顶层容器，隔离不同业务数据   |
| Collection（集合） | Table（数据表）     | 存储一组文档，无字段约束         |
| Document（文档）   | Row（数据行）       | 最小数据单元，Python 字典格式    |
| Field（字段）      | Column（字段/列）   | 文档中的键值对                   |
| _id                | Primary Key（主键） | 文档唯一标识，自动生成，不可重复 |

### MongoDB 核心特性

- **无结构化约束**：同一集合下的文档可拥有不同字段，适配多变业务场景
- **天然适配 Python**：文档与字典双向兼容，无需复杂数据转换
- **高读写性能**：适配海量非结构化、半结构化数据存储
- **功能完善**：支持查询、聚合、索引、事务、副本集、分片集群
- **场景适配广**：爬虫数据、用户行为日志、内容资讯、中小型业务数据存储

**核心特性**：MongoDB 无需手动创建数据库和集合，首次插入数据会自动完成初始化。

## 环境部署与依赖安装

### Python 依赖安装

使用官方驱动库 `pymongo`，推荐国内源加速安装：

```bash
# 官方源安装
pip install pymongo

# 清华源加速（推荐）
pip install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### MongoDB 服务部署方式

#### 方式1：Docker 快速部署（推荐开发环境）

```bash
# 启动 MongoDB 容器，映射默认端口27017
docker run -d -p 27199:27017 --name pyai_mongo --restart always docker.xuanyuan.run/library/mongo:latest
```

#### 方式2：本地安装

下载 MongoDB 社区版，默认端口 **27199**，启动本地服务即可使用。

#### 方式3：云端数据库

使用 MongoDB Atlas 云端免费数据库，无需本地部署。

## Python 连接 MongoDB

### 无认证本地连接（开发常用）

```python
from pymongo import MongoClient

# 连接本地默认端口 MongoDB
client = MongoClient("mongodb://localhost:27199/")

# 查询所有数据库名称
db_list = client.list_database_names()
print("当前所有数据库：", db_list)

# 关闭连接（pymongo 自带连接池，无需频繁关闭）
# client.close()
```

### 账号密码认证连接（生产环境）

```python
from pymongo import MongoClient

# 带认证连接，authSource 指定认证数据库
client = MongoClient("mongodb://username:password@localhost:27099/?authSource=admin")
```

### 连接池核心注意事项

MongoClient 默认内置连接池，**全局仅实例化一次**，禁止在循环、接口请求中重复创建客户端，否则会造成连接溢出、性能卡顿。

## 数据库与集合基础操作

```python
from pymongo import MongoClient

# 初始化客户端、数据库、集合
client = MongoClient("mongodb://localhost:27099/")
db = client["test_db"]  # 选择/创建数据库
coll = db["users"]      # 选择/创建集合

# 查询当前数据库下所有集合
coll_names = db.list_collection_names()
print("当前集合列表：", coll_names)
```

说明：赋值数据库、集合仅为声明操作，不会真实创建，只有插入数据后才会生成实体库和集合。

## 核心 CRUD 增删改查操作

### 新增数据（Create）

#### 插入单条文档

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27099/")
db = client["test_db"]
coll = db["users"]

# 文档数据（Python 字典格式）
user = {
    "name": "张三",
    "age": 25,
    "gender": "male",
    "hobby": ["篮球", "读书"],
    "address": {"city": "西安", "district": "雁塔区"}
}

# 插入单条数据
res = coll.insert_one(user)
print("新增文档ID：", res.inserted_id)
```

#### 批量插入多条文档

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27099/")
db = client["test_db"]
coll = db["users"]

user_list = [
    {"name": "李四", "age": 22, "gender": "female"},
    {"name": "王五", "age": 30, "gender": "male"},
    {"name": "赵六", "age": 28, "gender": "male"}
]

# 批量插入
res = coll.insert_many(user_list)
print("批量新增ID列表：", res.inserted_ids)
```

### 查询数据（Read）

#### 查询单条数据 find_one()

```python
# 查询匹配条件的第一条数据
data = coll.find_one({"name": "张三"})
print("单条查询结果：", data)
```

#### 查询多条数据 find()

```python
# 查询所有数据
all_data = coll.find()
for item in all_data:
    print(item)

# 条件查询：年龄大于25岁的用户
filter_data = coll.find({"age": {"$gt": 25}})
for item in filter_data:
    print(item)
```

注意：find() 返回游标对象（Cursor），仅可遍历一次，遍历结束后游标清空，无法二次读取。

#### 字段投影（指定返回字段）

```python
# 只返回 name、age 字段，隐藏默认 _id
data = coll.find({}, {"name": 1, "age": 1, "_id": 0})
for item in data:
    print(item)
```

#### 分页、排序查询

```python
# sort：1升序，-1降序；skip：跳过条数；limit：限制条数
# 年龄倒序，分页查询（第一页，每页10条）
page_data = coll.find().sort("age", -1).skip(0).limit(10)
for item in page_data:
    print(item)
```

### 更新数据（Update）

核心操作符 **$set**：仅更新指定字段，保留文档原有字段，避免整文档覆盖。

#### 更新单条数据

```python
# 将张三的年龄更新为26
res = coll.update_one(
    {"name": "张三"},
    {"$set": {"age": 26}}
)
print("更新成功条数：", res.modified_count)
```

#### 批量更新数据

```python
# 将所有25岁以下用户年龄统一加1
res = coll.update_many(
    {"age": {"$lt": 25}},
    {"$inc": {"age": 1}}  # $inc 数值自增操作符
)
print("批量更新成功条数：", res.modified_count)
```

高危注意：不使用 $set 直接传字典，会**覆盖整条文档**，丢失所有原有字段！

### 删除数据（Delete）

#### 删除单条数据

```python
res = coll.delete_one({"name": "李四"})
print("删除条数：", res.deleted_count)
```

#### 批量删除数据

```python
# 删除30岁以上所有用户
res = coll.delete_many({"age": {"$gt": 30}})
print("批量删除条数：", res.deleted_count)
```

## 高级查询运算符

MongoDB 内置丰富查询运算符，适配复杂条件筛选，Python 中直接通过字典嵌套使用。

### 常用查询运算符汇总

| 运算符 | 含义           | 对应 SQL |
| ------ | -------------- | -------- |
| $gt    | 大于           | >        |
| $gte   | 大于等于       | >=       |
| $lt    | 小于           | <        |
| $lte   | 小于等于       | <=       |
| $ne    | 不等于         | !=       |
| $in    | 包含在数组内   | IN()     |
| $nin   | 不包含在数组内 | NOT IN() |
| $or    | 或条件         | OR       |
| $and   | 且条件         | AND      |

### 高级查询示例

```python
# 1. $in 查询：年龄在22、25、28岁的用户
data1 = coll.find({"age": {"$in": [22, 25, 28]}})

# 2. $or 查询：年龄大于28 或 性别为女的用户
data2 = coll.find({
    "$or": [
        {"age": {"$gt": 28}},
        {"gender": "female"}
    ]
})

# 3. 数组字段查询：爱好包含篮球的用户
data3 = coll.find({"hobby": "篮球"})

for item in data3:
    print(item)
```

## 聚合管道 Aggregation（核心重点）

聚合管道是 MongoDB 数据分析核心，可实现 SQL 中 GROUP BY、统计、筛选、字段重构等复杂操作，数据按管道阶段依次处理，效率远高于 Python 内存统计。

### 常用管道阶段

- **$match**：筛选文档（等价 WHERE）
- **$group**：分组聚合（等价 GROUP BY）
- **$project**：重构、筛选字段（等价 SELECT）
- **$sort**：结果排序
- **$limit**：限制返回条数

### 聚合实战示例

业务需求：筛选18岁以上用户，按性别分组，统计各组人数、平均年龄，并按人数倒序排序

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27099/")
db = client["test_db"]
coll = db["users"]

# 定义聚合管道
pipeline = [
    # 第一步：筛选18岁以上用户
    {"$match": {"age": {"$gte": 18}}},
    # 第二步：按性别分组聚合
    {
        "$group": {
            "_id": "$gender",       # 分组字段
            "user_count": {"$sum": 1},  # 统计人数
            "avg_age": {"$avg": "$age"} # 计算平均年龄
        }
    },
    # 第三步：按人数倒序排序
    {"$sort": {"user_count": -1}}
]

# 执行聚合查询
result = coll.aggregate(pipeline)
for item in result:
    print("聚合结果：", item)
```

## 索引优化

索引可避免数据库全表扫描，大幅提升查询效率，是生产环境必备优化手段，但会轻微降低写入性能，需合理创建。

### 单字段索引

```python
# 为name字段创建升序索引
index_res = coll.create_index("name", 1)
print("创建索引名称：", index_res)
```

### 复合索引（多字段联合索引）

```python
# 年龄、城市联合索引
coll.create_index([("age", 1), ("address.city", 1)])
```

### 唯一索引（防重复数据）

```python
# 邮箱唯一索引，保证邮箱不重复
coll.create_index("email", 1, unique=True)
```

### 索引管理

```python
# 查看所有索引
print("索引信息：", coll.index_information())

# 删除指定索引
coll.drop_index("name_1")

# 删除所有索引
coll.drop_indexes()
```

## 事务操作

**重要限制**MongoDB 单机版不支持事务，仅**副本集/分片集群**支持事务，用于保证多操作原子性（要么全部成功，要么全部回滚）。

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27099/")
db = client["test_db"]
coll = db["users"]

# 开启会话与事务
with client.start_session() as session:
    with session.start_transaction():
        # 事务内多个操作，原子执行
        coll.insert_one({"name": "小明", "age": 20}, session=session)
        coll.update_one({"name": "张三"}, {"$set": {"age": 99}}, session=session)
        # 任意报错，所有操作自动回滚
```

## 工程化封装：通用操作类

封装通用 MongoDB 操作类，适配项目开发，可直接复用，解决原生代码冗余、ID 转换、分页重复代码问题。

```python
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional, List, Dict, Any

class MongoDBDao:
    """MongoDB 通用操作封装类"""
    def __init__(self, uri: str = "mongodb://localhost:27099/", db_name: str = "test_db"):
        # 全局单例客户端
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, coll_name: str):
        """获取集合对象"""
        return self.db[coll_name]

    def add_one(self, coll_name: str, data: Dict[str, Any]) -> ObjectId:
        """新增单条数据"""
        coll = self.get_collection(coll_name)
        res = coll.insert_one(data)
        return res.inserted_id

    def get_by_id(self, coll_name: str, doc_id: str) -> Optional[Dict[str, Any]]:
        """根据ID查询数据（自动转换ObjectId）"""
        try:
            coll = self.get_collection(coll_name)
            return coll.find_one({"_id": ObjectId(doc_id)})
        except Exception:
            return None

    def list_data(self, coll_name: str, filter_dict: Dict = None, page: int = 1, page_size: int = 10) -> List[Dict[str, Any]]:
        """分页查询数据"""
        filter_dict = filter_dict or {}
        skip_num = (page - 1) * page_size
        coll = self.get_collection(coll_name)
        return list(coll.find(filter_dict).skip(skip_num).limit(page_size))

    def update_by_id(self, coll_name: str, doc_id: str, update_data: Dict) -> int:
        """根据ID更新数据"""
        coll = self.get_collection(coll_name)
        res = coll.update_one({"_id": ObjectId(doc_id)}, {"$set": update_data})
        return res.modified_count

    def delete_by_id(self, coll_name: str, doc_id: str) -> int:
        """根据ID删除数据"""
        coll = self.get_collection(coll_name)
        res = coll.delete_one({"_id": ObjectId(doc_id)})
        return res.deleted_count

# 测试使用
if __name__ == "__main__":
    mongo_dao = MongoDBDao()
    # 新增数据
    new_id = mongo_dao.add_one("users", {"name": "测试用户", "age": 24})
    print("新增数据ID：", new_id)
    # 查询数据
    print("查询结果：", mongo_dao.get_by_id("users", str(new_id)))
```

## 高频踩坑总结

- 禁止循环内重复创建 MongoClient，会导致连接池溢出、服务卡顿
- 更新数据必须使用 $set，否则会覆盖整条文档，丢失原有字段
- 字符串格式的 _id 无法直接查询，必须转为 ObjectId 对象
- find() 游标仅可遍历一次，二次遍历无数据
- 单机 MongoDB 不支持事务，事务功能必须部署副本集
- 索引不宜过多，索引仅优化查询，会降低写入、更新性能

## 生产环境最佳实践

- 全局单例初始化 MongoClient，复用连接池，提升性能
- 数据库账号密码通过环境变量配置，禁止代码硬编码
- 大数据量查询使用分批游标读取，避免一次性加载全部数据占满内存
- 高频查询字段建立索引，定期排查慢查询日志
- 复杂统计优先使用聚合管道，避免 Python 内存循环统计
- 海量数据分页避免大 skip 偏移，优先使用 _id 游标分页
- 生产环境开启账号认证，禁止外网无密码暴露数据库

## 常用工具方法速查

```python
# 1. 统计匹配数据条数
count = coll.count_documents({"age": {"$gt": 18}})

# 2. 删除集合
coll.drop()

# 3. 删除数据库
client.drop_database("test_db")

# 4. 判断数据库/集合是否存在
db_name_list = client.list_database_names()
coll_name_list = db.list_collection_names()
```