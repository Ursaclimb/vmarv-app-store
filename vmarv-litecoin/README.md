# Litecoin Node for Umbrel

This is a custom Umbrel app for running a Litecoin full node.

## Installation

1. Copy this directory to your Umbrel server:
   ```bash
   scp -r umbrel-litecoin-app umbrel@192.168.86.33:~/umbrel/app-data/
   ```

2. Rename it to follow Umbrel's naming convention:
   ```bash
   ssh umbrel@192.168.86.33
   cd ~/umbrel/app-data
   mv umbrel-litecoin-app litecoin
   ```

3. Restart Umbrel or refresh the app store to see the app

## Configuration

- RPC User: `gossimerlite`
- RPC Password: `red2305`
- P2P Port: `9333`
- RPC Port: `9332`
- API Port: `5000`

## Features

- Full Litecoin node validation
- REST API for blockchain queries
- Dashboard support (when added to Umbrel UI)

## Storage

The blockchain data is stored in a Docker volume. Initial sync may take several hours.
