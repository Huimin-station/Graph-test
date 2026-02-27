import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from utils.key import dashscope_api_key
async def get_mcp_tools():

    client = MultiServerMCPClient(
            {
                "mcpServers": {
                "transport": "sse",
                "url": "https://dashscope.aliyuncs.com/api/v1/mcps/amap-maps/sse",
                "headers": {
                  "Authorization": f"Bearer {dashscope_api_key}"
             }
            },
            }
        )

    tools = await client.get_tools()
    return  tools

