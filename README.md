# Blockchain-DDoS-Threat_Prevention
Blockchain-Based Collaborative Threat Prevention for DDoS Attackes
# Blockchain-DDoS-Threat_Prevention

Blockchain-Based Collaborative Threat Prevention for DDoS Attacks

## Project Description
This project implements a blockchain-based collaborative threat prevention framework for Distributed Denial of Service (DDoS) attacks. The system combines blockchain technology, smart contracts, and automated detection mechanisms to improve trust, transparency, and response speed in cybersecurity operations.

## Components

### Smart Contract
- DDoSDecisionLog.sol
- Stores suspicious IP addresses, request counts, and final decisions on the blockchain.

### Detection Script
- ddos_detector.py
- Detects abnormal network traffic using Scapy.
- Connects to the blockchain through Web3.py and Ganache.
- Records detected DDoS attacks in the smart contract.

## Technologies Used
- Solidity
- Remix IDE
- Ganache
- Python
- Web3.py
- Scapy
- Ubuntu Server
- VMware Workstation
