from typing import Literal


# 根据记忆判断是否需要再次搜索
def search_or_not(state)->Literal["消息整合大模型节点","模型决策节点"]:
    if state["messages"][-1].content=="False":
        return "模型决策节点"
    return "消息整合大模型节点"

def continue_or_not(state) -> Literal["工具调用节点", "消息整合大模型节点"]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "工具调用节点"
    # Otherwise, we stop (reply to the user)
    return "消息整合大模型节点"

