from langchain_deepseek import ChatDeepSeek
from utils.key import deepseek


class ModelBuilder:
    def __init__(self,model_name:str,stream:bool=True):
        self.get_model = ChatDeepSeek(
            model=model_name,
            api_key=deepseek,
            streaming=stream
        )
    def build(self):
        return self.get_model


