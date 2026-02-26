
import datetime
import time

from langchain_core.messages import ToolMessage, HumanMessage, AIMessage
from langgraph.prebuilt import ToolNode

from agent.tools.base_tools import search_local_position, search_weather, tools


# 空节点
# def blank_node(state:dict):
#     return {}


# 获取当前时间节点
# def current_time_node(state:dict):
#     return {
#         "messages":[AIMessage(f"{datetime.datetime.now()}")]
#     }

# 工具天气查询节点
tools_node = ToolNode(tools)

