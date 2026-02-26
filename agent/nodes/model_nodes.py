from langchain_core.messages import SystemMessage
from agent.model.model_list import *
from agent.prompt.model_system_prompt import *


# 大模型分析节点
def model_start_node(state:dict):
    return {
        "messages":[
            model_start.invoke([SystemMessage(content=model_start_prompt)]+ state["messages"])
        ]
    }
# 并行工具获取节点
def model_with_tools_node(state:dict):
    return {
        "messages":[
            model_with_tools.invoke([SystemMessage(content=model_with_tools_prompt)]+state["messages"])
        ]
    }

# 大模型信息整合节点
def model_messages_get_node(state:dict):
    return {
        "messages":[
            model_messages_get.invoke([SystemMessage(content=model_messages_get_prompt)]+ state["messages"])
        ]
    }

