## 前言

Python操作MySQL最主流两个库：

- `mysql‑connector‑python`：MySQL官方驱动，纯Python编写，无需C依赖
- `pymysql`：第三方库，社区使用最广，语法几乎和官方库一致

本文示例优先使用 **pymysql**

**重要区分**

- pymysql：Python3 使用
- MySQLdb：只支持Python2，Python3废弃，不要再用

ORM框架（进阶）：`SQLAlchemy`，面向对象操作数据库，不需要手写原生SQL，教程后面会简单提及。

## . 环境准备与驱动安装

### 前提条件

1. 本地或远程已经安装好 MySQL 服务
2. 知道 MySQL 的：主机地址、端口、用户名、密码、数据库名

### 安装 pymysql

```bash
pip install pymysql
```

安装官方驱动备选：

```bash
pip install mysql-connector-python
```

下文全部以 `pymysql` 演示。

## 数据库基础概念回顾

- **数据库****(\**\*\*database\*\**\*)**：一个独立仓库，如 test_db
- **数据表****(\**\*\*table\*\**\*)**：库下面存储数据的表，如 user
- **字段/列****(\**\*\*column\*\**\*)**：表的属性，id,name,age
- **记录/行****(\**\*\*row\*\**\*)**：一条数据
- **游标****(\**\*\*Cursor\*\**\*)**：Python执行SQL、读取结果的对象，相当于查询的手柄

![null](https://cdn.llfc.club/image-20260818115512762.png)

## 连接 MySQL 数据库

### 先创建数据库

在DataGrip中创建数据库

```sql
create database if not exists py_adv_db charset='utf8mb4';
use py_adv_db;
select database();
```

### 最简单连接示例

```python
import pymysql

# 1. 创建数据库连接对象
conn = pymysql.connect(
    host='127.0.0.1',      # 数据库地址，远程填IP
    port=3306,              # mysql默认端口
    user='root',            # 用户名
    password='123456',      # 密码
    database='test_db',     # 要连接的数据库名称
    charset='utf8mb4'       # 字符集！！utf8mb4支持emoji，不要写utf‑8
)

# 2. 创建游标对象
cursor = conn.cursor()

# 3.关闭资源，用完一定要关闭
cursor.close()
conn.close()
```

**注意：**`charset='utf8mb4'`，**不是 utf‑8**，MySQL里没有横杠。

## 核心对象详解：Connection、Cursor

### Connection 连接对象

```
conn = pymysql.connect(...)
```

主要方法：

| 方法              | 作用                     |
| ----------------- | ------------------------ |
| `conn.cursor()`   | 创建游标                 |
| `conn.commit()`   | 提交事务，保存增删改结果 |
| `conn.rollback()` | 回滚事务，撤销修改       |
| `conn.close()`    | 关闭数据库连接           |

**MySQL默认开启事务！执行INSERT/UPDATE/DELETE之后必须commit()才会真正写入数据库，否则数据不会生效！**

### Cursor 游标对象

```
cursor = conn.cursor()
```

常用方法：

| 方法                                 | 作用             |
| ------------------------------------ | ---------------- |
| `cursor.execute(sql, args)`          | 执行单条SQL语句  |
| `cursor.executemany(sql, args_list)` | 批量执行多条SQL  |
| `cursor.fetchone()`                  | 获取一条查询结果 |
| `cursor.fetchmany(n)`                | 获取n条结果      |
| `cursor.fetchall()`                  | 获取全部查询结果 |
| `cursor.close()`                     | 关闭游标         |

#### 返回字典格式结果（非常实用）

默认返回元组，可以设置游标类型返回字典：

```python
cursor = conn.cursor(pymysql.cursors.DictCursor)
# 查询结果就会变成 [{"id":1,"name":"张三"},...]
```

## 增删改操作（INSERT / DELETE / UPDATE）

增删改属于写操作，执行完后 **必须 conn****.\**\*\*commit\*\**\*(\**\**)**

### 创建数据表

```sql
create table user(
  id int primary key auto_increment,
  name varchar(50),
  age smallint,
  email varchar(50)
);
```

### 插入单条数据

```python
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='test_db',
    charset='utf8mb4'
)
cursor = conn.cursor()

sql = """
INSERT INTO user(name, age, email)
VALUES (%s, %s, %s)
"""

# 参数列表
data = ("张三", 22, "zhangsan@qq.com")

cursor.execute(sql, data)

# 提交事务，写入数据库
conn.commit()

print(f"受影响行数：{cursor.rowcount}")

cursor.close()
conn.close()
```

### 更新数据

```python
sql = "UPDATE user SET age=%s WHERE id=%s"
cursor.execute(sql,(25, 1))
conn.commit()
```

### 删除数据

```python
sql = "DELETE FROM user WHERE id=%s"
cursor.execute(sql,(1,))
conn.commit()
```

`cursor.rowcount`：返回本次SQL影响了多少行记录。

## 查询操作（SELECT）

查询**不需要 commit**

### fetchone() 获取单条

```python
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='test_db',
    charset='utf8mb4'
)
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM user WHERE id = %s"
cursor.execute(sql,(1,))

row = cursor.fetchone()
print(row)  #字典格式 {'id':1,'name':'张三','age':22}

cursor.close()
conn.close()
```

### fetchall() 获取全部结果

```python
sql = "SELECT * FROM user"
cursor.execute(sql)
rows = cursor.fetchall()
for r in rows:
    print(r["name"], r["age"])
```

**大数据量表禁止使用fetchall**，一次性加载全部数据到内存，容易内存溢出，建议循环逐行读取。

### fetchmany(n) 获取指定条数

```python
rows = cursor.fetchmany(5)
```

游标读取结果是单向指针，读完一遍就到头了，不能重复fetch。

## 参数化查询 & SQL注入风险（重中之重）

### 危险写法！字符串拼接！绝对禁止！

```python
# 千万不要这样！！！
name = input("请输入用户名:")
sql = f"SELECT * FROM user WHERE name = '{name}'"
cursor.execute(sql)
```

SQL注入示例：用户输入 `' or 1=1 -- ` 就会查询出所有账号！

### 安全写法：参数化查询

pymysql使用 `%s` 作为占位符，**不是Python字符串格式化**！

```python
sql = "SELECT * FROM user WHERE name = %s"
cursor.execute(sql, (name,))
```

驱动内部自动转义特殊字符，彻底防注入。

**注意：**占位符不管什么类型，统一用 `%s`，不要写 `%d`。

## 事务管理（Commit / Rollback）

事务四大特性ACID：原子性、一致性、隔离性、持久性

**原子性**：一组SQL要么全部成功，要么全部失败回滚。

示例：转账，A扣钱、B加钱，中途出错就撤销

```python
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='test_db',
    charset='utf8mb4'
)
cursor = conn.cursor()

try:
    sql1 = "UPDATE account SET money=money-100 WHERE id=1"
    sql2 = "UPDATE account SET money=money+100 WHERE id=2"
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()   #全部成功提交
    print("转账成功")
except Exception as e:
    conn.rollback() #出错回滚，撤销所有操作
    print("转账失败，已回滚", e)
finally:
    cursor.close()
    conn.close()
```

## 异常处理

常见异常类：`pymysql.Error`、`pymysql.err.OperationalError`

```python
import pymysql
from pymysql.err import OperationalError

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='wrong_password',
        database='test_db',
        charset='utf8mb4'
    )
except OperationalError as e:
    print("数据库连接失败！",e)
```

## 上下文管理器 with 用法（自动关闭资源）

`with` 自动释放游标和连接，不用手动 close()，推荐生产环境使用。

```python
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='test_db',
    charset='utf8mb4'
)

with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)

# with结束游标自动关闭
conn.close()
```

**注意：**with不能自动commit！增删改依旧需要手动 `conn.commit()`

## 批量操作 executemany

一次性插入多条数据，性能远高于循环执行execute

```python
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='test_db',charset='utf8mb4')
cursor = conn.cursor()

sql = "INSERT INTO user(name,age) VALUES (%s,%s)"
data_list = [
    ("李四", 20),
    ("王五", 24),
    ("赵六", 29)
]

cursor.executemany(sql, data_list)
conn.commit()
print("批量插入行数", cursor.rowcount)

cursor.close()
conn.close()
```

## 获取自增主键ID

插入一条数据之后，获取刚生成的id：

```python
cursor.execute(sql,data)
conn.commit()
new_id = cursor.lastrowid
print("新增记录主键id=", new_id)
```

## 常用配置、编码、时区问题

### 14.1 字符集问题

- `utf8` 在MySQL最多存3字节，不能存emoji表情
- `utf8mb4` 完整utf‑8，推荐永远用这个

### 14.2 时区问题

数据库时间和本地不一致，连接时指定时区：

```python
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8mb4",
    init_command="SET time_zone = '+8:00'" #东八区
)
```

## 实战案例：简易用户管理系统

```python
import pymysql
from pymysql.cursors import DictCursor

class UserDB:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            database='test_db',
            charset='utf8mb4'
        )

    def add_user(self,name,age,email):
        sql = "INSERT INTO user(name,age,email) VALUES (%s,%s,%s)"
        with self.conn.cursor(DictCursor) as cur:
            cur.execute(sql,(name,age,email))
            self.conn.commit()
            return cur.lastrowid

    def get_user(self,uid):
        sql = "SELECT * FROM user WHERE id=%s"
        with self.conn.cursor(DictCursor) as cur:
            cur.execute(sql,(uid,))
            return cur.fetchone()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = UserDB()
    newid = db.add_user("小明", 18, "xm@qq.com")
    print("新增id", newid)
    print(db.get_user(newid))
    db.close()
```

## 最佳实践与避坑指南

### 推荐做法

1. 永远使用参数化查询，禁止字符串拼接SQL
2. 增删改后一定要 commit()
3. 使用 try‑except 捕获数据库异常，出错回滚rollback
4. 查询大量数据不要fetchall，分批读取
5. 用完连接、游标必须关闭，避免连接泄漏
6. 密码不要硬编码写代码里！配置文件/环境变量读取
7. 生产环境使用**连接池**，不要频繁创建销毁连接

### 常见坑

1. 忘记commit，修改的数据看不到
2. charset='utf‑8' 报错，正确是utf8mb4
3. 单条参数元组少逗号 `cursor.execute(sql,(1))` → 报错！应该 `(1,)`
4. 游标fetch之后指针到头，不能二次读取结果

### 进阶方向：连接池 & ORM

1. DBUtils：数据库连接池，解决频繁打开关闭连接开销大问题
2. SQLAlchemy ORM：面向对象操作数据库，减少手写SQL，大型项目首选

```bash
pip install sqlalchemy
```