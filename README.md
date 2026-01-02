# Stellar Wallet Collector Telegram Bot

This Telegram bot collects Stellar wallet addresses and sends instructions
on how to claim ORBX tokens via claimable balances.

## Features
- Validates Stellar wallet addresses
- Stores wallets safely
- Sends clear claim instructions
- Ready for GitHub + Render deployment

## Local Setup

1. Clone repository
2. Create `.env` file:
BOT_TOKEN=8063022001:AAFNsOgRvbrjI-UK1BGF62oVdZTLEMuMBXk
ASSET_ISSUER=GDYTQGDGHRXOIWANOUB4DY6BTKMMWTF5PVJC2KZVT6VFP5TYD7W63XO7 


3. Install dependencies
pip install -r requirements.txt


4. Run bot
python bot.py


## Render Deployment

- New Web Service
- Start Command: `python bot.py`
- Add Environment Variables:
  - BOT_TOKEN
  - ASSET_ISSUER
