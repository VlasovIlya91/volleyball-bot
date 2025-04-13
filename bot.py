import logging
import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логгирование
logging.basicConfig(level=logging.INFO)

# Загружаем переменные окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен подгрузился
print(f"Токен получен: {'да' if BOT_TOKEN else 'нет'}")

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Команда /start вызвана")
    await update.message.reply_text(group_info)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Получено сообщение: {update.message.text}")
    await update.message.reply_text("Спасибо за сообщение!")

async def main():
    if not BOT_TOKEN:
        print("❌ Токен не найден. Проверь файл .env")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Бот запущен. Ожидаем сообщения...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())


