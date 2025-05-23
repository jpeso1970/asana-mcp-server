import os
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.tools import Tool
from pydantic import BaseModel

class PingInput(BaseModel):
    pass

class PingOutput(BaseModel):
    status: str

def ping(ping_input: PingInput) -> PingOutput:
    return PingOutput(status="ok")

ping_tool = Tool.from_function(
    ping,
    name="ping",
    description="Health check tool"
)

fastmcp = FastMCP(
    name="asana-mcp-server",
    tools=[ping_tool]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastmcp.streamable_http_app(), host="0.0.0.0", port=3000)
