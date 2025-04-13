import logging
import os
import csv
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# Логирование
logging.basicConfig(level=logging.INFO)

# Загружаем токен
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logging.error("❌ Токен не найден! Проверь .env файл.")
else:
    logging.info(f"Токен получен: {'да' if BOT_TOKEN else 'нет'}")

# Текст
group_info = """Мы рады, что тебе интересны занятия волейболом! Вот, что мы можем предложить: 
🔥 ОДИНЦОВО!
📌 Можайское шоссе 109а
⏱ 20.15-22.15
📆 Понедельник, среда
🏐 Уровень: средний-
🧘‍♂️ Разминка, Офп, Техника, ±30 мин игра

Бесплатная парковка, раздевалка и душ, большие ауты, высокие потолки!

🥳 Только позитив, команда, новые знакомства и твой личный рост!
Заряжайся вместе с нами! m&mV🏐LL!🤩

Если тебе это подходит, пиши @sovamarii и тебя включат в состав на игру"""

# Функция для записи статистики в CSV файл
def log_start(user_id, username):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('start_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, username, timestamp])

# Команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("👉 Команда /start вызвана")

    # Логируем информацию о пользователе
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    log_start(user_id, username)

    await update.message.reply_text(group_info)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"💬 Получено сообщение: {update.message.text}")
    await update.message.reply_text("Спасибо за сообщение!")

# Запуск
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("✅ Бот запущен. Ожидаем сообщения...")
    app.run_polling()

if __name__ == "__main__":
    main()

