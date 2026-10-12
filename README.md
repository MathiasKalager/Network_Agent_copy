## Environment Setup (Linux)

1. Clone the repository and navigate to the project root.

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Copy and configure the environment file:
   ```bash
   cp .env.example .env  # If example exists, otherwise create .env
   # Edit .env to add your OpenAI API key and other required variables
   ```

5. Configure routers in `src/mcp_app/utils/routers.py`:
   - Update the `ROUTERS` dictionary with your actual router details (IP addresses, usernames, passwords).
   - Each router must have RESTCONF enabled to use MCP tools.
   - For ping and traceroute functionality, routers must have SSH enabled.

## Running the System

use python or python3 depending on which is used

### Start the MCP Server

The MCP server provides tools for network operations and should load before the agent:

```bash
python -m mcp_app.server
```

### Run the Agent

The agent executes the monitoring, diagnosis, remediation, and verification workflow:

```bash
python -m agent.agent
```
