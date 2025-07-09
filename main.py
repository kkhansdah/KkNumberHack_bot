from telegram.ext import Updater, CommandHandler
from logic import predict_from_input

BOT_TOKEN = "7600921671:AAG3uuoKDA-KWUtVCHwhzkK7K8WCcSfqN9s"

def predict(update, context):
    try:
        numbers = list(map(int, context.args))
        if len(numbers) != 10 or not all(0 <= n <= 9 for n in numbers):
            raise ValueError
        num1, num2, logic_used = predict_from_input(numbers)
        message = f"""
🎯 𝙉𝙚𝙭𝙩 𝙋𝙧𝙚𝙙𝙞𝙘𝙩𝙚𝙙 𝙉𝙪𝙢𝙗𝙚𝙧𝙨:

🔵 Level 1: {num1}  
🟢 Level 2: {num2}

🧠 Based on: {logic_used}  
📍 Stay Alert • Play Smart • Win Big
"""
        update.message.reply_text(message)
    except:
        update.message.reply_text("⚠️ Please send exactly 10 numbers like this:\n/predict 5 3 6 2 8 0 1 6 2 5")

def start(update, context):
    update.message.reply_text("👋 Welcome to Manual Pattern Prediction Bot!\nSend 10 numbers using /predict")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("predict", predict))

print("🤖 Bot is running...")
updater.start_polling()
updater.idle()
