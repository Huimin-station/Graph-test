
import datetime
import time

from langchain_core.messages import ToolMessage, HumanMessage, AIMessage

from agent.tools.base_tools import search_local_position, search_weather


# 空节点
def blank_node(state:dict):
    return state


# 获取当前时间节点
def current_time_node(state:dict):
    return {
        "messages":[AIMessage(f"{datetime.datetime.now()}")]
    }

# 工具天气查询节点
def tool_weather_node(state:dict):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = search_weather
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"],name=tool_call["name"] ))
    return {"messages": result}

# 工具位置查询节点
def tool_local_node(state:dict):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = search_local_position
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"],name=tool_call["name"] ))
    return {"messages": result}

