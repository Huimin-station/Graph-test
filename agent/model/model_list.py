from utils.model_builder import ModelBuilder
from agent.tools.base_tools import *

# 记忆读取判断模型(读取历史记忆，判断是否要重新获取位置)
model_start = ModelBuilder("deepseek-chat").get_model
# 当前位置获取模型
model_with_tools = ModelBuilder("deepseek-chat").get_model
model_with_tools = model_with_tools.bind_tools(tools)

# 信息整合模型
model_messages_get = ModelBuilder("deepseek-chat").get_model

