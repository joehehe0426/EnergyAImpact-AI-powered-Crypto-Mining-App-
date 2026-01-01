"""
StakeWise AI Configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (set these in .env file)
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID", "")
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY", "")

# Blockchain RPC Endpoints
RPC_ENDPOINTS = {
    "ethereum": f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}" if INFURA_PROJECT_ID else "https://eth.llamarpc.com",
    "polygon": "https://polygon-rpc.com",
    "arbitrum": "https://arb1.arbitrum.io/rpc",
    "optimism": "https://mainnet.optimism.io",
    "bsc": "https://bsc-dataseed.binance.org",
}

# Staking Protocol Addresses (Mainnet)
STAKING_CONTRACTS = {
    "lido": {
        "steth": "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84",
        "wsteth": "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0",
    },
    "rocketpool": {
        "reth": "0xae78736Cd615f374D3085123A210448E74Fc6393",
        "storage": "0x1d8f8f00cfa6758d7bE78336684788Fb0ee0Fa46",
    },
    "stakewise": {
        "swise": "0x48C3399719B582dD63eB5AADf12A40B4C3f52FA2",
    },
}

# Staking APIs (no auth required)
STAKING_APIS = {
    "lido": "https://eth-api.lido.fi",
    "rocketpool": "https://api.rocketpool.net",
    "defi_llama": "https://yields.llama.fi",
    "coingecko": "https://api.coingecko.com/api/v3",
    "staking_rewards": "https://api.stakingrewards.com/public/query",
}

# Supported staking assets
SUPPORTED_ASSETS = {
    "ETH": {
        "name": "Ethereum",
        "symbol": "ETH",
        "chain": "ethereum",
        "decimals": 18,
        "staking_options": ["lido", "rocketpool", "native"],
    },
    "MATIC": {
        "name": "Polygon",
        "symbol": "MATIC",
        "chain": "polygon",
        "decimals": 18,
        "staking_options": ["native", "lido"],
    },
    "SOL": {
        "name": "Solana",
        "symbol": "SOL",
        "chain": "solana",
        "decimals": 9,
        "staking_options": ["marinade", "native"],
    },
    "ADA": {
        "name": "Cardano",
        "symbol": "ADA",
        "chain": "cardano",
        "decimals": 6,
        "staking_options": ["native"],
    },
    "ATOM": {
        "name": "Cosmos",
        "symbol": "ATOM",
        "chain": "cosmos",
        "decimals": 6,
        "staking_options": ["native"],
    },
}

# AI Optimization Settings
AI_CONFIG = {
    "risk_weights": {
        "protocol_risk": 0.3,
        "smart_contract_risk": 0.25,
        "slashing_risk": 0.2,
        "liquidity_risk": 0.15,
        "volatility_risk": 0.1,
    },
    "optimization_interval": 3600,  # seconds
    "min_apy_threshold": 2.0,  # minimum APY to consider
    "max_risk_score": 7.0,  # max risk score (1-10)
}

# Flask Settings
FLASK_CONFIG = {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": os.getenv("FLASK_DEBUG", "false").lower() == "true",
}
