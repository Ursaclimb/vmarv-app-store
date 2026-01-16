import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

RPC_USER = os.getenv("RPC_USER", "gossimerlite")
RPC_PASSWORD = os.getenv("RPC_PASSWORD", "red2305")
RPC_IP = os.getenv("RPC_IP", "127.0.0.1")
RPC_PORT = os.getenv("RPC_PORT", "9332")
RPC_URL = f"http://{RPC_IP}:{RPC_PORT}"

def rpc_request(method, params=[]):
    headers = {'content-type': 'application/json'}
    payload = json.dumps({"method": method, "params": params, "id": 1})
    try:
        response = requests.post(RPC_URL, auth=(RPC_USER, RPC_PASSWORD), data=payload, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.route("/getconnectioncount")
def getconnectioncount():
    result = rpc_request("getconnectioncount")
    return jsonify(result.get("result", 0))

@app.route("/getnetworkhashps")
def network_hashrate():
    result = rpc_request("getnetworkhashps")
    network_hashrate_ths = round(result.get("result", 0) / 1e12, 1)
    return jsonify(network_hashrate_ths)

@app.route("/getblockchaininfo")
def blockchain_info():
    result = rpc_request("getblockchaininfo")
    blockchain_info = result.get("result", {})
    chain_size_gb = round(blockchain_info.get("size_on_disk", 0) / 1e9, 1)
    return jsonify(chain_size_gb)

@app.route("/getmempoolinfo")
def mempool_info():
    result = rpc_request("getmempoolinfo")
    mempool_info = result.get("result", {})
    mempool_size_kb = round(mempool_info.get("bytes", 0) / 1e3, 1)
    return jsonify(mempool_size_kb)

@app.route("/getblockheight")
def block_height():
    result = rpc_request("getblockchaininfo")
    blockchain_info = result.get("result", {})
    block_height = blockchain_info.get("blocks", 0)
    return jsonify(block_height)

@app.route("/getsyncprogress")
def sync_progress():
    result = rpc_request("getblockchaininfo")
    blockchain_info = result.get("result", {})
    verification_progress = round(blockchain_info.get("verificationprogress", 0) * 100, 1)
    return jsonify(verification_progress)

@app.route("/getblocktransactions/<int:block_number>")
def block_transactions(block_number):
    block_hash_result = rpc_request("getblockhash", [block_number])
    if "error" in block_hash_result or "result" not in block_hash_result:
        return jsonify(0)
    
    block_hash = block_hash_result["result"]
    block_result = rpc_request("getblock", [block_hash, 2])
    if "error" in block_result or "result" not in block_result:
        return jsonify(0)
    
    block_info = block_result["result"]
    transaction_count = len(block_info.get("tx", []))
    return jsonify(transaction_count)

@app.route("/health")
def health():
    result = rpc_request("getblockchaininfo")
    if "result" in result:
        return jsonify({"status": "healthy"})
    return jsonify({"status": "unhealthy"}), 503

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
