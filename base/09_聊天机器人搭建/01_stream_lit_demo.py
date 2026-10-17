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
st.divider()  #分割线

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