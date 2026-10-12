## Environment Setup (Linux)

1. Clone the repository and navigate to the project root.

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   ```bash
   pip install -e .
   ```


4. Copy and configure the environment file:
   ```bash
   cp .env.example .env  # If example exists, otherwise create .env
   ```

5. Configure routers in `src/mcp/utils/routers.py`:
   - Update the `ROUTERS` dictionary with your actual router details (IP addresses, usernames, passwords).
   - Each router must have RESTCONF enabled to use MCP tools.
   - For ping and traceroute functionality, routers must have SSH enabled.

## Configure the routing on eth0 before attaching the ethernet cable
```bash
sudo ip link set dev eth0 up
sudo ip address replace 192.168.0.2/24 dev eth0

sudo ip route replace 172.16.0.0/24 via 192.168.0.1 dev eth0
sudo ip route replace 10.0.0.0/28 via 192.168.0.1 dev eth0
sudo ip route replace 203.0.113.1/32 via 192.168.0.1 dev eth0
```

## Running the System

use python or python3 depending on which is used

### Start the MCP Server and Agent alone

```bash
python -m mcp_app.server
```

```bash
python -m agent.agent
```

### Start MCP and Agent Together

From the project root, start both processes with:

```bash
chmod +x ./run-all.sh
./run-all.sh
```
