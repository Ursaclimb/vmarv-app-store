# Litecoin Node for Umbrel

This is a custom Umbrel app for running a Litecoin full node.

## Installation

1. Add the app store to your Umbrel:
   - App Store → ... → Community App Stores
   - Add: `https://github.com/Ursaclimb/vmarv-app-store`

2. Install the "Litecoin Node" app

3. **IMPORTANT - Change Default Credentials:**
   After installation, you MUST change the RPC credentials for security:
   ```bash
   ssh umbrel@<your-umbrel-ip>
   cd ~/umbrel/app-data/vmarv-litecoin
   # Edit docker-compose.yml and replace:
   # LITECOIN_RPC_USER: litecoinrpc -> your-username
   # LITECOIN_RPC_PASSWORD: changeme -> your-secure-password
   
   # Then restart the app
   docker compose restart
   ```

## Configuration

Default RPC Port: `9332`
Default P2P Port: `9333`
GUI Port: `80`
API Port: `5000`

## Features

- Full Litecoin node validation
- Real-time dashboard with sync progress and peer info
- REST API for blockchain queries
- Support for merged mining

## Storage

The blockchain data is stored in `~/.litecoin`. Initial sync may take several hours.

## Security Notes

- Always change the default RPC credentials before exposing to a network
- Keep your RPC port only accessible locally if possible
- Consider using a firewall to restrict access to mining ports

