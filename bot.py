import re
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

# ---------------- CONFIG ----------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
ASSET_CODE = "ORBX"  # change if needed
ASSET_ISSUER = os.getenv("ASSET_ISSUER")
WALLETS_FILE = "wallets.txt"
# ---------------------------------------

STELLAR_REGEX = r"G[A-Z2-7]{55}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    match = re.search(STELLAR_REGEX, text)
    if not match:
        await update.message.reply_text(
            "❌ Invalid address.\n\n"
            "Please send a valid Stellar wallet address starting with **G**."
        )
        return

    wallet = match.group(0)

    # Save wallet if new
    if not os.path.exists(WALLETS_FILE):
        open(WALLETS_FILE, "w").close()

    with open(WALLETS_FILE, "r") as f:
        wallets = f.read().splitlines()

    if wallet not in wallets:
        with open(WALLETS_FILE, "a") as f:
            f.write(wallet + "\n")

    # Reply with claim instructions
    await update.message.reply_text(
        f"✅ **Wallet received successfully!**\n\n"
        f"### How to claim your {ASSET_CODE} tokens:\n"
        f"1️⃣ Open **Freighter**, **Lobstr**, or **Scopuly** wallet\n"
        f"2️⃣ Add this asset (trustline):\n"
        f"`{ASSET_CODE}:{ASSET_ISSUER}`\n"
        f"3️⃣ Wait for the airdrop distribution\n"
        f"4️⃣ Go to **Claimable Balances** and claim your tokens\n\n"
        f"🚀 Welcome to the ORBX ecosystem!"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Stellar Wallet Collector Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
