import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.tools import Tool
from pydantic import BaseModel

# Load environment variables
load_dotenv()
PORT = int(os.environ.get("SERVER_PORT", 3000))

# --- Ping Tool Schema ---
class PingInput(BaseModel):
    pass

class PingOutput(BaseModel):
    status: str

def ping(ping_input: PingInput) -> PingOutput:
    return PingOutput(status="ok")

ping_tool = Tool.from_function(
    ping,
    name="ping",
    description="Health check tool that returns status ok."
)

fastmcp = FastMCP(
    name="asana-mcp-server",
    tools=[ping_tool]
)

if __name__ == "__main__":
    import uvicorn
    print(f"Starting MCP server on port {PORT}...")
    uvicorn.run(fastmcp.streamable_http_app(), host="0.0.0.0", port=PORT)
