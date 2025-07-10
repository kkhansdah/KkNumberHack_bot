from ai_logic import predict_numbers, update_accuracy, load_memory
from telegram.ext import Updater, CommandHandler
import json

# Memory file (pretrained)
memory = load_memory()

# Accuracy tracking
stats = {"total": 0, "correct": 0}

# Telegram command: /start
def start(update, context):
    update.message.reply_text("🤖 Welcome to Ultra AI Predictor Bot!\nUse /predict followed by last 10 numbers.")

# Telegram command: /predict
def predict(update, context):
    try:
        numbers = list(map(int, context.args))
        if len(numbers) != 10:
            update.message.reply_text("❌ Please send exactly 10 numbers like:\n/predict 3 4 5 6 1 0 8 9 7 2")
            return

        top3, logic = predict_numbers(numbers, memory)
        stats["total"] += 1

        response = f"🌟 Predicted Numbers:\n\n"
        response += f"🔵 Level 1: {top3[0]}\n🟢 Level 2: {top3[1]}\n🟣 Level 3: {top3[2]}\n\n"
        response += f"🧠 Logic: {logic}"

        update.message.reply_text(response)
    except:
        update.message.reply_text("⚠️ Invalid input. Use: /predict 1 2 3 4 5 6 7 8 9 0")

# Telegram command: /accuracy
def accuracy(update, context):
    if stats["total"] == 0:
        update.message.reply_text("⚠️ No predictions yet.")
        return
    percent = (stats["correct"] / stats["total"]) * 100
    update.message.reply_text(f"✅ Accuracy: {percent:.2f}%\n🎯 {stats['correct']} / {stats['total']}")

# Run bot (insert your token below)
def main():
    updater = Updater("7600921671:AAEGttPW5TnBd9Y_9KWtKfzn1pX3SklT3oI", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))
    dp.add_handler(CommandHandler("accuracy", accuracy))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
