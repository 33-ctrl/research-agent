import os
from dotenv import load_dotenv
import streamlit as st
from zai import ZhipuAiClient

# 读取 .env 文件
load_dotenv()

# 页面基础设置
st.set_page_config(page_title="联网研究 Agent", page_icon="🔎")

st.title("🔎 联网研究 Agent")
st.write("输入一个研究主题，程序会自动联网搜索，并生成中文研究报告。")

# 读取 API Key
api_key = os.getenv("ZAI_API_KEY")

if not api_key:
    st.error("没有读取到 ZAI_API_KEY。请检查 .env 文件是否正确。")
    st.stop()

# 创建智谱客户端
client = ZhipuAiClient(api_key=api_key)

# 保存多轮对话历史
if "history" not in st.session_state:
    st.session_state.history = []

# 输入框
topic = st.text_input("请输入研究主题：", "AI Agent 在学习中的应用")

# 生成按钮
if st.button("开始研究"):
    if not topic.strip():
        st.warning("请输入一个主题。")
        st.stop()

    tools = [
        {
            "type": "web_search",
            "web_search": {
                "enable": "True",
                "search_engine": "search_pro",
                "search_result": "True",
                "count": "5",
                "content_size": "high",
                "search_prompt": (
                    "你是一名专业中文研究员。"
                    "请基于联网搜索结果，输出一份中文 Markdown 研究报告。"
                    "报告必须包含以下部分："
                    "1. 一句话结论 "
                    "2. 关键发现 "
                    "3. 风险与争议 "
                    "4. 可执行建议 "
                    "5. 参考来源。"
                    "要求语言清晰，适合新手学习和面试准备。"
                )
            }
        }
    ]

    messages = st.session_state.history + [
        {"role": "user", "content": topic}
    ]

    with st.spinner("正在联网搜索并生成报告，请稍等..."):
        response = client.chat.completions.create(
            model="glm-4-air",
            messages=messages,
            tools=tools
        )

    answer = response.choices[0].message.content

    # 记录历史
    st.session_state.history.append({"role": "user", "content": topic})
    st.session_state.history.append({"role": "assistant", "content": answer})

    st.success("研究完成。")
    st.markdown(answer)

# 继续追问
st.divider()
follow_up = st.text_input("继续追问（可选）：", "")

if st.button("发送追问"):
    if not follow_up.strip():
        st.warning("请输入追问内容。")
        st.stop()

    tools = [
        {
            "type": "web_search",
            "web_search": {
                "enable": "True",
                "search_engine": "search_pro",
                "search_result": "True",
                "count": "5",
                "content_size": "high",
                "search_prompt": (
                    "你是一名专业中文研究员。"
                    "请结合已有上下文和最新联网搜索结果继续回答。"
                    "输出中文 Markdown。"
                )
            }
        }
    ]

    messages = st.session_state.history + [
        {"role": "user", "content": follow_up}
    ]

    with st.spinner("正在继续搜索并回答，请稍等..."):
        response = client.chat.completions.create(
            model="glm-4-air",
            messages=messages,
            tools=tools
        )

    answer = response.choices[0].message.content

    st.session_state.history.append({"role": "user", "content": follow_up})
    st.session_state.history.append({"role": "assistant", "content": answer})

    st.success("追问完成。")
    st.markdown(answer)