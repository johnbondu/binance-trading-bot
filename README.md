# Binance Futures Testnet Trading Bot

## Project Overview

This project is a Python CLI Trading Bot that connects to Binance Futures Testnet and places MARKET and LIMIT orders.

The bot supports:
- BUY and SELL orders
- MARKET and LIMIT order types
- CLI-based user input
- Logging
- Input validation
- Exception handling

---

## Technologies Used

- Python 3
- python-binance
- argparse
- logging
- python-dotenv

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env
├── cli.py
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1. Clone Repository

git clone <repo-link>

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Virtual Environment

Windows:

venv\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Add API Keys

Create .env file:

API_KEY=your_api_key
API_SECRET=your_secret_key

---

## Example Commands

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000

---

## Features

- MARKET order support
- LIMIT order support
- BUY and SELL functionality
- Input validation
- Logging
- Error handling
- Binance Futures Testnet integration

---

## Logging

Logs are stored in:

logs/trading.log