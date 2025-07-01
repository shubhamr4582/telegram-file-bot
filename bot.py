from pyrogram import Client, filters

api_id = 22263681
api_hash = "f5aeb37a71867215d6b4be6fbbf06c49"
bot_token = "7880621934:AAGCIc_5df7x0vkggcfx-bk3pMOJ1D-qAFA"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Bot is working on Heroku!")

app.run()
