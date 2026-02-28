import asyncio

from langchain_core.messages import HumanMessage, AIMessageChunk, AIMessage
from langgraph.constants import START,END
from langgraph.graph import StateGraph
from agent.messages_state.messages_state import MessageState
from agent.nodes.choose import search_or_not, continue_or_not
from agent.nodes.model_nodes import *
from agent.nodes.tools_nodes import *
from utils.png_print import get_png
from dotenv import load_dotenv




async def main():
    load_dotenv()
    agent = (
        StateGraph(MessageState)
        # .add_node("获取实时时间节点",current_time_node)
        .add_node("模型检查节点",model_start_node)
        .add_node("模型决策节点",model_with_tools_node)
        .add_node("工具调用节点",tools_node)
        .add_node("消息整合大模型节点",model_messages_get_node)
        # .add_edge(START,"获取实时时间节点")
        .add_edge(START,"模型检查节点")
        # .add_edge("获取实时时间节点","模型检查节点")
        .add_conditional_edges(
            "模型检查节点",
            search_or_not,
            ["模型决策节点","消息整合大模型节点"]
        )
        .add_conditional_edges(
            "模型决策节点",
            continue_or_not,
            [ "工具调用节点","消息整合大模型节点"]
        )
        .add_edge("工具调用节点","模型决策节点")
        .add_edge("消息整合大模型节点",END)
        .compile()
        )
    history = []

    while True:
        user = input("\n用户：")
        user_content = user.strip()
        ai_content = ""

        async for chunk in agent.astream({"messages":history + [HumanMessage(user)]},stream_mode=["messages"]):
            ai_content += chunk[-1][0].content


            if isinstance(chunk[-1][0],AIMessageChunk) and (chunk[-1][0].content != ("False" or "True")):
                print(chunk[-1][0].content,end="",flush=True)
        print("\nUSR:",user)
        print("\nAI:",ai_content)
        history.append(HumanMessage(user))
        history.append(AIMessage(ai_content))





if __name__ == '__main__':
    asyncio.run(main())