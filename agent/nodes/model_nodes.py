from langchain_core.messages import SystemMessage
from agent.model.model_list import *
from agent.prompt.model_system_prompt import *


# # 大模型分析节点
# async def model_start_node(state:dict):
#     model_list_get = await model_list()
#     return {
#         "messages":[
#              model_list_get[0].invoke([SystemMessage(content=model_start_prompt)]+ state["messages"])
#         ]
#     }
# 并行工具获取节点
async def model_with_tools_node(state:dict):
    model_list_get = await model_list()
    print(state)
    return {
        "messages":[
            model_list_get[1].invoke([SystemMessage(content=model_with_tools_prompt+state["knowledge"])]+state["messages"])
        ]
    }

# # 大模型信息整合节点
# async def model_messages_get_node(state:dict):
#     model_list_get = await model_list()
#     return {
#         "messages":[
#             model_list_get[2].invoke([SystemMessage(content=model_messages_get_prompt)]+ state["messages"])
#         ]
#     }

