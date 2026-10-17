## Redis 简介

**Redis**（Remote Dictionary Server）是一个开源的、基于内存的高性能键值数据库，支持多种数据结构，常用作：

- **缓存层**：加速数据读取
- **消息队列**：发布/订阅模式
- **会话存储**：用户登录状态
- **排行榜/计数器**：实时统计
- **分布式锁**：并发控制

### 为什么 Python + Redis？

- Python 的 `redis-py`库是官方推荐的客户端
- 异步支持（`aioredis`）适合高并发场景
- 与 Django/Flask/FastAPI 等框架无缝集成

## 环境准备

### 安装 Redis 服务器

```bash
# macOS
brew install redis
brew services start redis
# Ubuntu/Debian
sudo apt-get install redis-server
sudo systemctl start redis
# Docker（推荐）
docker run -d --name redis -p 6379:6379 redis:latest
```

### 安装 Python 客户端

```bash
# 基础客户端
pip install redis
# 异步支持（Python 3.7+）
pip install redis[hiredis]   # 带 C 解析器，性能更好
```

### 验证连接

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
print(r.ping())  # 输出: True
```

## 基础连接与配置

### 基础连接方式

```python
import redis
# 方式 1：直接连接
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,                    # 数据库编号（0-15）
    password=None,           # 密码认证
    decode_responses=True    # 自动将 bytes 转为 str
)
# 方式 2：连接池（推荐生产环境使用）
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=50,      # 最大连接数
    decode_responses=True
)
r = redis.Redis(connection_pool=pool)
# 方式 3：从 URL 连接
r = redis.from_url('redis://:password@localhost:6379/0')
```

### 连接参数详解

| 参数                     | 说明               | 默认值      |
| ------------------------ | ------------------ | ----------- |
| `host`                   | 服务器地址         | `localhost` |
| `port`                   | 端口               | `6379`      |
| `db`                     | 数据库索引（0-15） | `0`         |
| `password`               | 认证密码           | `None`      |
| `socket_timeout`         | 连接超时（秒）     | `None`      |
| `socket_connect_timeout` | 建立连接超时       | `None`      |
| `decode_responses`       | 自动解码为字符串   | `False`     |
| `charset`                | 编码格式           | `utf-8`     |

## 数据类型操作

Redis 支持 5 种核心数据类型：String、Hash、List、Set、Sorted Set。

### String（字符串）

最基础类型，可存储字符串、数字、二进制数据。

```python
# 基础操作
r.set('name', 'Alice')           # 设置键值
r.set('name', 'Bob', ex=60)      # 设置并指定 60 秒过期时间
r.set('name', 'Charlie', nx=True) # 仅当 key 不存在时才设置（分布式锁基础）
# 读取
value = r.get('name')            # 获取值
print(value)                     # 'Alice'（如果 decode_responses=True）
# 批量操作
r.mset({'key1': 'val1', 'key2': 'val2'})
result = r.mget(['key1', 'key2'])  # ['val1', 'val2']
# 数字操作
r.set('counter', 0)
r.incr('counter')                # 自增 1，返回 1
r.incrby('counter', 5)           # 自增 5，返回 6
r.decr('counter')                # 自减 1，返回 5
r.incrbyfloat('counter', 1.5)    # 浮点自增，返回 6.5
# 其他
r.set('temp', 'hello')
r.append('temp', ' world')       # 'hello world'
r.strlen('temp')                 # 11
r.getrange('temp', 0, 4)         # 'hello'（子串）
```

### Hash（哈希）

适合存储对象，如用户信息。

```python
# 存储用户对象
r.hset('user:1001', mapping={
    'name': '张三',
    'age': '25',
    'email': 'zhangsan@example.com'
})
# 读取字段
name = r.hget('user:1001', 'name')       # '张三'
all_fields = r.hgetall('user:1001')      # {'name': '张三', 'age': '25', ...}
# 字段操作
r.hincrby('user:1001', 'age', 1)         # 年龄加 1
r.hexists('user:1001', 'phone')          # False
r.hdel('user:1001', 'email')             # 删除字段
r.hlen('user:1001')                      # 字段数量
# 批量读取
keys = r.hkeys('user:1001')              # ['name', 'age']
values = r.hvals('user:1001')            # ['张三', '26']
```

### List（列表）

双向链表，适合消息队列、最新 N 条数据。

```python
r = conn_pool()
r.delete('queue:tasks')
# 从队列左侧插入数据
r.lpush('queue:tasks','task1')
# 从队列右侧插入数据
r.rpush('queue:tasks','task2','task3')
# 查看队列中数据, 获取队列中所有的数据
datas = r.lrange('queue:tasks',0,-1)
print(f'datas:{datas}')
# 获取队列中元素的个数
print(r.llen('queue:tasks'))
r.delete('queue:tasks')
# 演示栈操作
r.lpush('queue:tasks','task1','task2','task3')
print(r.lpop('queue:tasks'))
print(r.lpop('queue:tasks'))
print(r.lpop('queue:tasks'))
print(f'🖤'*50)
print(r.lrange('queue:tasks',0,-1))
print(f'😊'*50)
# 演示队列操作
r.lpush('queue:tasks','task1','task2','task3')
print(r.rpop('queue:tasks'))
print(r.rpop('queue:tasks'))
print(r.rpop('queue:tasks'))

# 从左侧阻塞弹出,如果队列为空，最多阻塞5s
res = r.blpop('queue:tasks',timeout=1)
print(f'res:{res}')
r.lpush('queue:tasks','task2')
# 队列中插入数据/删除数据
r.linsert('queue:tasks','before',
          'task2','new_task')
print(r.lrange('queue:tasks',0,-1))
# 裁剪，保留从0到0的1个元素
r.ltrim('queue:tasks',0,0)
print(r.lrange('queue:tasks',0,-1))
# 删除1个值为new_task的元素
r.lrem('queue:tasks',1,'new_task')
print(r.lrange('queue:tasks',0,-1))
```

### Set（集合）

无序不重复集合，适合标签、共同好友等。

```python
# 添加成员
r.sadd('tags:python', 'web', 'backend', 'ai')
r.sadd('tags:java', 'web', 'backend', 'android')
# 查询
r.smembers('tags:python')                # {'web', 'backend', 'ai'}
r.sismember('tags:python', 'ai')         # True
r.scard('tags:python')                   # 3（成员数量）
r.srandmember('tags:python', 2)          # 随机取 2 个成员
# 集合运算
r.sinter('tags:python', 'tags:java')     # 交集：{'web', 'backend'}
r.sunion('tags:python', 'tags:java')     # 并集
r.sdiff('tags:python', 'tags:java')      # 差集：{'ai'}
# 删除
r.srem('tags:python', 'ai')              # 删除成员
r.spop('tags:python')                    # 随机移除并返回一个成员
```

### Sorted Set（有序集合）

带权重的集合，天然适合排行榜。

```python
# 添加成员（带分数）
r.zadd('leaderboard', {'player1': 100, 'player2': 85, 'player3': 120})
# 查询排名
r.zrange('leaderboard', 0, -1)                    # 按分数升序：['player2', 'player1', 'player3']
r.zrange('leaderboard', 0, -1, withscores=True)   # 带分数：[('player2', 85.0), ...]
r.zrevrange('leaderboard', 0, 2)                  # 降序取前 3 名
# 获取排名（从 0 开始）
r.zrank('leaderboard', 'player1')                 # 升序排名：1
r.zrevrank('leaderboard', 'player1')              # 降序排名：1
# 获取分数
r.zscore('leaderboard', 'player1')                # 100.0
# 修改分数
r.zincrby('leaderboard', 10, 'player1')           # player1 分数 +10
# 范围查询
r.zrangebyscore('leaderboard', 80, 100)           # 分数在 80-100 之间的成员
r.zcount('leaderboard', 80, 100)                  # 分数在 80-100 之间的成员数量
# 删除
r.zrem('leaderboard', 'player3')                  # 删除成员
r.zremrangebyscore('leaderboard', 0, 50)          # 删除分数 0-50 的成员
```

## 高级特性

### 键的过期与持久化

```python
r.set('session:user123', 'data', ex=3600)    # 1 小时后过期
r.set('temp', 'value', px=5000)              # 5 秒后过期（毫秒）
r.expire('name', 60)                         # 给已有 key 设置 60 秒过期
r.ttl('name')                                # 查看剩余存活时间（秒）
r.persist('name')                            # 取消过期（持久化）
# 过期回调（配合 Redis Keyspace Notifications）
```

### 事务（Pipeline）

Redis 事务保证命令批量执行，但**不支持回滚**。

```python
def pipe_op():
    r = conn_pool()
    # 管道
    pipe = r.pipeline()
    pipe.set('key1','value1')
    pipe.set('key2','value2')
    pipe.set('counter',1)
    pipe.incr('counter')
    pipe.set('stock:1001',5)
    results = pipe.execute()
    print(results)

    # 事务操作
    with r.pipeline() as pipe:
        # 乐观锁
        while True:
            try:
                # 1.监视某个key,比如key表示的是一个库存
                pipe.watch('stock:1001')
                # 2. 读取当前库存(watch之后再读)
                current_stock = int(pipe.get('stock:1001') or 0)

                if current_stock > 0:
                    # 3. 开启事务
                    pipe.multi()
                    # 4. 事务内部命令，扣减库存
                    pipe.decr('stock:1001')
                    # 5. 提交事务
                    pipe.execute()
                    print('扣减成功')
                    break
                else:
                    print('库存不足')
                    pipe.unwatch()
                    break

            # 当我们执行管道操作时，其他线程或者进程已经对key修改了，
            # 就会报错
            except redis.WatchError:
                continue
```

### 发布/订阅（Pub/Sub）

```python
import redis
import time
import threading
import uuid

def publisher():
    r = conn_pool()
    for i in range(5):
        r.publish('channel:news',f'消息{i}')
        print(f'发布: 消息{i}')


def subscriber():
    r = conn_pool()
    # 创建订阅者
    pubsub = r.pubsub()
    # 设置订阅者从哪里获取消息,订阅频道
    pubsub.subscribe('channel:news')

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f'收到: {message["data"]}')
            # 如果获取到第5条消息，说明消息获取结束
            if message['data'] == '消息4':
                pubsub.unsubscribe()
                break

def pub_sub_thread():
    threading.Thread(target=publisher).start()
    threading.Thread(target=subscriber).start()
```

### 分布式锁

```python
import redis
import time
import threading
import uuid

def acquire_lock(r,lock_name, acquire_time= 10):
    '''
    获取分布式锁
    :param r: redis对象
    :param lock_name: 锁的名字
    :param acquire_time: 锁持有的时间
    :return: identifier or None
    '''
    # 生成唯一id
    identifier = str(uuid.uuid4())
    # 准备key
    lock_key = f'lock:{lock_name}'

    # 设置NX(不存在才设置) + EX(设置过期时间) 保证原子性
    if r.set(lock_key, identifier, nx=True, ex=acquire_time):
        return identifier
    # 其他线程/进程无法加锁
    return None

def release_lock(r,lock_name, identifier):
    '''
    释放分布式锁,(使用lua脚本保证原子性)
    :param r: redis对象
    :param lock_name: 锁的名字
    :param identifier: 之前加锁的value
    :return:  删除成功返回1，失败返回0
    '''
    lock_key = f'lock:{lock_name}'
    lua_script = f'''
        if redis.call("get", KEYS[1]) == ARGV[1] then 
            return redis.call("del", KEYS[1])
        else
            return 0
        end
    '''
    return r.eval(lua_script, 1, lock_key, identifier)

def use_dis_redis_lock():
    r = conn_pool()
    lock_id = acquire_lock(r,'order:1001')
    if lock_id:
        try:
            print('获取锁成功，执行业务逻辑...')
            time.sleep(2)
        finally:
            release_lock(r,'order:1001',lock_id)
            print('锁已经释放')
    else:
        print('获取锁失败')
```

### 异步操作（aioredis）

```python
import asyncio
import redis.asyncio as aioredis
async def main():
    # 创建redis连接池
    pool  = aioredis.ConnectionPool(
        host='119.91.129.93',
        port=6380,
        db=1,
        max_connections=50,  # 设置连接池的最大连接数
        decode_responses=True,
        password='123456'
    )
    # 创建redis对象
    r = aioredis.Redis(connection_pool=pool)
    print(await r.ping())
    # 设置key和value对
    await r.set('name','zack')
    print(f'name is {await r.get('name')}')
    # 管道操作
    pipe = r.pipeline()
    pipe.set('k1','v1')
    pipe.set('k2','v2')

    results = await pipe.execute()
    print(f'results is {results}')
    await r.aclose()



if __name__ == '__main__':
    asyncio.run(main())
```

## 实战案例

### 案例 1：网站限流器（滑动窗口）

```python
import redis
import time
class RateLimiter:
    def __init__(self, r, key_prefix, limit, window):
        self.r = r
        self.key_prefix = key_prefix
        self.limit = limit      # 最大请求数
        self.window = window    # 时间窗口（秒）
    
    def is_allowed(self, user_id):
        key = f"{self.key_prefix}:{user_id}"
        now = time.time()
        window_start = now - self.window
        
        pipe = self.r.pipeline()
        # 删除窗口外的旧记录
        pipe.zremrangebyscore(key, 0, window_start)
        # 统计当前窗口内的请求数
        pipe.zcard(key)
        # 添加当前请求
        pipe.zadd(key, {str(now): now})
        # 设置 key 过期时间
        pipe.expire(key, self.window)
        
        _, current_count, _, _ = pipe.execute()
        
        return current_count < self.limit
# 使用：每用户每分钟最多 10 次请求
r = redis.Redis(decode_responses=True)
limiter = RateLimiter(r, 'rate:api', limit=10, window=60)
for i in range(12):
    allowed = limiter.is_allowed('user123')
    print(f"请求 {i+1}: {'通过' if allowed else '拒绝'}")
    time.sleep(0.5)
```

### 案例 2：缓存装饰器

```python
import redis
import json
import hashlib
import functools

pool = redis.ConnectionPool(
        host='119.91.129.93',
        port = 6380,
        db = 1,
        max_connections=50,  # 设置连接池的最大连接数
        decode_responses=True,
        password='123456'
    )

# 创建redis对象
r = redis.Redis(connection_pool=pool)
print(r.ping())

def cache(expire=300):
    '''

    :param expire: redis过期时间
    :return: 装饰器外层函数
    '''
    # func将来接受load_from_db
    def decorator(func):
        '''

        :param func: 将来接受load_from_db
        :return: 内层函数
        '''
        @functools.wraps(func)
        def inner(*args, **kwargs):
            cache_key = f"cache:{func.__name__}:{hashlib.md5(str(args).encode()+str(kwargs).encode()).hexdigest()}"
            # 尝试读取缓存
            cached = r.get(cache_key)
            if cached:
                print('缓存命中')
                return json.loads(cached)
            # 执行函数并缓存结果,这里就是从数据库加载数据了
            result = func(*args, **kwargs)
            # 将数据库加载的结果放入redis
            r.set(cache_key, json.dumps(result),ex=expire)
            print(f'写入缓存')
            return result
        return inner
    return decorator


@cache(expire=60)
def load_from_db(user_id):
    # 模拟数据库查询
    print(f'查询数据库: user_id={user_id}')
    return {"id":user_id, "name":f"User_{user_id}","age":25}

# 第一次查数据库
print(load_from_db(1001))
# 第二次缓存命中
print(load_from_db(1001))
```

### 案例 3：实时排行榜

```python
import random
import redis
pool = redis.ConnectionPool(
        host='119.91.129.93',
        port = 6380,
        db = 1,
        max_connections=50,  # 设置连接池的最大连接数
        decode_responses=True,
        password='123456'
    )

# 创建redis对象
r = redis.Redis(connection_pool=pool)
print(r.ping())

class Leaderboard:
    def __init__(self,key):
        # self.key存储集合名字
        self.key = key

    def add_score(self,player,score):
        # 向集合中添加用户和得分
        r.zadd(self.key,{player:score})

    def get_top(self, n = 10):
        # 获取key集合中，前n个用户
        return r.zrevrange(self.key, 0, n-1, withscores=True)

    def get_rank(self, player):
        # 获取player对应的排名，如果排名为空则返回None否则返回rank+1
        # rank是从0开始，所以+1
        rank = r.zrevrank(self.key, player)
        return rank+1 if rank is not None else None

    def get_nearby(self,player,range_count=2):
        rank = r.zrevrank(self.key, player)
        if rank is None:
            return []
        # 获取0或者rank-range_count的最大值，防止负数越界
        # start作为当前玩家能看到的前range_count名用户
        start = max(0,rank-range_count)
        # 当前玩家能看到的后面range_count名用户
        end = range_count + rank
        return r.zrevrange(self.key, start,end, withscores=True)

if __name__ == '__main__':
    # 模拟游戏排行
    lb = Leaderboard('game:score')
    # 添加玩家分数
    players = ['Zack','Ray','Charlies','David','Eve']
    random.seed(5)
    for p in players:
        lb.add_score(p,random.randint(100,1000))

    print(f'🏆 排行榜 Top3: ')
    # enumerate(lb.get_top(3),1)表示每个元素和数字拼接，数字从1开始
    for rank, (player,score) in enumerate(lb.get_top(3),1):
        print(f"{rank}: {player}: {score}分")
    print(f'Zack的排名: 第{lb.get_rank('Zack')}名')
    print(f'Zack附近的玩家:\n')
    for player,score in lb.get_nearby('Zack'):
        print(f' {player}: {int(score)} 分')
```

## 性能优化与最佳实践

### 使用 Pipeline 减少网络往返

```python
# ❌ 低效：100 次网络往返
for i in range(100):
    r.set(f'key:{i}', f'value:{i}')
# ✅ 高效：1 次网络往返
pipe = r.pipeline()
for i in range(100):
    pipe.set(f'key:{i}', f'value:{i}')
pipe.execute()
```

### 批量操作优于循环

```python
# ❌ 低效
for user in users:
    r.hset('users', user['id'], json.dumps(user))
# ✅ 高效
mapping = {u['id']: json.dumps(u) for u in users}
r.hset('users', mapping=mapping)
```

### 合理设置 Key 命名空间

```python
# 推荐格式：业务:模块:标识
user:profile:1001
order:detail:202308250001
cache:api:/api/v1/users
lock:inventory:sku_12345
```

### 4. 避免 Big Key

```python
# ❌ 一个 Hash 存了 100 万个字段
r.hset('all_users', mapping=...)  # 内存和网络压力大
# ✅ 分片存储
for i in range(0, total, 1000):
    batch = users[i:i+1000]
    r.hset(f'users:shard:{i//1000}', mapping=batch)
```

### 连接池配置建议

```python
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=100,        # 根据并发量调整
    socket_keepalive=True,      # TCP 保活
    socket_keepalive_options={}, # 平台相关配置
    health_check_interval=30,   # 健康检查间隔
    decode_responses=True
)
```

### 常见问题排查

| 问题       | 原因                  | 解决方案                            |
| ---------- | --------------------- | ----------------------------------- |
| 连接超时   | 网络延迟或 Redis 阻塞 | 增加超时时间，检查慢查询            |
| 内存暴涨   | 未设置过期时间        | 所有 key 设置 TTL，开启内存淘汰策略 |
| 性能下降   | 大量慢查询            | 使用 `SLOWLOG` 分析，优化数据结构   |
| 数据不一致 | 并发竞争              | 使用事务或分布式锁                  |

## 附录：常用命令速查表

| 操作         | Redis 命令              | Python 方法                    |
| ------------ | ----------------------- | ------------------------------ |
| 设置值       | `SET key value`         | `r.set(key, value)`            |
| 获取值       | `GET key`               | `r.get(key)`                   |
| 删除键       | `DEL key`               | `r.delete(key)`                |
| 检查存在     | `EXISTS key`            | `r.exists(key)`                |
| 设置过期     | `EXPIRE key 60`         | `r.expire(key, 60)`            |
| 哈希设置     | `HSET key field value`  | `r.hset(key, field, value)`    |
| 列表左推     | `LPUSH key value`       | `r.lpush(key, value)`          |
| 集合添加     | `SADD key member`       | `r.sadd(key, member)`          |
| 有序集合添加 | `ZADD key score member` | `r.zadd(key, {member: score})` |

**提示**：Redis 6.0+ 支持多线程 IO，Python 客户端也逐步支持。对于超高并发场景，建议结合异步编程（`aioredis`）和连接池使用。