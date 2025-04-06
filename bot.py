import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

group_info = """Мы рады, что тебе интересны занятия волейболом! Вот, что мы можем предложить: 
🔥 ОДИНЦОВО!
📌 Можайское шоссе 109а
⏱ 20.15-22.15
📆 Понедельник, среда
🏐 Уровень: средний-
🧘‍♂️ Разминка, Офп, Техника, ±30 мин игра
💸 1000 ₽/1000 ₽/1300 ₽
пробное/по абонементу/разовое

Тренер: Мария Стрекалова. КМС, 4-х кратная чемпионка России. 💪
Бесплатная парковка, раздевалка и душ, большие ауты, высокие потолки!

🥳 Только позитив, команда, новые знакомства и твой личный рост!
Заряжайся вместе с нами! m&mV🏐LL!🤩

Если тебе это подходит, пиши @sovamarii и тебя включат в состав на игру"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(group_info)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Спасибо за сообщение!")

async def main():
    app = ApplicationBuilder().token("8029397370:AAEFLQ_ZrEt-BMDSIHnE7u6zwwR1mJWI8os").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
