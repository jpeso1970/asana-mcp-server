# Product Requirements Document: Locally Running Asana MCP Server

## 1. Overview

This document outlines the requirements for developing a Model Context Protocol (MCP) server that runs locally on a Mac M3, enabling MCP agent applications, such as Anthropic’s Claude Desktop, to interact with an Asana account. The server will act as a standardized interface, allowing AI agents to perform operations like listing tasks, creating projects, and managing workspaces in Asana via natural language queries.

### Purpose
The Asana MCP Server aims to bridge AI agents with Asana’s API, enabling seamless task and project management within a user’s Asana workspace. By running locally on a Mac M3 using Python and the `modelcontextprotocol` SDK, it ensures simplicity, security, and compatibility for individual users or developers testing AI-driven workflows on macOS.

### Scope
- Develop a Python-based MCP server using the `modelcontextprotocol` SDK, optimized to run locally on a Mac M3.
- Support core Asana operations: task management (list, create, update, delete), project management (list, create), and workspace queries.
- Integrate with desktop MCP clients like Claude Desktop, accessible from the local Mac M3 environment.
- Provide setup and testing instructions for developers using a Mac M3 with Windsurf.

## 2. Goals and Objectives

### Goals
- Enable AI agents to interact with Asana’s API via an MCP server running locally on a Mac M3 using Python.
- Provide a secure, locally running server for individual use on macOS.
- Simplify setup and configuration for developers on a Mac M3 using Windsurf.

### Objectives
- Implement at least five Asana-related tools (e.g., `list_tasks`, `create_task`, `update_task`, `list_projects`, `get_workspace`) using the `modelcontextprotocol` SDK.
- Achieve compatibility with Claude Desktop and other MCP clients supporting SSE on a Mac M3.
- Ensure robust error handling for authentication and API issues.
- Deliver documentation for setup, configuration, and usage tailored for a Mac M3 environment.

## 3. Functional Requirements

### Features
1. **Authentication**:
   - Authenticate with Asana using a Personal Access Token (PAT).
   - Support configuration via environment variables (`ASANA_ACCESS_TOKEN`, `DEFAULT_WORKSPACE_ID`) on a Mac M3.
2. **Task Management**:
   - List tasks in a workspace or project, with optional filters (e.g., `sort_by`, `completed`).
   - Create new tasks with details (name, description, due date, assignee, project).
   - Update existing tasks (e.g., change status, custom fields).
   - Delete tasks.
3. **Project Management**:
   - List projects in a workspace.
   - Create new projects with basic details (name, description).
4. **Workspace Queries**:
   - Retrieve details of the user’s workspace(s).
5. **Read-Only Mode**:
   - Support a `READ_ONLY_MODE` environment variable to disable write operations for testing.
6. **MCP Client Integration**:
   - Expose tools via MCP protocol using `modelcontextprotocol` SDK, compatible with Claude Desktop running locally on a Mac M3.
   - Support Server-Sent Events (SSE) for client-server communication within the local environment.
7. **Testing Interface**:
   - Provide compatibility with MCP Inspector for interactive tool testing on a Mac M3.

### User Stories
- As a developer, I want to configure the MCP server with my Asana PAT on my Mac M3 so I can securely access my workspace.
- As a user, I want to ask Claude Desktop on my Mac M3 to “list my Asana tasks” and see a summary of tasks in my workspace.
- As a user, I want to create a new task in Asana via natural language (e.g., “Create an Asana task called ‘Plan sprint’ due tomorrow”) using my Mac M3.
- As a developer, I want to test the server in read-only mode on my Mac M3 to ensure no accidental changes to my Asana data.
- As a user, I want clear error messages if authentication fails or the Asana API is unavailable when using the server on my Mac M3.

## 4. Technical Requirements

### Tech Stack
- **Language**: Python 3.10+, compatible with macOS on a Mac M3.
- **Dependencies**:
  - `modelcontextprotocol`: Python SDK for MCP server implementation with FastMCP.
  - `asana`: Python SDK for Asana API interactions.
  - `pydantic`: For input validation (included with `modelcontextprotocol`).
  - `python-dotenv`: For environment variable management on macOS.
  - `pytest`: For unit testing.
- **Transport**: Server-Sent Events (SSE) for local MCP communication on a Mac M3, managed by `modelcontextprotocol`.
- **Configuration File**: `.env` for storing `ASANA_ACCESS_TOKEN`, `DEFAULT_WORKSPACE_ID`, and port settings, managed on a Mac M3.
- **Testing Tool**: MCP Inspector (runs on `http://localhost:5173` by default) accessible via a Mac M3 browser.

### Setup Instructions
1. Clone the repository to your Mac M3 in `~/CascadeProjects/asana-mcp-server`.
2. Open Windsurf and load the project from `~/CascadeProjects/asana-mcp-server`.
3. Create a `.env` file with:
   ```
   ASANA_ACCESS_TOKEN=your-asana-access-token
   DEFAULT_WORKSPACE_ID=your-workspace-id
   SERVER_PORT=3000
   CLIENT_PORT=5173
   READ_ONLY_MODE=false
   ```
4. In Windsurf’s Cascade interface, run the server using the `modelcontextprotocol` FastMCP application.
5. Use MCP Inspector (`http://localhost:5173`) on your Mac M3 to test tools.
6. Configure Claude Desktop on your Mac M3 by adding the server to `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "asana": {
         "command": "python",
         "args": ["main.py"],
         "env": { "ASANA_ACCESS_TOKEN": "your-asana-access-token" }
       }
     }
   }
   ```

### Development Tasks
- Initialize Python project with `modelcontextprotocol` SDK on a Mac M3.
- Implement MCP server with Asana tools using `asana` and `modelcontextprotocol` SDKs.
- Define tool schemas with `pydantic` for input validation.
- Integrate Asana SDK for API calls.
- Add error handling for authentication, rate limits, and invalid inputs.
- Test with MCP Inspector and Claude Desktop on a Mac M3.
- Write README with setup and usage instructions for Mac M3 users.

## 5. Non-Functional Requirements

### Security
- Store Asana PAT in environment variables on the Mac M3, not in source code.
- Validate all inputs to prevent injection attacks using `pydantic`.
- Support read-only mode to prevent unintended data changes.

### Performance
- Handle Asana API rate limits (e.g., retry on 429 errors).
- Ensure server response time < 2 seconds for typical requests on a Mac M3.

### Scalability
- Designed for single-user, local use on a Mac M3; no multi-user or remote support required.

### Compatibility
- Compatible with MCP clients supporting SSE (e.g., Claude Desktop) on a Mac M3.
- Tested with Asana API v1, `modelcontextprotocol` SDK, and Python 3.10+ on macOS.

## 6. Assumptions and Constraints

### Assumptions
- Users have an Asana account and can generate a PAT via the Asana developer console.
- Users have a Mac M3 running a macOS version compatible with Python 3.10+.
- Claude Desktop is the primary MCP client, running locally on the Mac M3, though other SSE-compatible clients may work.
- The MCP server runs locally on the Mac M3, with no requirement for remote hosting.
- Windsurf manages the Python environment and dependencies, including `modelcontextprotocol`.

### Constraints
- Runs locally on a Mac M3 only; remote hosting (e.g., Cloudflare) is out of scope.
- Limited to Asana API capabilities (e.g., no real-time updates without webhooks).
- No support for complex Asana features (e.g., task dependencies, advanced reporting) in initial release.

## 7. References
- **Asana API Documentation**: Official documentation for Asana’s REST API, covering authentication, tasks, projects, and more.  
  URL: [https://developers.asana.com/docs](https://developers.asana.com/docs)
- **MCP Specification**: The Model Context Protocol specification, detailing the protocol for AI agent integrations.  
  URL: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **mcp-server-asana GitHub Repository**: Example implementation of an Asana MCP server (Node.js-based, for reference).  
  URL: [https://github.com/roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana)
- **MCP Python SDK**: Official Python SDK for MCP servers, including FastMCP setup and usage details.  
  URL: [https://github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)