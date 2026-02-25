from langchain_core.messages import HumanMessage, AIMessageChunk
from langgraph.constants import START,END
from langgraph.graph import StateGraph
from agent.messages_state.messages_state import MessageState
from agent.nodes.choose import search_or_not, weather_continue, local_continue
from agent.nodes.model_nodes import *
from agent.nodes.tools_nodes import *
from agent.nodes.tools_nodes import tool_weather_node, tool_local_node, blank_node
from utils.png_print import get_png
from dotenv import load_dotenv
load_dotenv()



agent = (
    StateGraph(MessageState)
    .add_node("获取实时时间节点",current_time_node)
    .add_node("模型检查节点",model_start_node)
    .add_node("天气工具决策节点",model_weather_node)
    .add_node("天气工具调用节点",tool_weather_node)
    # .add_node("当前位置决策节点",model_local_node)
    # .add_node("位置工具调用节点",tool_local_node)
    .add_node("转接空节点",blank_node)
    .add_node("消息整合大模型节点",model_messages_get_node)
    .add_edge(START,"获取实时时间节点")
    .add_edge("获取实时时间节点","模型检查节点")
    .add_conditional_edges(
        "模型检查节点",
        search_or_not,
        ["转接空节点","消息整合大模型节点"]
    )
    .add_edge("转接空节点","天气工具决策节点")
    .add_conditional_edges(
        "天气工具决策节点",
        weather_continue,
        [ "天气工具调用节点","消息整合大模型节点"]
    )
    .add_edge("天气工具调用节点","天气工具决策节点")
    # .add_edge("转接空节点","当前位置决策节点")
    # .add_conditional_edges(
    #     "当前位置决策节点",
    #     local_continue,
    #     [ "位置工具调用节点","消息整合大模型节点"]
    # )
    # .add_edge("位置工具调用节点","当前位置决策节点")
    .add_edge("消息整合大模型节点",END)
    .compile()
    )




# get_png(agent)


for chunk in agent.stream({"messages": [HumanMessage("上海今天天气怎样？")]},stream_mode=["messages"]):
    if isinstance(chunk[-1][0],AIMessageChunk) and (chunk[-1][0].content != ("False" or "True")):
        print(chunk[-1][0].content,end="",flush=True)
