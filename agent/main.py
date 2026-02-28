import asyncio
from langchain_core.messages import HumanMessage, AIMessageChunk, AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START,END
from langgraph.graph import StateGraph
from agent.messages_state.messages_state import MessageState
from agent.nodes.choose import  continue_or_not
from agent.nodes.model_nodes import *
from agent.nodes.rag_node import rag_node
from agent.nodes.tools_nodes import *
from dotenv import load_dotenv



async def main():

    load_dotenv()
    checkpointer = InMemorySaver()
    agent = (
        StateGraph(MessageState)
        .add_node("rag知识库节点",rag_node)
        .add_node("模型决策节点",model_with_tools_node)
        .add_node("工具调用节点",tools_node)
        .add_edge(START,"rag知识库节点")
        .add_edge("rag知识库节点","模型决策节点")
        .add_conditional_edges(
            "模型决策节点",
            continue_or_not,
            [ "工具调用节点",END]
        )
        .add_edge("工具调用节点","模型决策节点")
        .compile(checkpointer = checkpointer)
        )
    while True:
        user = input("\nusr_input：")

        async for chunk in agent.astream({"messages":[HumanMessage(user)]}, {"configurable": {"thread_id": "1"}},stream_mode=["messages"]):
            if isinstance(chunk[-1][0],AIMessageChunk) and (chunk[-1][0].content != ("False" or "True")):
                print(chunk[-1][0].content,end="",flush=True)






if __name__ == '__main__':
    asyncio.run(main())