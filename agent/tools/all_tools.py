
from agent.tools.base_tools import base_tools
from agent.tools.mcp_tools import get_mcp_tools

async def get_all_tools():
    all_tools = base_tools +await get_mcp_tools()
    return all_tools

