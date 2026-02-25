import operator
from typing import TypedDict, Annotated

from langchain_core.messages import AnyMessage


class MessageState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    new_time: str
