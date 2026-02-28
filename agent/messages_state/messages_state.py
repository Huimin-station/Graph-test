from typing import TypedDict, Annotated

from langchain_core.messages import AnyMessage, AIMessage
from langgraph.graph import add_messages


class MessageState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    knowledge: list[AIMessage]