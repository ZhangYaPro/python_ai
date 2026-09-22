## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">项目简介</font>**
<font style="color:rgb(0, 0, 0);">本项目基于Ollama本地大模型，利用streamlit实现前端界面，实现聊天对话机器人。</font>

<font style="color:rgb(0, 0, 0);">整体界面如下:</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666740729-80667375-3367-47dd-8c80-9b82f7eeb890.png" width="1662" alt="" title="" crop="0,0,1,1" id="u7a7fc76b" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">源码地址</font>**
<font style="color:rgb(0, 0, 0);">连接地址: </font>[<font style="color:rgb(239, 112, 96);">https://github.com/secondtonone1/python_ai</font>](https://github.com/secondtonone1/python_ai)

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">Ollama简介</font>**
<font style="color:black;background-color:rgb(255, 249, 249);">Ollama：是一款旨在简化大型语言模型本地部署和运行过程的开源软件。</font>

<font style="color:black;background-color:rgb(255, 249, 249);">中文名：羊驼</font>

<font style="color:black;background-color:rgb(255, 249, 249);">网址：</font>[<font style="color:rgb(239, 112, 96);background-color:rgb(255, 249, 249);">https://ollama.com/</font>](https://ollama.com/)

**<font style="color:rgb(0, 0, 0);">Ollama</font>**<font style="color:rgb(0, 0, 0);"> 是一款</font>**<font style="color:rgb(0, 0, 0);">开源、跨平台的本地大语言模型（LLM）运行与管理工具</font>**<font style="color:rgb(0, 0, 0);">，采用 MIT 许可，核心目标是让用户在个人设备上零门槛部署、管理和运行各类开源大模型，被称为 “大模型领域的 Docker”。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/svg/27211935/1778666739333-ff3bb1db-d281-402f-a598-5a0e8dc78f52.svg" width="256" alt="" title="" crop="0,0,1,1" id="ud5f03844" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px"><img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666739437-77080cc4-7b4b-41a6-a6cd-e27f227814cb.png" width="399" alt="" title="" crop="0,0,1,1" id="u07725994" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

### <font style="color:rgb(0, 0, 0);">核心定位</font>
+ **<font style="color:black;">本地化优先</font>**<font style="color:black;">：所有数据与计算在本机完成，不上云，保障</font>**<font style="color:black;">隐私安全</font>**<font style="color:black;">与</font>**<font style="color:black;">离线可用</font>**<font style="color:black;">。</font>
+ **<font style="color:black;">极简部署</font>**<font style="color:black;">：封装底层环境、格式转换、硬件适配等复杂细节，实现</font>**<font style="color:black;">一条命令安装、一条命令拉取 / 运行模型</font>**<font style="color:black;">。</font>
+ **<font style="color:black;">模型管家</font>**<font style="color:black;">：统一管理主流开源模型，支持一键下载、删除、更新与版本控制。</font>

### <font style="color:rgb(0, 0, 0);">主要特点</font>
1. **<font style="color:black;">跨平台</font>**<font style="color:black;">：支持 Windows、macOS、Linux，也可通过 Docker 部署。</font>
2. **<font style="color:black;">硬件友好</font>**<font style="color:black;">：自动识别并调用 NVIDIA/AMD GPU、Apple Silicon 加速；支持 GGUF 量化，降低显存门槛，普通电脑也能运行 7B–70B 模型。</font>
3. **<font style="color:black;">丰富模型库</font>**<font style="color:black;">：内置 Llama 3、Qwen、DeepSeek、Mistral、Gemma 等主流开源模型，支持社区自定义模型。</font>
4. **<font style="color:black;">标准 REST API</font>**<font style="color:black;">：默认提供 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">http://localhost:11434</font>`<font style="color:black;"> 接口，涵盖模型管理、对话、生成、流式输出等，</font>**<font style="color:black;">兼容 OpenAI 接口格式</font>**<font style="color:black;">，便于集成到 Apifox、Postman 或自研应用。</font>
5. **<font style="color:black;">开发者友好</font>**<font style="color:black;">：提供 Python/JS/Go 等 SDK，支持多轮对话、上下文记忆、思考链输出与工具调用。</font>

### <font style="color:rgb(0, 0, 0);">典型用途</font>
+ <font style="color:black;">隐私敏感场景（企业内部文档、个人数据处理）</font>
+ <font style="color:black;">离线环境（无网 / 弱网）智能助手开发</font>
+ <font style="color:black;">快速本地调试与原型验证（无需云端账号）</font>
+ <font style="color:black;">构建私有知识库与 RAG 应用Ollama</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">Ollama部署安装</font>**
### <font style="color:rgb(0, 0, 0);">环境说明</font>
+ <font style="color:black;">支持系统：</font>**<font style="color:black;">Windows / macOS / Linux</font>**
+ <font style="color:black;">默认服务端口：</font>**<font style="color:black;">11434</font>**
+ <font style="color:black;">安装后默认本地接口地址：</font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">http://localhost:11434</font>`
+ <font style="color:black;">自动后台常驻运行，开机自启</font>

### <font style="color:rgb(0, 0, 0);">Windows 安装</font>
1. <font style="color:black;">官网下载安装包：</font>[<font style="color:rgb(239, 112, 96);">https://ollama.com/download/windows</font>](https://ollama.com/download/windows)
2. <font style="color:black;">双击 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">OllamaSetup.exe</font>`<font style="color:black;"> 默认下一步安装即可</font>
3. <font style="color:black;">安装完成自动启动后台服务</font>
4. <font style="color:black;">验证安装（CMD/PowerShell 执行）</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666740924-4f18096c-a404-4eb8-951e-3f7af2fbc884.png" width="868" alt="" title="" crop="0,0,1,1" id="u6e228696" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<font style="color:rgb(0, 0, 0);">安装好后重新开cmd测试</font>

ollama --version

### <font style="color:rgb(0, 0, 0);">macOS 安装</font>
**<font style="color:rgb(0, 0, 0);">方式 1：官网安装包</font>**

<font style="color:rgb(0, 0, 0);">下载：</font>[<font style="color:rgb(239, 112, 96);">https://ollama.com/download/mac</font>](https://ollama.com/download/mac)

<font style="color:rgb(0, 0, 0);">拖拽到应用程序，打开即自动部署后台服务。</font>

**<font style="color:rgb(0, 0, 0);">方式 2：Homebrew 安装</font>**

brew install ollama

<font style="color:rgb(0, 0, 0);">启动服务：</font>

ollama serve

### <font style="color:rgb(0, 0, 0);">Linux 安装（推荐一键脚本）</font>
**<font style="color:rgb(0, 0, 0);">一键安装（通用）</font>**

<font style="color:rgb(0, 0, 0);">运行</font>

curl -fsSL https://ollama.com/install.sh | sh

+ <font style="color:black;">自动配置系统服务、开机自启、后台守护进程</font>
+ <font style="color:black;">安装完成直接可用</font>

### <font style="color:rgb(0, 0, 0);">手动启停服务</font>
<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 启动
systemctl start ollama

# 停止
systemctl stop ollama

# 开机自启
systemctl enable ollama
```

### <font style="color:rgb(0, 0, 0);">Docker 容器安装（服务器 / 隔离环境推荐）</font>
**<font style="color:rgb(0, 0, 0);">1. 拉取镜像并启动</font>**

<font style="color:rgb(0, 0, 0);">运行</font>

```bash
docker run -d \
-v ollama:/root/.ollama \
-p 11434:11434 \
--name ollama \
ollama/ollama
```

**<font style="color:rgb(0, 0, 0);">2. 容器内操作模型</font>**

<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 进入容器
docker exec -it ollama bash

# 拉取并运行模型
ollama run llama3
```

### <font style="color:rgb(0, 0, 0);">安装后基础验证（全平台通用）</font>
1. <font style="color:black;">命令行测试拉取模型运行</font>

ollama run deepseek-r1:1.5b

1. <font style="color:black;">API 接口连通性测试</font>

<font style="color:rgb(0, 0, 0);">运行</font>

curl http://localhost:11434/api/tags

<font style="color:rgb(0, 0, 0);">能返回本地模型列表即安装部署正常。</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">Ollama命令</font>**
### <font style="color:rgb(0, 0, 0);">基础版本与服务命令</font>
<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 查看版本
ollama --version

# 手动启动服务
ollama serve
```

### <font style="color:rgb(0, 0, 0);">模型拉取与运行</font>
<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 拉取模型
ollama pull 模型名

# 交互式运行模型
ollama run 模型名
```

### <font style="color:rgb(0, 0, 0);">模型管理命令</font>
<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 查看本地已安装所有模型
ollama list

# 删除本地模型
ollama rm 模型名

# 查看模型详细信息
ollama show 模型名
```

### <font style="color:rgb(0, 0, 0);">进阶常用命令</font>
<font style="color:rgb(0, 0, 0);">运行</font>

```bash
# 停止正在运行的模型
ollama stop 模型名

# 查看运行日志
ollama logs

# 复制模型（自定义别名）
ollama create 新模型名 -f Modelfile
```

**<font style="color:rgb(0, 0, 0);">编程代码助手（适合 IT 教学）</font>**

<font style="color:rgb(0, 0, 0);">新建文件命名 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Modelfile</font>`<font style="color:rgb(0, 0, 0);">，内容：</font>

```dockerfile
FROM llama3:latest
PARAMETER temperature 0.3
SYSTEM """
你是资深编程老师，擅长Python、C++、Go、Rust、Java、嵌入式开发。
讲解代码通俗易懂，给出完整可运行示例，
会加关键注释，一步步拆解思路，适合零基础学习。
"""
```

<font style="color:rgb(0, 0, 0);">创建命令：</font>

ollama create code-teacher -f Modelfile

<font style="color:rgb(0, 0, 0);">运行</font>

ollama run code-teacher

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">HTTP协议基础</font>**
<font style="color:rgb(0, 0, 0);">Ollama启动后将作为本地HTTP接口服务运行，所有模型管理、对话生成等操作均需通过HTTP请求完成。因此，掌握HTTP基础是实现Ollama对接的前提。</font>

### <font style="color:rgb(0, 0, 0);">HTTP协议定义</font>
<font style="color:rgb(0, 0, 0);">HTTP（超文本传输协议）是客户端与服务端之间进行数据通信的通用网络协议，规定了客户端发起请求、服务端返回响应的标准格式与交互规则。在Ollama对接场景中，客户端（Apifox、代码、浏览器等）通过HTTP请求与Ollama服务端进行交互，获取模型服务。</font>

### <font style="color:rgb(0, 0, 0);">核心角色</font>
+ <font style="color:black;">客户端：主动发起HTTP请求的主体，包括Apifox、Python/Java代码、浏览器、嵌入式程序等。</font>
+ <font style="color:black;">服务端：被动接收并响应HTTP请求的主体，即本地启动的Ollama服务，默认占用11434端口。</font>

### <font style="color:rgb(0, 0, 0);">核心请求方式</font>
<font style="color:rgb(0, 0, 0);">Ollama接口仅涉及两种HTTP请求方式，根据业务场景选择使用：</font>

**<font style="color:rgb(0, 0, 0);">GET请求</font>**

<font style="color:rgb(0, 0, 0);">用途：从Ollama服务端获取已存在的数据，不修改服务端数据。</font>

<font style="color:rgb(0, 0, 0);">特点：无请求体，请求参数可拼接在URL末尾，适用于查询类操作。</font>

**<font style="color:rgb(0, 0, 0);">POST请求</font>**

<font style="color:rgb(0, 0, 0);">用途：向Ollama服务端提交数据、发起业务请求，如对话交互、文本生成、模型拉取等。</font>

<font style="color:rgb(0, 0, 0);">特点：支持请求体，常用JSON格式传递参数，数据传输安全、可承载内容量大，适用于提交类、指令类操作。</font>

### <font style="color:rgb(0, 0, 0);">HTTP接口三要素</font>
<font style="color:rgb(0, 0, 0);">调用任何HTTP接口，需明确以下三要素，Ollama接口也遵循此规则：</font>

1. <font style="color:black;">请求地址（URL）：Ollama服务的基础地址固定为 </font>[<font style="color:rgb(239, 112, 96);">http://localhost:11434</font>](http://localhost:11434)<font style="color:black;">，接口路径拼接在基础地址后。</font>
2. <font style="color:black;">请求方法（GET/POST）：根据接口功能选择，查询用GET，提交/指令用POST。</font>
3. <font style="color:black;">请求体/参数：POST请求通过JSON格式传递参数（如模型名、提问内容）；GET请求参数可省略或拼接在URL后。</font>

**<font style="color:rgb(0, 0, 0);">地址区分</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666740837-d637ff08-987e-418d-9a06-df94388677e8.png" width="1242" alt="" title="" crop="0,0,1,1" id="u196240e2" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741102-3fa9bc75-a436-40d1-8cd7-4f9883ae85a8.png" width="1169" alt="" title="" crop="0,0,1,1" id="u0a7025c1" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">浏览器访问Ollama服务</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741056-5435153d-5012-4003-bfa0-60a0e5508cca.png" width="667" alt="" title="" crop="0,0,1,1" id="uaa42deef" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

### <font style="color:rgb(0, 0, 0);">数据交互格式</font>
<font style="color:rgb(0, 0, 0);">Ollama所有接口的请求参数与响应数据均采用JSON格式。JSON为键值对结构，具有易读性强、跨编程语言兼容的特点，可被Python、Java、嵌入式开发相关编程语言直接解析。</font>

<font style="color:rgb(0, 0, 0);">Ollama的核心运行机制是启动本地HTTP服务，监听11434端口。开发者通过客户端发起HTTP请求，向Ollama服务端传递指令（如查询模型、发起对话），Ollama服务端执行对应操作后，以JSON格式返回响应数据。掌握HTTP基础后，即可通过标准HTTP请求实现Ollama接口的调用。</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">Ollama核心API接口</font>**
<font style="color:rgb(0, 0, 0);">以下为Ollama常用核心API接口，结合前文HTTP基础知识点，明确接口调用细节，可直接用于实操调试。</font>

### <font style="color:rgb(0, 0, 0);">查看本地模型列表</font>
<font style="color:rgb(0, 0, 0);">用途：查询本地已安装的所有Ollama模型信息，包括模型名、修改时间、大小等。</font>

+ <font style="color:black;">请求方式：GET</font>
+ <font style="color:black;">接口地址：</font>[<font style="color:rgb(239, 112, 96);">http://localhost:11434/api/tags</font>](http://localhost:11434/api/tags)
+ <font style="color:black;">实操说明：使用Apifox或浏览器，选择GET请求，输入接口地址，发起请求后，将返回JSON格式的本地模型列表。</font>

### <font style="color:rgb(0, 0, 0);">大模型对话接口</font>
<font style="color:rgb(0, 0, 0);">用途：与Ollama模型进行多轮对话交互，适用于智能助手、聊天类功能开发。</font>

+ <font style="color:black;">请求方式：POST</font>
+ <font style="color:black;">接口地址：</font>[<font style="color:rgb(239, 112, 96);">http://localhost:11434/api/chat</font>](http://localhost:11434/api/chat)
+ <font style="color:black;">请求体（JSON格式）：</font>

```json
{
  "model": "deepseek-r1:1.5b",  
  "messages": [{"role": "user", "content": "有什么减肥方案"}],  
  "stream": false  
}
```



**<font style="color:rgb(0, 0, 0);">服务器回复</font>**

```json
{
  "model": "deepseek-r1:1.5b",
  "created_at": "2026-05-17T02:15:27.140973Z",
  "message": {
    "role": "assistant",
    "content": "<think>\n嗯，我现在想减肥，可是有点不知道从哪里开始。我记得之前没动过动脑筋，只是简单地吃得多喝得多。可是现在想减肥了，怎么办呢？我需要一个具体的计划，而不是走一遍水路。\n\n首先，我觉得要制定一个长期的计划比较好，毕竟减肥不是一蹴而就的事情。不过具体怎么制定呢？是不是需要先了解自己的身体状况，比如体重、身高、体型、还有最近吃的东西和运动的情况？\n\n然后，饮食方面我有点犹豫。以前总是吃 lots of junk food，好像长得很高。现在如果想要减肥，早餐应该怎么做？比如，早上要不要吃早饭？有没有什么容易引起肚子痛的食物，或者容易反弹的食物呢？\n\n接着，运动也很重要，可是我现在不太喜欢动。不过我可以试着找一些小技巧，比如走一下楼梯、坐一下镜子之类的。但问题是，这些小动作可能效果有限，我需要坚持下去吗？\n\n另外，还有其他方面的因素，比如体重管理和心情调整，这些也需要考虑进去吗？因为有时候只是吃不消，或者运动也不如预期，可能会导致心情不好，甚至反弹减肥。\n\n我还发现以前的饮食习惯比较单一，比如多吃肉类、蔬菜少食乳制品之类的。现在是不是应该改变一下饮食结构，多摄入一些蛋白质和健康脂肪，同时控制总热量摄入？\n\n我还不太清楚如何具体实施这些计划。或许我可以先看看有没有什么资源或者工具能帮助我制定减肥计划？比如手机上的减肥APP、专业医生的建议等等。\n\n还有一个问题是，如果体重管理不好，可能会导致反弹。这时候该怎么办呢？是不是需要给自己设定一个合理的目标，不急于减少，而是逐步减少，同时注意不要吃太多或过量的零食和饮料？\n\n总之，我觉得我需要从以下几个方面入手：\n\n1. 了解自己的身体状况，制定长期计划。\n2. 制定饮食计划，选择易消化的食物和适量的运动。\n3. 改变饮食习惯，增加健康脂肪摄入，减少高热量食物。\n4. 注意体重管理，设定合理的目标，避免反弹。\n5. 给自己时间和坚持，不要因为一点事情而放弃。\n\n不过现在还不知道具体怎么操作，可能需要更多的实际例子或者步骤。或许可以先从制定计划开始，看看有没有可行的方法。\n\n比如，我听说过有特定的饮食建议，比如每天吃3个苹果、一个橙子之类的健康水果，这样能提供足够的营养和能量。还有均衡性的饮食结构，比如多吃蔬菜、瘦肉，少食高糖高脂食物。\n\n运动方面，我可以尝试散步、跑步或者其他可以增加热量消耗的运动方式，但需要有意识地进行，不能随便动来动去，否则容易受伤或者感到不适。\n\n另外，我还记得之前有一些减肥视频，里面有很多技巧，比如定时吃饭、避免过多摄入糖分等等。或许这些视频能给我一些实用的建议和方法。\n\n还有，我还需要了解自己的体脂率，看看目前属于轻薄还是肥胖，进而调整饮食和运动计划。如果体脂率较高，可能需要更多的控制和变化，但如果是过胖的话，可能需要更严格的限制。\n\n也许我可以先从最基础的部分开始，比如每天吃3-4个苹果、一个橙子，或者更多的健康水果，来补充能量和蛋白质。同时，每周安排一定的时间进行小的运动，比如散步或做简单的拉伸，这样可以增加肌肉量，也有助于保持体重。\n\n另外，饮食方面，我可以尽量减少高脂肪食物和高糖食物，多吃一些低脂、低饱和的食物，同时避免辛辣刺激性食物，这些都是容易反弹的食物来源。\n\n关于运动，我需要找到合适的时间进行锻炼，比如在下午或者晚上，而不是早上或晚上。这样可以保证有足够的睡眠时间，有助于恢复体力。\n\n还有，如果我最近有其他健康问题，比如高血压或者糖尿病，可能会影响减肥效果，这时候需要特别注意，避免过度消耗能量或者增加饮食中的热量来源。\n\n总的来说，我觉得制定一个合理的计划是一个关键步骤，不过需要耐心和坚持。可能我会遇到一些困难，但只要逐步调整和坚持下去，应该能够达到目标体重。\n</think>\n\n为了有效进行减肥，以下是一份详细的计划建议：\n\n### 1. 定期制定长期计划\n- **设定目标**：明确减肥的目标，例如每周减少5-7公斤，或者达到某个体脂率（如20%-25%）。\n- **了解身体状况**：检查体重、身高、体型和最近饮食和运动的记录。定期复查这些数据，确保信息无误。\n\n### 2. 制定饮食计划\n- **蛋白质摄入**：每天吃3-4个健康水果（如苹果、橘子）、一个蔬菜（如胡萝卜、青菜）和1-2个瘦肉（如鸡肉、 ham），均衡增加蛋白质。\n- **高热量食物控制**：避免过多摄入糖分和油炸食品，选择低脂、低饱和的高蛋白零食，如坚果、燕麦等。\n- **健康脂肪摄入**：每天摄入至少1.5-2杯豆类或水果（如菠菜）、少量鱼肉或鸡肉，增加纤维和热量来源。\n- **控制总热量**：减少食糖和油炸食物的摄入，通过减少零食选择低糖高纤维食物来平衡热量。\n\n### 3. 改变饮食习惯\n- **定时吃饭**：吃三餐后2-3小时分餐，避免过量或突然用餐。\n- **避免过量零食**：避免吃过多盐、油和巧克力，尤其是那些容易反弹的零食。\n- **减少高脂肪食物**：如肥肉、鸡胸肉、红烧鱼等，增加健康脂肪摄入。\n\n### 4. 注意体重管理\n- **设定合理目标**：通过饮食调整和运动，设定每周或每月体重目标（如1公斤/周）。\n- **避免极端减肥**：不要过度减肥，避免暴饮暴食导致反弹。保持平和心态，逐步减少不必要的零食摄入。\n\n### 5. 给予心情调整\n- **设定小目标**：每天设定较小的减重目标，例如“今天吃10个苹果”，逐步增加难度。\n- **记录饮食和运动**：详细记录每周的饮食、运动和心理活动，帮助分析并及时调整计划。\n\n### 6. 持续坚持\n- **减少外界压力**：学会控制情绪，避免过度减肥带来的焦虑或反弹感。\n- **寻求专业建议**：如有健康问题（如高血压/糖尿病），咨询医生以确保运动和饮食的合理性。\n\n通过以上步骤，逐步制定和执行计划，有助于有效减肥。耐心和坚持是关键，调整和优化计划需要时日积累，逐步实现目标体重。"
  },
  "done_reason": "stop",
  "done": true,
  "total_duration": 14123381000,
  "load_duration": 38089100,
  "prompt_eval_count": 6,
  "prompt_eval_duration": 15000000,
  "eval_count": 1420,
  "eval_duration": 14069000000
}
```

**<font style="color:rgb(0, 0, 0);">让模型有记忆</font>**

<font style="color:rgb(0, 0, 0);">客户端追问问题，需要在原有的请求和回答的基础上，继续追问才可以</font>

<font style="color:rgb(0, 0, 0);">将客户端和ollama服务器回复的结果，做成列表，放入messages中</font>

```json
{
  "model": "deepseek-r1:1.5b",  
  "messages": [
    {"role": "user", "content": "有什么减肥方案?"},
    {"role": "assistant", "content": "<think>\n嗯，我现在想减肥，可是有点不知道从哪里开始。我记得之前没动过动脑筋，只是简单地吃得多喝得多。可是现在想减肥了，怎么办呢？我需要一个具体的计划，而不是走一遍水路。\n\n首先，我觉得要制定一个长期的计划比较好，毕竟减肥不是一蹴而就的事情。不过具体怎么制定呢？是不是需要先了解自己的身体状况，比如体重、身高、体型、还有最近吃的东西和运动的情况？\n\n然后，饮食方面我有点犹豫。以前总是吃 lots of junk food，好像长得很高。现在如果想要减肥，早餐应该怎么做？比如，早上要不要吃早饭？有没有什么容易引起肚子痛的食物，或者容易反弹的食物呢？\n\n接着，运动也很重要，可是我现在不太喜欢动。不过我可以试着找一些小技巧，比如走一下楼梯、坐一下镜子之类的。但问题是，这些小动作可能效果有限，我需要坚持下去吗？\n\n另外，还有其他方面的因素，比如体重管理和心情调整，这些也需要考虑进去吗？因为有时候只是吃不消，或者运动也不如预期，可能会导致心情不好，甚至反弹减肥。\n\n我还发现以前的饮食习惯比较单一，比如多吃肉类、蔬菜少食乳制品之类的。现在是不是应该改变一下饮食结构，多摄入一些蛋白质和健康脂肪，同时控制总热量摄入？\n\n我还不太清楚如何具体实施这些计划。或许我可以先看看有没有什么资源或者工具能帮助我制定减肥计划？比如手机上的减肥APP、专业医生的建议等等。\n\n还有一个问题是，如果体重管理不好，可能会导致反弹。这时候该怎么办呢？是不是需要给自己设定一个合理的目标，不急于减少，而是逐步减少，同时注意不要吃太多或过量的零食和饮料？\n\n总之，我觉得我需要从以下几个方面入手：\n\n1. 了解自己的身体状况，制定长期计划。\n2. 制定饮食计划，选择易消化的食物和适量的运动。\n3. 改变饮食习惯，增加健康脂肪摄入，减少高热量食物。\n4. 注意体重管理，设定合理的目标，避免反弹。\n5. 给自己时间和坚持，不要因为一点事情而放弃。\n\n不过现在还不知道具体怎么操作，可能需要更多的实际例子或者步骤。或许可以先从制定计划开始，看看有没有可行的方法。\n\n比如，我听说过有特定的饮食建议，比如每天吃3个苹果、一个橙子之类的健康水果，这样能提供足够的营养和能量。还有均衡性的饮食结构，比如多吃蔬菜、瘦肉，少食高糖高脂食物。\n\n运动方面，我可以尝试散步、跑步或者其他可以增加热量消耗的运动方式，但需要有意识地进行，不能随便动来动去，否则容易受伤或者感到不适。\n\n另外，我还记得之前有一些减肥视频，里面有很多技巧，比如定时吃饭、避免过多摄入糖分等等。或许这些视频能给我一些实用的建议和方法。\n\n还有，我还需要了解自己的体脂率，看看目前属于轻薄还是肥胖，进而调整饮食和运动计划。如果体脂率较高，可能需要更多的控制和变化，但如果是过胖的话，可能需要更严格的限制。\n\n也许我可以先从最基础的部分开始，比如每天吃3-4个苹果、一个橙子，或者更多的健康水果，来补充能量和蛋白质。同时，每周安排一定的时间进行小的运动，比如散步或做简单的拉伸，这样可以增加肌肉量，也有助于保持体重。\n\n另外，饮食方面，我可以尽量减少高脂肪食物和高糖食物，多吃一些低脂、低饱和的食物，同时避免辛辣刺激性食物，这些都是容易反弹的食物来源。\n\n关于运动，我需要找到合适的时间进行锻炼，比如在下午或者晚上，而不是早上或晚上。这样可以保证有足够的睡眠时间，有助于恢复体力。\n\n还有，如果我最近有其他健康问题，比如高血压或者糖尿病，可能会影响减肥效果，这时候需要特别注意，避免过度消耗能量或者增加饮食中的热量来源。\n\n总的来说，我觉得制定一个合理的计划是一个关键步骤，不过需要耐心和坚持。可能我会遇到一些困难，但只要逐步调整和坚持下去，应该能够达到目标体重。\n</think>\n\n为了有效进行减肥，以下是一份详细的计划建议：\n\n### 1. 定期制定长期计划\n- **设定目标**：明确减肥的目标，例如每周减少5-7公斤，或者达到某个体脂率（如20%-25%）。\n- **了解身体状况**：检查体重、身高、体型和最近饮食和运动的记录。定期复查这些数据，确保信息无误。\n\n### 2. 制定饮食计划\n- **蛋白质摄入**：每天吃3-4个健康水果（如苹果、橘子）、一个蔬菜（如胡萝卜、青菜）和1-2个瘦肉（如鸡肉、 ham），均衡增加蛋白质。\n- **高热量食物控制**：避免过多摄入糖分和油炸食品，选择低脂、低饱和的高蛋白零食，如坚果、燕麦等。\n- **健康脂肪摄入**：每天摄入至少1.5-2杯豆类或水果（如菠菜）、少量鱼肉或鸡肉，增加纤维和热量来源。\n- **控制总热量**：减少食糖和油炸食物的摄入，通过减少零食选择低糖高纤维食物来平衡热量。\n\n### 3. 改变饮食习惯\n- **定时吃饭**：吃三餐后2-3小时分餐，避免过量或突然用餐。\n- **避免过量零食**：避免吃过多盐、油和巧克力，尤其是那些容易反弹的零食。\n- **减少高脂肪食物**：如肥肉、鸡胸肉、红烧鱼等，增加健康脂肪摄入。\n\n### 4. 注意体重管理\n- **设定合理目标**：通过饮食调整和运动，设定每周或每月体重目标（如1公斤/周）。\n- **避免极端减肥**：不要过度减肥，避免暴饮暴食导致反弹。保持平和心态，逐步减少不必要的零食摄入。\n\n### 5. 给予心情调整\n- **设定小目标**：每天设定较小的减重目标，例如“今天吃10个苹果”，逐步增加难度。\n- **记录饮食和运动**：详细记录每周的饮食、运动和心理活动，帮助分析并及时调整计划。\n\n### 6. 持续坚持\n- **减少外界压力**：学会控制情绪，避免过度减肥带来的焦虑或反弹感。\n- **寻求专业建议**：如有健康问题（如高血压/糖尿病），咨询医生以确保运动和饮食的合理性。\n\n通过以上步骤，逐步制定和执行计划，有助于有效减肥。耐心和坚持是关键，调整和优化计划需要时日积累，逐步实现目标体重。"},
    {"role": "user", "content": "还有什么推荐的方案吗？"}
  ],  
  "stream": false  
}
```



### <font style="color:rgb(0, 0, 0);">文本生成接口</font>
<font style="color:rgb(0, 0, 0);">用途：根据指定提示词，让Ollama模型生成文本内容（非对话场景，如文案、代码生成）。</font>

+ <font style="color:black;">请求方式：POST</font>
+ <font style="color:black;">接口地址：</font>[<font style="color:rgb(239, 112, 96);">http://localhost:11434/api/generate</font>](http://localhost:11434/api/generate)
+ <font style="color:black;">请求体（JSON格式）：</font>

```json
{
  "model": "llama3:latest",  // 模型名称
  "prompt": "写一段Python大模型开发的入门文案",  // 文本生成提示词
  "stream": false  // 关闭流式输出
}
```

### <font style="color:rgb(0, 0, 0);">接口通用注意事项</font>
+ <font style="color:black;">调用接口前，需确保Ollama服务已启动，且端口11434未被占用。</font>
+ <font style="color:black;">POST请求必须指定请求头Content-Type: application/json，否则会导致请求失败。</font>
+ <font style="color:black;">请求体中model参数需填写本地已安装的模型名称，否则会返回模型不存在错误。</font>
+ <font style="color:black;">stream参数设为true时，将采用流式输出（实时返回响应内容），适合前端展示；false为一次性返回完整响应。</font>



## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">ApiFox对接Ollama</font>**
### <font style="color:rgb(0, 0, 0);">ApiFox官网</font>
[<font style="color:rgb(239, 112, 96);">https://apifox.com/?utm_source=bing&utm_medium=sem&utm_campaign=%E5%93%81%E7%89%8C%E8%AF%8D-Apifox&utm_content=Apifox-%E6%A0%B8%E5%BF%83&utm_term=apifox%E5%AE%98%E7%BD%91&search_term=apifox%E5%AE%98%E7%BD%91&msclkid=dee3617345c31b6b779e0b775b7a686a</font>](https://apifox.com/?utm_source=bing&utm_medium=sem&utm_campaign=%E5%93%81%E7%89%8C%E8%AF%8D-Apifox&utm_content=Apifox-%E6%A0%B8%E5%BF%83&utm_term=apifox%E5%AE%98%E7%BD%91&search_term=apifox%E5%AE%98%E7%BD%91&msclkid=dee3617345c31b6b779e0b775b7a686a)

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741317-a047414e-7811-4516-a214-110a443e370c.png" width="1217" alt="" title="" crop="0,0,1,1" id="u33653b5b" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">ApiFox测试HTTP</font>**
**<font style="color:rgb(0, 0, 0);">创建项目</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741370-4816cef0-e3fd-4110-87ca-154c4c3026fb.png" width="1406" alt="" title="" crop="0,0,1,1" id="u9ec72e07" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">选择空白项目</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741422-ee7bd145-7663-4f3b-a877-9f14c0ce4cd9.png" width="1350" alt="" title="" crop="0,0,1,1" id="u38a9d23e" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">输入请求连接和内容</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742058-eb39c43c-5358-4217-a687-2b06ede27914.png" width="1176" alt="" title="" crop="0,0,1,1" id="u1b765315" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">请求内容</font>**

```json
{
  "model": "deepseek-r1:1.5b",  
  "messages": [{"role": "user", "content": "你好，介绍一下自己"}], 
  "stream": false  
}
```

**<font style="color:rgb(0, 0, 0);">请求链接</font>**

http://localhost:11434/api/chat

**<font style="color:rgb(0, 0, 0);">回复内容</font>**

```json
{
  "model": "deepseek-r1:1.5b",
  "created_at": "2026-05-13T07:49:24.5359256Z",
  "message": {
    "role": "assistant",
    "content": "<think>\n\n</think>\n\n你好！我是DeepSeek-R1，一个由深度求索公司开发的智能助手。关于我以及我的能力，我始终遵循人工智能的原理与规则，旨在为您提供准确和 helpful 的信息。请问有什么可以为您服务的？"
  },
  "done_reason": "stop",
  "done": true,
  "total_duration": 1597406000,
  "load_duration": 967306500,
  "prompt_eval_count": 7,
  "prompt_eval_duration": 128000000,
  "eval_count": 54,
  "eval_duration": 499000000
}
```

**<font style="color:rgb(0, 0, 0);">使用Ollama规则构建apifox的请求项目</font>**

<font style="color:rgb(0, 0, 0);">我用豆包生成了一个Ollama.apifox.json文件，放入资料包了，大家可以去源码中查看</font>

[<font style="color:rgb(239, 112, 96);">https://github.com/secondtonone1/python_ai/blob/master/base/09_%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%90%AD%E5%BB%BA/%E8%B5%84%E6%96%99/Ollama.apifox.json</font>](https://github.com/secondtonone1/python_ai/blob/master/base/09_%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%90%AD%E5%BB%BA/%E8%B5%84%E6%96%99/Ollama.apifox.json)

<font style="color:rgb(0, 0, 0);">可以再次新建一个项目，这次导入json文件即可</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741743-bf9e9452-4950-4339-b736-2664fd378a96.png" width="1224" alt="" title="" crop="0,0,1,1" id="u91b5eda3" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741920-511d19c7-96c1-4542-b38d-f55bc3293a61.png" width="853" alt="" title="" crop="0,0,1,1" id="u39ab2d59" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666741844-d006d52e-f4ad-4c48-9ee9-f1ea3dc73c7f.png" width="880" alt="" title="" crop="0,0,1,1" id="u758eb0de" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742018-815319fd-4ee6-4c84-91c3-b43bef1b6c18.png" width="1507" alt="" title="" crop="0,0,1,1" id="u980e0085" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742229-20c5c8eb-7048-4a7e-b14a-604ce188b5b6.png" width="861" alt="" title="" crop="0,0,1,1" id="ufc57e723" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742961-4b354651-1b74-4187-9d64-43c611a19ae9.png" width="1411" alt="" title="" crop="0,0,1,1" id="u48fe08c6" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">接口环境配置</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742647-06891a57-311b-4817-ba48-054302ce57b8.png" width="1563" alt="" title="" crop="0,0,1,1" id="u4ec90ae3" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742608-556725e6-7839-4058-af07-7afb7c98f765.png" width="1284" alt="" title="" crop="0,0,1,1" id="u5d08520e" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742785-1bc5ebe4-59c1-4896-8108-3fc0d32df0bf.png" width="1182" alt="" title="" crop="0,0,1,1" id="u98cbd193" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">调试</font>**

<font style="color:rgb(0, 0, 0);">调试内容和之前一致，无需修改</font>

```json
{
  "model": "deepseek-r1:1.5b",  
  "messages": [{"role": "user", "content": "你好，介绍一下自己"}], 
  "stream": false  
}
```

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1778666742914-95ec904c-bf38-4dff-aace-3ade9f516755.png" width="1166" alt="" title="" crop="0,0,1,1" id="u29073bb1" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

  