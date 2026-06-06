from scapy.all import sniff
from collections import defaultdict
from web3 import Web3
import time

ganache_url = "http://192.168.17.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = "0xdb934580fcE35a11B58C6D73aDeE468a2833fa8"

abi = [
    {
        "inputs": [
            {"internalType": "string", "name": "_ip", "type": "string"},
            {"internalType": "uint256", "name": "_requestCount", "type": "uint256"},
            {"internalType": "string", "name": "_finalDecision", "type": "string"}
        ],
        "name": "addDecision",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=abi)

ip_counter = defaultdict(int)
blocked_ips = set()

THRESHOLD = 5

def detect(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        ip_counter[src_ip] += 1

        print(f"{src_ip} -> {ip_counter[src_ip]} packets")

        if ip_counter[src_ip] > 1000:
            print("===================================")
            print(f"[ALERT] DDoS Attack Detected from {src_ip}")
            print("===================================")

            account = web3.eth.accounts[0]

            tx_hash = contract.functions.addDecision(
