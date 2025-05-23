import pytest
import httpx
import os

# These values should match your server config
SERVER_URL = os.getenv("SERVER_URL", "http://localhost:3000/mcp")

@pytest.mark.asyncio
async def test_ping_tool():
    """Test the ping tool via MCP protocol."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        session_id = "test-session"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"
        }
        cookies = {"session_id": session_id}
        call_tool_payload = {
            "method": "call_tool",
            "params": {
                "name": "ping",
                "arguments": {},
                "session_id": session_id
            },
            "session_id": session_id,
            "id": 1,
            "jsonrpc": "2.0"
        }
        resp_ping = await client.post(SERVER_URL, json=call_tool_payload, headers=headers, cookies=cookies)
        print(f"Ping tool status: {resp_ping.status_code}")
        print(f"Ping tool content: {resp_ping.text}")
        assert resp_ping.status_code == 200
        data = resp_ping.json()
        assert "result" in data
        assert data["result"][0]["status"] == "ok"
