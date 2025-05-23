from mcp.server.fastmcp.server import FastMCP
from mcp.server.fastmcp.tools import Tool
from pydantic import BaseModel

class PingInput(BaseModel):
    pass

class PingOutput(BaseModel):
    status: str

ping_tool = Tool.from_function(
    lambda ping_input: PingOutput(status="ok"),
    name="ping",
    description="Health check tool that returns status ok."
)

fastmcp = FastMCP(
    name="asana-mcp-server",
    tools=[ping_tool]
)

app = fastmcp.streamable_http_app()

print("Available routes:")
for route in getattr(app, 'routes', []):
    print(f"Path: {getattr(route, 'path', None)} | Methods: {getattr(route, 'methods', None)} | Name: {getattr(route, 'name', None)}")
