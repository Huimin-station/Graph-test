import datetime
import time

from langchain_core.tools import tool


@tool
def search_weather(city:str)->str:
    """查询目的地当前的天气"""
    time.sleep(2)
    return "多云"

@tool
def search_local_position(city:str)->str:
    """当需要了解用户当前所在位置时调用"""
    time.sleep(1)
    return "青岛"

@tool
def search_time()->str:
    """当问题需要准确的时间时候调用"""
    return str(datetime.datetime.now())

tools = [search_weather,search_local_position,search_time]