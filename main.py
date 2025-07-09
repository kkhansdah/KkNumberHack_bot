from telegram.ext import Updater, CommandHandler
from logic import predict_numbers
import os

TOKEN = "7600921671:AAG3uuoKDA-KWUtVCHwhzkK7K8WCcSfqN9s"

def start(update, context):
    update.message.reply_text("👋 नमस्ते! मुझे 10 नंबर भेजो:\nउदाहरण: /predict 5 4 3 2 1 6 8 7 2 3")

def predict(update, context):
    try:
        numbers = list(map(int, context.args))
        if len(numbers) != 10:
            update.message.reply_text("❌ कृपया 10 नंबर दो। उदाहरण: /predict 5 3 2 1 9 8 7 6 4 0")
            return

        result = predict_numbers(numbers)
        update.message.reply_text(result)

    except:
        update.message.reply_text("⚠️ कुछ गलत हुआ। सही फॉर्मेट: /predict 5 3 2 1 9 8 7 6 4 0")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
