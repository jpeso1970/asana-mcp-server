# Asana MCP Server Development To-Do List

This document provides a step-by-step to-do list for building a locally running Model Context Protocol (MCP) server that integrates with Asana, as specified in the Product Requirements Document (PRD) located at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md`. The server will be developed on a Mac M3 with macOS compatible with Python 3.10+, using the `modelcontextprotocol` Python SDK. The project folder is `~/CascadeProjects/asana-mcp-server`, and this to-do list is located at `~/docs/asana_mcp_server_todo.md`.

**Windsurf Instructions**: Using the Cascade interface, load this to-do list (`~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_todo.md`) and the PRD (`~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md`). Execute only the “Windsurf Tasks (AI)” sections, identified by “Windsurf Prompt:”, in sequence, following vibe-coding best practices (iterative commits, minimal boilerplate, AI collaboration). Reference the PRD for project requirements (e.g., Functional Requirements, Tech Stack). Ignore “Manual Tasks (You)”, which are performed by the human user. Commit changes in Cascade after each task with the specified commit message. Ensure all files are created within `~/CascadeProjects/asana-mcp-server`.

**Manual Tasks (You)** are limited to setting up the Windsurf project and obtaining the Asana Personal Access Token (PAT). These must be completed before Windsurf begins. **Windsurf Tasks (AI)** cover all development, testing, and documentation.

## Phase 1: Project Setup

### Manual Tasks (You)
1. **Install and Set Up Windsurf Project on Mac M3**
   - Download Windsurf from its official site or Mac App Store on your Mac M3.
   - Follow the installation prompts to set up Windsurf, ensuring it supports Python 3.10+ projects.
   - In Terminal, run `mkdir -p ~/CascadeProjects/asana-mcp-server/docs` to create the project and docs directories.
   - Open Windsurf and create a new project named `asana-mcp-server` in `~/CascadeProjects/asana-mcp-server`:
     - Select “New Project,” choose `~/CascadeProjects/asana-mcp-server`, and confirm.
   - Verify Windsurf launches the project by checking the project explorer shows `~/CascadeProjects/asana-mcp-server`.
   - Save the PRD as `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` and this to-do list as `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_todo.md`.
   - Note: If Windsurf requires a license or account, set this up first.

2. **Obtain Asana Personal Access Token (PAT)**
   - Open a browser on your Mac M3 and go to https://app.asana.com/0/developer-console.
   - Log in to Asana, navigate to “My Access Tokens,” and click “Create new token.”
   - Name the token (e.g., “MCP Server”) and copy the generated PAT to a secure location (e.g., a password manager).
   - Find your workspace ID:
     - In Asana’s UI, go to a project and check the URL for the workspace ID (e.g., `https://app.asana.com/0/[WORKSPACE_ID]/...`).
     - Alternatively, note that Windsurf will test authentication later to confirm the ID.
   - Save the PAT and workspace ID securely for the next phase.

### Windsurf Tasks (AI)
3. **Initialize Python Project**
   - Windsurf Prompt: “Read the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` for project requirements. In `~/CascadeProjects/asana-mcp-server`, set up a Python 3.10+ project with a virtual environment, including dependencies `modelcontextprotocol`, `asana`, `python-dotenv`, and `pytest`, as specified in the PRD Tech Stack.”
   - Windsurf Prompt: “Create a `pyproject.toml` for dependency management and a `main.py` with a basic MCP server skeleton using `modelcontextprotocol` FastMCP.”
   - Windsurf Prompt: “Initialize a Git repository and create a `.gitignore` file excluding `__pycache__`, `.env`, `.venv`, and `*.pyc`.”
   - Review the generated files in Windsurf’s Cascade UI and commit with “Initialized Asana MCP server Python project.”

4. **Configure Environment Variables**
   - Windsurf Prompt: “Create a `.env` file in `~/CascadeProjects/asana-mcp-server` with variables `ASANA_ACCESS_TOKEN=placeholder`, `DEFAULT_WORKSPACE_ID=placeholder`, `SERVER_PORT=3000`, `CLIENT_PORT=5173`, and `READ_ONLY_MODE=false`, as per the PRD Setup Instructions.”
   - Windsurf Prompt: “Add code in `main.py` to load `.env` variables using `python-dotenv` and initialize the MCP server with these settings.”
   - Note: The human user will update `.env` with the PAT and workspace ID in Phase 2.
   - Commit with “Configured environment variables.”

## Phase 2: Core Development

### Manual Tasks (You)
5. **Update Environment Variables with PAT**
   - Open `~/CascadeProjects/asana-mcp-server/.env` in a text editor on your Mac M3 (e.g., `code ~/CascadeProjects/asana-mcp-server/.env` in Terminal).
   - Replace `ASANA_ACCESS_TOKEN=placeholder` with your PAT (e.g., `ASANA_ACCESS_TOKEN=1/123456789:abcdef`).
   - Replace `DEFAULT_WORKSPACE_ID=placeholder` with your workspace ID (e.g., `DEFAULT_WORKSPACE_ID=123456789`).
   - Save the file and verify by running `cat ~/CascadeProjects/asana-mcp-server/.env` to check the values.
   - In Windsurf’s Cascade interface, reload the project to ensure it recognizes the updated `.env`.

### Windsurf Tasks (AI)
6. **Create Basic MCP Server**
   - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (MCP Client Integration). Generate a Python MCP server in `main.py` using `modelcontextprotocol` FastMCP, running locally on port 3000 with Server-Sent Events (SSE), including a `ping` tool that returns `{ 'status': 'ok' }`.”
   - Windsurf Prompt: “Add error handling for server startup failures and invalid MCP protocol messages.”
   - Test the server in Windsurf’s Cascade preview mode. Verify the `ping` tool works by accessing `http://localhost:3000` in a Mac M3 browser.
   - Review and tweak the generated code in Cascade’s UI (e.g., adjust error messages). Commit with “Implemented basic MCP server with ping tool.”

7. **Integrate Asana SDK**
   - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Authentication). Create `asana_client.py` with an Asana client initialized using `asana` Python SDK and `ASANA_ACCESS_TOKEN` from `.env`, including a function to test authentication by fetching workspaces.”
   - Windsurf Prompt: “Add error handling for invalid Asana tokens or API failures.”
   - Test the authentication function in Cascade’s preview mode, ensuring it returns workspace data.
   - Review the generated code in Cascade and commit with “Integrated Asana SDK with authentication.”

8. **Implement Task Management Tools**
   - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Task Management). Create `tools/list_tasks.py` with a `pydantic` model (via `modelcontextprotocol`) for inputs (`workspace_id`, `project_id`, `sort_by`) and logic to list tasks using `asana.Client.tasks.find_all`, returning task name, due date, and status.”
   - Windsurf Prompt: “Create `tools/create_task.py` with a `pydantic` model for inputs (`name`, `description`, `due_date`, `project_id`) and logic to create a task using `asana.Client.tasks.create`.”
   - Windsurf Prompt: “Create `tools/update_task.py` and `tools/delete_task.py` with `pydantic` models and logic for updating and deleting tasks.”
   - Windsurf Prompt: “Register all task tools in the MCP server in `main.py` using `modelcontextprotocol` tool registration.”
   - Test each tool in Cascade’s preview mode with sample inputs. Tweak code in Cascade’s UI if needed.
   - Commit iteratively after each tool with messages like “Added list_tasks tool,” “Added create_task tool.”

9. **Implement Project Management Tools**
   - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Project Management). Create `tools/list_projects.py` to fetch projects in a workspace using `asana.Client.projects.find_all`, returning project names and IDs.”
   - Windsurf Prompt: “Create `tools/create_project.py` with a `pydantic` model for inputs (`name`, `description`) and logic to create a project using `asana.Client.projects.create`.”
   - Windsurf Prompt: “Register project tools in the MCP server using `modelcontextprotocol`.”
   - Test tools in Cascade’s preview mode and refine code in the UI.
   - Commit with “Added project management tools.”

10. **Implement Workspace Query Tool**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Workspace Queries). Create `tools/get_workspace.py` to fetch workspace details using `asana.Client.workspaces.find_all` or `find_by_id`, returning workspace name and ID.”
    - Windsurf Prompt: “Register the workspace tool in the MCP server using `modelcontextprotocol`.”
    - Test in Cascade’s preview mode and tweak code in the UI.
    - Commit with “Added workspace query tool.”

11. **Add Read-Only Mode**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Read-Only Mode). Add logic to `create_task`, `update_task`, `delete_task`, and `create_project` to check `READ_ONLY_MODE` from `.env` and raise an exception if true.”
    - Test by setting `READ_ONLY_MODE=true` in `.env` (manually, later) and attempting a write operation in Cascade’s preview mode.
    - Commit with “Implemented read-only mode.”

12. **Implement Error Handling**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Non-Functional Requirements: Performance, Security). Add retry logic for Asana API rate limits (HTTP 429) with exponential backoff in all tools using `tenacity`.”
    - Windsurf Prompt: “Ensure all tools use `pydantic` (via `modelcontextprotocol`) for input validation and return user-friendly error messages for invalid inputs, authentication failures, or API downtime.”
    - Test error handling in Cascade’s preview mode with invalid inputs or a mock 429 response.
    - Review and tweak error messages in Cascade’s UI. Commit with “Added error handling with retries.”

## Phase 3: Testing

### Manual Tasks (You)
13. **Install Claude Desktop**
    - Download Claude Desktop from Anthropic’s official site on your Mac M3.
    - Follow the installation prompts to install and sign in.
    - Verify Claude Desktop launches by opening it and checking the UI.

14. **Configure Claude Desktop**
    - Locate Claude Desktop’s configuration file, likely at `~/Library/Application Support/Claude/claude_desktop_config.json`.
    - Run `code ~/Library/Application Support/Claude/claude_desktop_config.json` in Terminal to open it in VS Code.
    - Add the following, replacing `your-asana-access-token` with your PAT:
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
    - Save the file and restart Claude Desktop.
    - Verify the configuration by running the server in Windsurf’s Cascade interface and checking if Claude Desktop connects (e.g., query “List my Asana tasks”).

15. **Test Read-Only Mode**
    - Open `~/CascadeProjects/asana-mcp-server/.env` with `code ~/CascadeProjects/asana-mcp-server/.env`.
    - Set `READ_ONLY_MODE=true` and save.
    - In Claude Desktop, attempt to create a task (e.g., “Create an Asana task called ‘Test’”). Verify an exception is raised.
    - Reset `READ_ONLY_MODE=false` and save.

### Windsurf Tasks (AI)
16. **Test with MCP Inspector**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Testing Interface). Set up MCP Inspector to run on `CLIENT_PORT` (5173) and test all tools interactively using `pytest` with `modelcontextprotocol`.”
    - Windsurf Prompt: “Generate `tests/test_tools.py` with test cases for each tool (e.g., valid/invalid inputs for `list_tasks`) and run them.”
    - Note: The human user will manually open `http://localhost:5173` in a Mac M3 browser to interact with MCP Inspector.
    - Windsurf Prompt: “Analyze test results and suggest fixes for any failures.”
    - Apply fixes in Cascade’s UI and commit with “Fixed MCP Inspector test issues.”

17. **Test with Claude Desktop**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (MCP Client Integration). Run the MCP server with `modelcontextprotocol` and simulate Claude Desktop queries (e.g., ‘List my Asana tasks’, ‘Create a task called Test due tomorrow’) using `pytest`.”
    - Windsurf Prompt: “Debug any connection or query failures, ensuring compatibility with Claude Desktop.”
    - Review test results in Cascade’s UI and apply fixes. Commit with “Completed Claude Desktop testing.”

18. **Fix Bugs**
    - Windsurf Prompt: “Analyze all test results and suggest fixes for bugs in tool outputs, error handling, or server stability.”
    - Apply fixes in Cascade’s UI and retest in MCP Inspector and Claude Desktop.
    - Commit with “Fixed bugs from testing.”

## Phase 4: Documentation and Finalization

### Manual Tasks (You)
19. **Review README**
    - Open Windsurf on your Mac M3 and view `README.md` in the `asana-mcp-server` project via Cascade.
    - Read the README and edit it in Cascade’s UI to add personal notes (e.g., your Asana workspace name).
    - Save the changes in Windsurf.

20. **Share Project**
    - In Windsurf’s Cascade interface, export the project to GitHub:
      - Go to project settings and select “Export to GitHub.”
      - On your Mac M3, visit https://github.com/new, create a repository named `asana-mcp-server`, and copy its URL.
      - In Cascade, paste the GitHub URL and follow prompts to push the project.
    - Share the GitHub URL or Windsurf project link with stakeholders via email or a messaging app.

### Windsurf Tasks (AI)
21. **Write README**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Setup Instructions, Development Tasks). Generate a `README.md` with:
      - Project overview (Python-based MCP server on Mac M3 using `modelcontextprotocol`).
      - Prerequisites (Windsurf, Python 3.10+, Asana PAT, Mac M3).
      - Setup instructions (share PRD/to-do in Windsurf, manually update `.env`, configure Claude Desktop).
      - Usage instructions (run MCP server, test with MCP Inspector/Claude Desktop).
      - Tool descriptions (`list_tasks`, `create_task`, etc.).
      - References: Asana API (https://developers.asana.com/docs), MCP Specification (https://modelcontextprotocol.io), mcp-server-asana repo (https://github.com/roychri/mcp-server-asana), MCP Python SDK (https://github.com/modelcontextprotocol/python-sdk).
      - Troubleshooting tips (e.g., invalid PAT, MCP server errors).”
    - Commit with “Added README documentation.”

22. **Optimize and Clean Up**
    - Windsurf Prompt: “Refactor all Python code for clarity, removing unused code and optimizing tool definitions with PEP 8 compliance.”
    - Windsurf Prompt: “Run `pytest` to ensure all tests pass and verify the server runs with `modelcontextprotocol` FastMCP.”
    - Review suggestions in Cascade’s UI and apply changes. Commit with “Optimized and cleaned up code.”

23. **Final Testing**
    - Windsurf Prompt: “Refer to the PRD at `~/CascadeProjects/asana-mcp-server/docs/asana_mcp_server_prd.md` (Non-Functional Requirements: Compatibility). Run end-to-end tests for all tools with Claude Desktop queries using `pytest` and verify read-only mode.”
    - Windsurf Prompt: “Test server stability by simulating several hours of operation with `modelcontextprotocol`.”
    - Windsurf Prompt: “Fix any final issues in tool functionality or stability.”
    - Commit with “Completed final testing.”

## Notes
- **Windsurf Parsing**: Windsurf should execute only “Windsurf Tasks (AI)” sections, identified by “Windsurf Prompt:”. Ignore “Manual Tasks (You)”, which are for human execution.
- **Vibe-Coding**: Windsurf tasks use natural language prompts, encourage iterative commits, and rely on Windsurf for boilerplate and optimizations. Review AI-generated code in Cascade’s UI after each prompt.
- **Manual Tasks**: Perform these outside Windsurf before or alongside Windsurf tasks as indicated.
- **Security**: Never commit `.env` to Git; Windsurf will manage it securely.
- **Environment**: Assumes a Mac M3 with macOS compatible with Windsurf and Python 3.10+.
- **Dependencies**: The Asana PAT and workspace ID must be valid before Phase 2.
- **File Locations**: PRD and to-do list must be saved in `~/CascadeProjects/asana-mcp-server/docs` before starting Windsurf tasks.