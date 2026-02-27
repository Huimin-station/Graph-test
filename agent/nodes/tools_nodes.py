
from langgraph.prebuilt import ToolNode

from agent.tools.all_tools import get_all_tools


# 空节点
# def blank_node(state:dict):
#     return {}


# 获取当前时间节点
# def current_time_node(state:dict):
#     return {
#         "messages":[AIMessage(f"{datetime.datetime.now()}")]
#     }

# 工具天气查询节点
async def tools_node(state:dict):
    tools_node = ToolNode(await get_all_tools())
    return tools_node

