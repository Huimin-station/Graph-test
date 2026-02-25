from langchain_core.tools import tool


@tool
def search_weather(city:str)->str:
    """查询目的地的天气"""
    return "多云"

@tool
def search_local_position(city:str)->str:
    """当需要了解用户当前所在位置时调用"""
    return "青岛"