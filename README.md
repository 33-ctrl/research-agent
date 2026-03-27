# 联网研究 Agent

## 项目简介
这是一个基于智谱 AI Web Search 和 Streamlit 开发的研究型智能体应用。
用户输入研究主题后，系统会自动联网搜索并生成结构化中文研究报告。

## 功能
- 输入研究主题
- 自动联网搜索
- 输出研究报告
- 支持继续追问

## 技术栈
- Python
- Streamlit
- zai-sdk
- python-dotenv

## 安装方式
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py