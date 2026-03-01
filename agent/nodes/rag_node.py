from langchain_core.messages import HumanMessage, AIMessage

from agent.rag.rag import Rag

rag = Rag()
rag.add_knowledge()
def rag_node(state:dict):
    knowledge = rag.search_knowledge(state["messages"][-1].content)
    knowledge_list = ""
    for i in knowledge:
        knowledge_list += i.page_content
    return {"knowledge": knowledge_list}

