## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">产品概述</font>**
<font style="color:rgb(0, 0, 0);">Streamlit 是一款基于 Python 的</font>**<font style="color:rgb(0, 0, 0);">快速 Web 应用开发框架</font>**<font style="color:rgb(0, 0, 0);">，无需掌握前端 HTML、CSS、JavaScript 技术，仅依靠纯 Python 代码，即可在短时间内搭建可视化网页、交互系统、数据平台、AI 对话界面等应用。</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">核心特点</font>**
1. <font style="color:black;">开发效率极高</font>

<font style="color:black;">一行代码实现页面组件，开发流程简洁，几分钟即可完成功能页面搭建。</font>

2. <font style="color:black;">纯 Python 开发</font>

<font style="color:black;">全程使用 Python 语法编写，后端开发者、数据分析人员可快速上手，无前端学习成本。</font>

3. <font style="color:black;">原生丰富交互组件</font>

<font style="color:black;">内置文本输入、数字框、下拉选择、单选、多选、滑块、勾选框、聊天框、按钮等常用交互控件。</font>

<font style="color:black;">会话状态持久化</font>

<font style="color:black;">支持</font>

4. <font style="color:rgb(0, 0, 0);">session_state</font>

<font style="color:black;">全局状态存储，可保存用户输入、聊天记录、配置参数，页面刷新数据不丢失。</font>

5. <font style="color:black;">实时运行预览</font>

<font style="color:black;">代码保存自动刷新页面，调试直观，开发体验流畅。</font>

6. <font style="color:black;">轻量化部署</font>

<font style="color:black;">依赖少、启动快，支持本地运行、内网部署、服务器部署，适配多种办公与开发场景。</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">适用应用场景</font>**
+ <font style="color:black;">内部业务管理简易后台</font>
+ <font style="color:black;">数据分析可视化平台</font>
+ <font style="color:black;">AI 聊天机器人前端界面</font>
+ <font style="color:black;">算法调试演示平台</font>
+ <font style="color:black;">快速原型功能验证</font>
+ <font style="color:black;">办公自动化交互工具</font>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">环境安装</font>**
pip install streamlit

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">项目运行命令</font>**
streamlit run 项目文件名.py

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">常用核心组件说明</font>**
|    **<font style="color:rgb(0, 0, 0);">组件方法</font>**     |   **<font style="color:rgb(0, 0, 0);">功能用途</font>**   |
| :----------------------------------------------------------: | :-------------------------------------------------------: |
| <font style="color:rgb(0, 0, 0);">st.set_page_config</font>  |   <font style="color:rgb(0, 0, 0);">全局页面配置</font>   |
| <font style="color:rgb(0, 0, 0);">st.title / st.header</font> |   <font style="color:rgb(0, 0, 0);">页面标题设置</font>   |
|    <font style="color:rgb(0, 0, 0);">st.text_input</font>    |  <font style="color:rgb(0, 0, 0);">单行文本输入框</font>  |
|   <font style="color:rgb(0, 0, 0);">st.number_input</font>   |    <font style="color:rgb(0, 0, 0);">数字输入框</font>    |
|    <font style="color:rgb(0, 0, 0);">st.selectbox</font>     |    <font style="color:rgb(0, 0, 0);">下拉选择框</font>    |
|      <font style="color:rgb(0, 0, 0);">st.radio</font>       |     <font style="color:rgb(0, 0, 0);">单选按钮</font>     |
|   <font style="color:rgb(0, 0, 0);">st.multiselect</font>    |    <font style="color:rgb(0, 0, 0);">多选选择器</font>    |
|      <font style="color:rgb(0, 0, 0);">st.slider</font>      |  <font style="color:rgb(0, 0, 0);">数值滑动调节器</font>  |
|     <font style="color:rgb(0, 0, 0);">st.checkbox</font>     |    <font style="color:rgb(0, 0, 0);">复选勾选框</font>    |
|      <font style="color:rgb(0, 0, 0);">st.button</font>      |   <font style="color:rgb(0, 0, 0);">功能触发按钮</font>   |
|    <font style="color:rgb(0, 0, 0);">st.chat_input</font>    |  <font style="color:rgb(0, 0, 0);">对话聊天输入框</font>  |
|   <font style="color:rgb(0, 0, 0);">st.chat_message</font>   |   <font style="color:rgb(0, 0, 0);">聊天气泡展示</font>   |
|     <font style="color:rgb(0, 0, 0);">st.sidebar</font>      |  <font style="color:rgb(0, 0, 0);">侧边栏布局容器</font>  |
|     <font style="color:rgb(0, 0, 0);">st.columns</font>      |   <font style="color:rgb(0, 0, 0);">页面分栏布局</font>   |
|  <font style="color:rgb(0, 0, 0);">st.session_state</font>   | <font style="color:rgb(0, 0, 0);">全局数据状态存储</font> |


## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">完整代码</font>**
```python
import streamlit as st

# 页面全局配置
st.set_page_config(
    page_title="Streamlit 聊天机器人教学版",
    page_icon="🤖",
    layout="wide"
)

# 页面标题与说明
st.title("🤖 Streamlit AI 聊天机器人演示")
st.markdown("### 核心功能：各类用户输入控件 + 标准聊天界面")
st.divider()

# 侧边栏：机器人参数配置区
with st.sidebar:
    st.title("⚙️ 机器人设置")
    bot_name = st.text_input("机器人名称", value="智能助手")
    model_mode = st.selectbox(
        "选择对话模型风格",
        ["通用闲聊", "专业技术问答", "文案创作", "心理咨询"]
    )
    reply_len = st.radio("回复长度", ["简短", "中等", "详细"])
    enable_func = st.multiselect(
        "开启附加功能",
        ["联网搜索", "代码解释", "翻译", "总结"]
    )
    temperature = st.slider(
        "AI 创意程度",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )
    auto_clear = st.checkbox("发送后自动清空输入", value=False)

# 主页面：用户信息输入区
st.header("👤 用户信息输入区")
col1, col2 = st.columns(2)
with col1:
    user_nick = st.text_input("你的昵称", placeholder="请输入昵称...")
    user_age = st.number_input(
        "你的年龄",
        min_value=1,
        max_value=120,
        value=25
    )
with col2:
    user_gender = st.selectbox("性别", ["男", "女", "保密"])
    user_mood = st.slider("当前心情指数", 0, 10, 5)

st.divider()

# 核心模块：聊天窗口
st.header("💬 AI 聊天对话窗口")

# 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 渲染历史聊天记录
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 聊天输入框
user_input = st.chat_input("请在这里输入想问的问题...")

# 处理用户输入与AI回复
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 模拟AI回复（可替换为大模型API调用）
    ai_reply = f"""
你好 {user_nick if user_nick else "朋友"}！👋
你当前的心情指数：{user_mood}分（满分10分）
你发送的内容：{user_input}
---
🤖 机器人配置：
- 机器人名称：{bot_name}
- 对话模式：{model_mode}
- 回复长度：{reply_len}
- AI创意度：{temperature}
- 开启功能：{", ".join(enable_func) if enable_func else "无"}
---
提示：此为模拟回复，替换大模型API后可实现真实AI对话！
"""

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

    if auto_clear:
        st.rerun()

# 清空聊天记录按钮
if st.button("🔄 清空全部聊天记录"):
    st.session_state.messages = []
    st.rerun()

# 大模型对接示例（伪代码）
# import openai
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=st.session_state.messages
# )
# ai_reply = response.choices[0].message.content
```

  