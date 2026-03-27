# 联网研究 Agent

这是一个基于智谱 AI Web Search 的研究型 Agent 项目。

## 功能
- 输入一个研究主题
- 自动联网搜索
- 生成中文研究报告
- 支持继续追问

## 技术栈
- Python
- Streamlit
- zai-sdk
- 智谱 AI Web Search

## 启动方式

```bash
python -m venv .venv
.venv\Scripts\activate
pip install zai-sdk streamlit python-dotenv
streamlit run app.py