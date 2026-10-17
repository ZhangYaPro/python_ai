# 从一个网址说起：认识 Web 与 FastAPI

在写第一行代码之前，我们先弄清楚几个最基本的问题：网页是什么？在浏览器里输入一个网址后发生了什么？我们这门课要写的程序在其中扮演什么角色？FastAPI 又是个什么东西？把这些想明白，后面的概念都会顺理成章。

### 1.1 你每天都在使用 Web

用浏览器看新闻、查资料、购物、用网页版邮箱，乃至很多手机 App 里点开的页面——它们都有一个共同点：

- 你在一个**客户端**（绝大多数时候是浏览器）上操作；
- 背后有一台（实际是很多台）远方的**服务器**在为你服务。

你在浏览器里看到的文字、图片、按钮、视频，不是凭空出现的，而是**服务器通过网络"送"过来的**。我们这门课要学的，就是怎么用 Python 写出"送出这些内容"的服务器程序。

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791071304247-0d004d9e-712d-4d66-94cd-637cf5c72875.png)

### 1.2 在浏览器输入一个网址，发生了什么

假设你在地址栏输入 `http://www.example.com/books` 然后回车，想看看有哪些书。整个过程可以拆成四步：

1. 浏览器把"我想要 `/books` 这个资源"打包成一个**请求（Request）**，通过网络发给服务器；
2. 服务器收到请求，看了看路径是 `/books`，于是去准备数据（可能要查询数据库）；
3. 服务器把准备好的内容打包成一个**响应（Response）**，发回给浏览器；
4. 浏览器收到响应，把内容渲染成你看到的页面。

这个"请求—响应"的来回，全世界的浏览器和服务器都遵循同一套对话规矩，这套规矩叫 **HTTP**（超文本传输协议）。你可以把它理解成浏览器和服务器之间的"共同语言"：浏览器用 HTTP 提问，服务器用 HTTP 回答。

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791093264867-1884736d-2924-4828-af32-9eb0440d7df1.png)

请记住这种对话的两个特点：**一问一答、答完即结束**。浏览器不主动发问，服务器就不会主动说话

### 1.3 前端与后端：一个管"长相"，一个管"脑子"

一次网页访问里，其实有两种不同的工作：

- **前端**：服务器把内容送过来之后，浏览器负责把文字、颜色、排版、按钮、动画呈现出来，并响应你的点击、输入。这部分由 HTML、CSS、JavaScript 完成，运行在你的浏览器里。
- **后端**：运行在服务器上，负责"处理逻辑、存取数据"——判断你有没有登录、查询你要的图书、计算价格、把数据存进数据库。

用餐厅打个比方：

| 餐厅里的角色       | 对应 Web 里的角色 | 干什么                               |
| ------------------ | ----------------- | ------------------------------------ |
| 菜单、装修、服务员 | 前端              | 你看得到、摸得着，负责接待和呈现     |
| 后厨               | 后端              | 你看不到，负责真正"做菜"（处理逻辑） |
| 冰柜、仓库里的食材 | 数据库            | 存放原材料（数据），后厨按需取用     |

你点菜（浏览器发请求）→ 后厨从仓库取食材、把菜做好（后端处理逻辑、读写数据库）→ 服务员把菜端上桌（响应返回、前端显示）。

**我们这门课要写的是"后厨"，也就是后端**：让 Python 程序充当服务器，接收浏览器的请求、处理逻辑、返回响应。

### 1.4 后端要做哪些事？为什么需要"框架"

现在问题来了：如果不借助任何工具，要用 Python 从零写一个能回应浏览器的后端，你得自己完成这五件事：

1. 监听一个网络端口，等待客户端连接；
2. 从到来的**原始字节流**里，按 HTTP 规矩解析出：请求方法（GET / POST）、路径（`/books`）、参数、请求头、请求体；
3. 根据路径，决定"应该执行哪个函数"；
4. 执行业务逻辑、查询数据库；
5. 把结果重新按 HTTP 规矩拼成字节流，发回去。

你会发现，第 1、2、3、5 件事对几乎所有网站都一样——不管你做的是图书网站、订单系统还是博客，它们与你的具体业务毫无关系，却非常繁琐、极易出错。

**Web 框架（Web Framework）就是把这些重复劳动提前做好的工具**。有了框架之后：

- 你只需声明"哪个路径对应哪个函数"（这叫**路由**）；
- 框架帮你监听端口、解析请求，并把请求包装成一个好用的对象；
- 你在函数里把数据 `return` 出去，框架帮你拼成合法的响应。

于是你可以把精力集中在第 4 件事——真正的业务逻辑上。打个比方：框架就像已经帮你把灶台、锅具、水电、排烟系统都装好的厨房，你这个"厨师"只管专心做菜，不必每次都从砌灶台开始。

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791093516864-ea6297ca-ba47-4817-bbae-9fa1a6ec7fd7.png)

### 1.5 FastAPI 是什么

**FastAPI 是一个现代的、高性能的 Python Web 框架**，同样用来编写网站和接口（后端）。它的名字来自 **Fast（快速）+ API（接口）**，尤其擅长编写"接口服务"。它有几个非常亮眼的特点：

- **基于类型注解**：你用 Python 自带的类型提示（type hints）声明参数和数据结构，框架据此**自动完成数据校验**——类型不对、超出范围的请求会被直接挡下，并清楚告诉你哪里错了；
- **自动生成接口文档**：代码写完，立刻得到一个**可以在网页上直接点击调试**的接口说明页面（`/docs`），不需要手写一行文档；
- **原生支持"异步"**：能高效处理大量并发请求，也原生支持 WebSocket 实时连接；
- **性能出色**：在官方基准测试中，它的性能接近 Node.js、Go 这类以高并发见长的技术。

**为什么会出现 FastAPI 这样的框架？** 传统的 Web 框架大多以"同步"方式工作：来一个请求，就派一个执行单元从头服务到尾。可 Web 请求的大部分时间其实都花在"等待"上——等数据库返回、等另一个网络接口回应。在等待的时候，这个执行单元被占着却什么也做不了，想提高并发就只能不断加开执行单元（线程），开销不小。FastAPI 用"异步"方式工作，让执行单元在等待时转而去处理别的请求，从而用更少的资源扛住更多并发；与此同时，它还把"数据校验"和"接口文档"这两件本来要手写的苦差事一并自动化了。

**FastAPI 特别适合**：

- **AI / 大模型应用的后端**——LangChain、Dify 等主流 AI 生态都以 FastAPI 为默认框架；
- 高并发、大量 IO 等待的服务；
- 需要清晰接口文档、多人协作的项目；
- 需要实时推送（WebSocket）的服务。

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791113582318-ecefd231-c02f-4d23-83a6-589f7dfd477c.png)

### 1.6 先建立一个直觉：什么是"异步"

FastAPI 最核心、也最容易让人犯怵的词就是"异步"。这里我们先用一个生活例子建立直觉，**不求甚解，有个印象即可**，第 7、8 章会带你把它彻底搞懂并亲手实测。

想象一个厨师在厨房做菜：

- **同步的做法**：厨师炖上一锅汤，这锅汤要小火煮 30 分钟。在这 30 分钟里，厨师就站在锅前干等，什么也不做；其他人点的菜也只能排队等着。
- **异步的做法**：厨师把汤炖上之后，**利用这 30 分钟的"等待时间"转身去切菜、炒菜、准备别的菜**；等汤煮好了，再回过来处理这锅汤。

同样是一个厨师（一个执行单元），异步的做法在"等待"时不闲着，于是能同时照看很多锅、服务很多人。

回到 Web 开发：一个请求大部分时间都在"等"（等数据库、等外部接口）。所谓异步，就是让程序**在等待的时候让出自己，去服务其他请求**，等数据回来了再继续。这件事能极大地提升并发能力。

# 环境准备与最小 Demo

安装依赖：

```bash
pip install fastapi uvicorn
```

- **fastapi：框架本体**
- **uvicorn：ASGI 服务器，用来运行 FastAPI（类似 flask 的 werkzeug）**

main.py 最简示例：

```python
from fastapi import FastAPI

# 创建应用实例
app = FastAPI(title="FastAPI教学Demo", version="1.0")

# 定义GET接口，路径 /
@app.get("/")
async def root():
    return {"msg": "Hello FastAPI"}
```

启动服务：

```bash
uvicorn main:app --reload
```

| 参数     | 说明                                               |
| -------- | -------------------------------------------------- |
| main     | 文件名 main.py                                     |
| app      | 文件里 app = FastAPI() 的实例变量名                |
| --reload | 开发模式，代码修改自动重启；**生产环境一定要关掉** |

访问地址：

- 接口：[http://127.0.0.1:8000](http://127.0.0.1:8000/)
- Swagger 交互式文档：http://127.0.0.1:8000/docs
- ReDoc 静态文档：http://127.0.0.1:8000/redoc

如果启动失败，可以尝试使用如下命令

```bash
python -m pip install --user --upgrade "typing-extensions>=4.14.1"
python -m uvicorn 102_fast_api_main:app --reload
```

> 讲解点：打开 docs 页面，可以直接在网页上调试接口，不需要 postman。

**async 与普通函数：**

```python
# 异步写法，适合IO任务（数据库、http请求）
@app.get("/async")
async def demo_async():
    return {"data": "async"}

# 普通同步函数也支持，CPU密集任务可以用
@app.get("/sync")
def demo_sync():
    return {"data": "sync"}
```

FastAPI 会自动处理，不用纠结一开始全部改成 async。

# 路径参数与查询参数

## 路径参数（URL 路径里的变量）

```python
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    # 类型标注int，FastAPI自动校验，如果传入字符串会直接报错
    return {"user_id": user_id}
```

访问：http://127.0.0.1:8000/user/1001。校验：访问 /user/abc 直接返回 422 参数校验错误。

## 查询参数（?key=value）

```python
@app.get("/user/list")
async def get_user_list(page: int = 1, size: int = 10):
    # page默认值1，size默认10
    return {"page": page, "size": size}
```

1. 浏览器直接访问（最简单）

**① 不传参数，使用默认值 page=1, size=10**

```bash
http://127.0.0.1:8000/user/list
```

返回：`{"page":1,"size":10}`

**② 传 page=2，size=20**

```bash
http://127.0.0.1:8000/user/list?page=2&size=20
```

返回：`{"page":2,"size":20}`

可选参数写法：

```python
from typing import Optional
@app.get("/search")
async def search(keyword: Optional[str] = None):
    return {"keyword": keyword}
```

请求

```python
http://127.0.0.1:8000/search?keyword=zack
```

# Pydantic 数据模型（请求体 POST）

**重点**：GET 没有请求体，POST/PUT 用请求体传复杂 JSON，**Pydantic 是 FastAPI 最核心的能力**。

```python
from pydantic import BaseModel, Field

# 定义请求体模型
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20, description="用户名")
    password: str = Field(min_length=6)
    age: int | None = Field(default=None, ge=0, le=120) # 可选，0~120

@app.post("/user/create")
async def create_user(user: UserCreate):
    # FastAPI自动把前端json解析成UserCreate对象，并自动校验
    return {"msg": "创建成功", "data": user.model_dump()}
```

测试：在 /docs 打开 try it out，传入 json。如果用户名长度不足，自动返回 422 错误，带详细错误信息。

> 强调：不用手动写 if 判断长度，Pydantic 自动完成，极大减少重复校验代码。

## FastAPI 自带文档调试（最推荐，开发首选）

启动服务后访问：

```bash
http://127.0.0.1:8000/docs
```

找到 `POST /user/create` → 点 **Try it out** 在请求体编辑框填入 JSON 示例：

```bash
{
  "username": "zhangsan",
  "password": "123456",
  "age": 25
}
```

点 Execute 直接发送请求，看返回结果。

age 是可选字段，可以省略不写：

```bash
{
  "username": "lisi",
  "password": "654321"
}
```

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791337578739-2ae3a208-24c1-487a-b62a-d561c8b63160.png)

**响应模型**：过滤返回字段，比如不返回密码：

```python
class UserOut(BaseModel):
    username: str
    age: int | None

@app.post("/user/create", response_model=UserOut)
async def create_user(user: UserCreate):
    return user
```

response_model 会自动过滤，不会把 password 返回前端，安全。

# 状态码与自定义响应

```python
from fastapi import status
from fastapi.responses import JSONResponse

@app.get("/item/{item_id}", status_code=status.HTTP_201_CREATED)
async def get_item(item_id: int):
    if item_id <= 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "id不能小于等于0"}
        )
    return {"item_id": item_id}
```

| 常量                         | 含义       |
| ---------------------------- | ---------- |
| status.HTTP_200_OK           | 成功       |
| status.HTTP_201_CREATED      | 创建成功   |
| status.HTTP_400_BAD_REQUEST  | 参数错误   |
| status.HTTP_401_UNAUTHORIZED | 未登录     |
| status.HTTP_403_FORBIDDEN    | 权限不足   |
| status.HTTP_404_NOT_FOUND    | 资源不存在 |

# 依赖注入（FastAPI 灵魂）

依赖注入：把公共逻辑抽成函数，接口直接引用，解耦鉴权、数据库会话、日志。

**示例：简单鉴权依赖**

```python
from fastapi import Depends, Header, HTTPException

# 定义依赖函数
async def get_token(authorization: str | None = Header(default=None)):
    if not authorization or authorization != "Bearer test_token":
        raise HTTPException(status_code=401, detail="token无效")
    return authorization

# 接口使用依赖 Depends
@app.get("/user/info")
async def user_info(token: str = Depends(get_token)):
    return {"msg": "访问成功", "token": token}
```

讲解重点：

1. 多个接口共用鉴权逻辑，不用每个接口复制代码；
2. 依赖可以嵌套，依赖里面还可以 Depends 别的依赖；
3. 适合：token 校验、获取 db 会话、日志记录、参数预处理。

函数**只有一个入参**：`authorization`

- `Header(default=None)` 作用：声明这个参数的数据源是 HTTP Header，`default=None` 代表缺省值为 None。
- 千万不要理解成：`authorization` 和 `Header` 是两个参数。

启动命令

```bash
python -m uvicorn 103_fastapi_depends:app --reload --port 10086
```

# HTTP 原始报文示例

重点：`Authorization` 放在**请求头（Request Header）**，不是请求体，也不是 url 参数

## 完整 HTTP 请求报文（GET /user/info）

```http
GET /user/info HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: curl/7.68.0
Accept: */*
Authorization: Bearer test_token
```

解释：

1. 第一行：请求方法、路径、HTTP 版本
2. 从第 2 行开始，**每一行都是请求头**
3. `Authorization: Bearer test_token` 就是我们代码里读取的头部字段
4. 头部结束后空一行，GET 请求没有请求体

对应代码：`authorization: str | None = Header(default=None)` FastAPI 读到这一行的值就是字符串：`"Bearer test_token"`

------

## 如果不带 Authorization header

```http
GET /user/info HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: curl/7.68.0
Accept: */*
```

此时代码里 `authorization` 变量 = `None`，直接抛出 401。

## 如果 token 写错

```http
GET /user/info HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: curl/7.68.0
Accept: */*
Authorization: Bearer abc123
```

读到的值是 `"Bearer abc123"`，不等于 `Bearer test_token`，同样 401。

## 配套：服务端返回成功的 HTTP 响应报文

```http
HTTP/1.1 200 OK
date: Tue, 14 Oct 2026 xxx
server: uvicorn
content-length: 60
content-type: application/json

{"msg":"访问成功","token":"Bearer test_token"}
```

# 路由拆分（大型项目目录结构）

单文件适合 demo，真实项目必须拆分路由。推荐目录结构：

```latex
my_fastapi/
├── main.py              # 入口文件
├── routers/
│   ├── __init__.py
│   ├── user.py          # 用户相关接口
│   └── item.py          # 商品相关接口
├── schemas/             # pydantic模型
│   └── user.py
├── dependencies.py      # 公共依赖
└── database.py          # 数据库连接
```

routers/user.py：

```python
from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["用户模块"])

@router.get("/list")
async def user_list():
    return {"data": ["user1","user2"]}
```

main.py：

```python
from fastapi import FastAPI
from routers.user import router as user_router

app = FastAPI()
app.include_router(user_router)
```

- prefix="/user"：这个路由下所有接口自动拼接前缀
- tags=["用户模块"]：在 docs 文档里分组展示接口

# 全局异常处理

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# 自定义全局HTTP异常处理器
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "msg": exc.detail, "data": None}
    )

# 捕获非预期的服务器异常
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "msg": "服务器内部错误", "data": None}
    )

@app.get("/error")
async def test_error():
    raise HTTPException(status_code=400, detail="业务异常")
```

# CORS 跨域与中间件

前端 Vue/React 访问后端会跨域，FastAPI 自带 CORS 中间件。

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境不要写*，填写前端域名 ["https://xxx.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**同源 vs 跨域**

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791952040708-384b8c9a-f9e1-455f-836e-4273be6a986e.png)

**常见跨域场景**

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791952139247-8dd66797-aa54-4ab7-8d2b-3ffe2dff84d4.png)

**跨域处理方案**

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791952443783-08d22362-23cc-4df3-b198-b8eb4b0ddbd4.png)

**另一种处理方案**

![img](https://cdn.nlark.com/yuque/0/2026/jpeg/27211935/1791953422094-02239110-450c-4b67-bb56-d6de3fb4d768.jpeg)

**中间件示例**

自定义中间件（记录请求耗时）：

```python
import time
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
import time
from fastapi import FastAPI, Request

# 1. 创建 FastAPI 应用
app = FastAPI(title="中间件耗时统计演示")

# 2. 注册全局 HTTP 中间件：自动计算每个接口的处理耗时
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 请求进来第一步：记录开始时间戳
    start_time = time.time()

    # 放行请求，交给后面的接口处理，等待返回响应
    response = await call_next(request)

    # 响应回来：计算整个请求的总耗时
    process_time = time.time() - start_time

    # 把耗时写入响应头（X-开头是行业约定的自定义响应头）
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    return response


# ---------------- 下面是业务接口 ----------------

# 接口1：快速查询图书列表（无额外延迟）
@app.get("/books", summary="查询图书列表")
async def get_book_list():
    return {
        "code": 200,
        "data": ["Python编程", "FastAPI入门", "机器人学导论"]
    }

# 接口2：模拟慢查询（故意加延迟，模拟查数据库/控制机械臂的耗时操作）
@app.get("/books/{book_id}", summary="查询单本图书（模拟慢接口）")
async def get_book_detail(book_id: int):
    # 模拟数据库查询/硬件操作耗时：0.5秒
    time.sleep(0.5)
    return {
        "code": 200,
        "data": {
            "id": book_id,
            "title": "SO-ARM101机械臂开发指南",
            "price": 59.9
        }
    }
```

# 后台任务

适合：接口快速返回，后台异步执行任务（日志、发送邮件、推送消息）。

> ⚠ 注意：后台任务不是分布式任务队列！服务重启任务会丢失；长时间任务要用 Celery/RQ。

```python
from fastapi import BackgroundTasks

def write_log(msg: str):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

@app.post("/send")
async def send_msg(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "收到消息")
    return {"msg": "任务已提交"}
```

# 生命周期事件（启动/关闭钩子）

```python
@app.on_event("startup")
async def startup():
    print("服务启动，初始化数据库连接、加载大模型权重")

@app.on_event("shutdown")
async def shutdown():
    print("服务关闭，释放资源、关闭数据库")
```

新版 FastAPI 推荐用 lifespan 替代 on_event，更现代写法：

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup：服务启动前执行
    print("lifespan start")
    yield
    # shutdown：服务关闭时执行
    print("lifespan end")

app = FastAPI(lifespan=lifespan)
```

案例

```python
from fastapi import FastAPI

app = FastAPI(title="生命周期演示-on_event版")

# 模拟全局资源：数据库连接、缓存数据
db_conn = None
book_cache = {}

# ========== 启动钩子：服务启动前自动执行 ==========
@app.on_event("startup")
async def startup():
    global db_conn, book_cache
    print("[startup] 服务启动中...")
    # 模拟：初始化数据库连接
    db_conn = "已连接"
    print(f"  → 数据库连接：{db_conn}")
    
    # 模拟：预热缓存、加载图书数据
    book_cache = {1: "Python编程", 2: "FastAPI入门", 3: "机械臂控制"}
    print(f"  → 图书缓存加载完成，共 {len(book_cache)} 本")
    print("[startup] 启动完成 ✅\n")

# ========== 关闭钩子：服务关闭前自动执行 ==========
@app.on_event("shutdown")
async def shutdown():
    global db_conn
    print("\n[shutdown] 服务关闭中...")
    # 模拟：关闭数据库连接、释放资源
    db_conn = "已断开"
    print(f"  → 数据库连接：{db_conn}")
    print("[shutdown] 资源释放完成 ✅")

# 测试接口
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"code": 200, "data": book_cache.get(book_id), "db_status": db_conn}
```

![img](https://cdn.nlark.com/yuque/0/2026/png/27211935/1791954762262-a9819528-1a0b-43bb-96f7-b8b516580b28.png)

# 数据库集成简易示例（SQLAlchemy + async）

## 一、前置准备

### 1. 安装依赖包

```bash
pip install "sqlalchemy[asyncio]" aiomysql fastapi uvicorn pydantic
```

- `aiomysql`：Python 异步 MySQL 驱动，SQLAlchemy 异步操作 MySQL 的核心依赖
- `pydantic`：FastAPI 原生支持的请求 / 响应数据校验框架

### 2. 先在远程 MySQL 创建业务库

用 Navicat 或命令行登录远程 MySQL，执行一次建库语句（必须提前创建，否则连接报错）：

```bash
CREATE DATABASE IF NOT EXISTS test_db 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

------

#### 二、完整可运行代码（`main.py`）

```python
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from contextlib import asynccontextmanager

# SQLAlchemy 异步相关导入
from sqlalchemy.ext.asyncio import (
create_async_engine,
async_sessionmaker,
AsyncSession
)
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func, select

# ------------------------------
# 1. 远程 MySQL 数据库配置
# ------------------------------
# 格式：mysql+aiomysql://用户名:密码@主机:端口/数据库名?字符集
DATABASE_URL = "mysql+aiomysql://root:123456@119.91.129.93:3381/test_db?charset=utf8mb4"

# 创建异步引擎
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # 开发环境开启：打印SQL日志；生产环境关闭
    pool_pre_ping=True, # 自动检测断开的连接，避免长连接失效
    pool_size=5,        # 连接池核心大小
    max_overflow=10     # 连接池最大溢出数
)

# 异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,  # 提交后不失效对象，避免重复查询
    class_=AsyncSession
)

# ORM 模型基类
Base = declarative_base()

# ------------------------------
# 2. ORM 数据模型（用户表）
# ------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

# ------------------------------
# 3. Pydantic 响应模型（接口格式规范）
# ------------------------------
class UserResp(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True  # 支持 ORM 对象直接转 Pydantic

# ------------------------------
# 4. 应用生命周期：启动自动建表
# ------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时：创建所有数据表
    async with engine.begin() as conn:
        # 同步建表方法放到异步线程执行
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 关闭时：释放数据库连接池
    await engine.dispose()

app = FastAPI(title="异步MySQL集成示例", lifespan=lifespan)

# ------------------------------
# 5. 数据库会话依赖（每个请求一个独立会话）
# ------------------------------
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ------------------------------
# 6. 全异步 CRUD 数据库操作
# ------------------------------
async def create_user(db: AsyncSession, username: str, email: str) -> User:
    """创建用户"""
    user = User(username=username, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)  # 刷新获取数据库生成的ID和时间
    return user

async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    """根据ID查用户"""
    return await db.get(User, user_id)

async def get_user_by_name(db: AsyncSession, username: str) -> User | None:
    """根据用户名查用户"""
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()

async def list_users(db: AsyncSession, skip: int = 0, limit: int = 10) -> list[User]:
    """分页查询用户列表"""
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

async def update_user_email(db: AsyncSession, user_id: int, new_email: str) -> User | None:
    """更新用户邮箱"""
    user = await get_user_by_id(db, user_id)
    if not user:
        return None
    user.email = new_email
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int) -> bool:
    """删除用户"""
    user = await get_user_by_id(db, user_id)
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True

# ------------------------------
# 7. FastAPI 接口层
# ------------------------------
@app.post("/users/", response_model=UserResp, summary="创建用户")
async def create_user_api(
    username: str,
    email: str,
    db: AsyncSession = Depends(get_db)
):
    # 用户名唯一性校验
    if await get_user_by_name(db, username):
        raise HTTPException(status_code=400, detail="用户名已存在")
    return await create_user(db, username, email)

@app.get("/users/{user_id}", response_model=UserResp, summary="根据ID查询用户")
async def get_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

@app.get("/users/", summary="查询用户列表")
async def list_users_api(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    users = await list_users(db, skip, limit)
    return {"code": 200, "data": users}

@app.put("/users/{user_id}", response_model=UserResp, summary="更新用户邮箱")
async def update_user_api(
    user_id: int,
    email: str,
    db: AsyncSession = Depends(get_db)
):
    user = await update_user_email(db, user_id, email)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

@app.delete("/users/{user_id}", summary="删除用户")
async def delete_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    if not await delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"code": 200, "message": "删除成功"}

# ------------------------------
# 启动入口
# ------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10086, reload=True)
```

------

#### 三、启动与测试

1. 将代码保存为 `main.py`
2. 启动服务：

```plain
python main.py
```

1. 打开浏览器访问接口文档，直接在线测试：

```plain
http://localhost:8000/docs
```

所有接口都可以点「Try it out」直接调用，验证数据库读写是否正常。

# 生产部署方案

生产推荐：**gunicorn \**\*\*+\*\**\* uvicorn worker**。安装与启动：

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

- -w 4：worker 数量，一般设置为 CPU 核心数*2+1
- -k UvicornWorker：使用 uvicorn 异步 worker
- -b 0.0.0.0:8000：监听所有网卡

线上前面再加 Nginx 做反向代理、ssl 证书、限流。容器化补充 Dockerfile：

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
```

# 课后实战小项目

实战：简易图书管理 API

1. 图书新增（POST），校验书名、价格
2. 查询图书列表（GET，分页）
3. 根据 id 查询单本图书
4. 删除图书接口
5. 增加 token 鉴权依赖
6. 全局统一返回格式