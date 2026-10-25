import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice
from aiogram.filters import CommandStart

BOT_TOKEN = "8796038950:AAHYYKJLQbARcrZSR4D2MPGeKykfv2XdGZE"
ADMIN_ID = 6274533113
КАВЫЧЕК
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer_invoice(
        title="100 звёзд для Приватки",
        description="Покупка 100 звёзд для использования в приватке Нортона",
        payload="stars_100",
        currency="XTR",
        prices=[LabeledPrice(label="100 звёзд", amount=100)],
        provider_token="" 
    )

@dp.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery):
    await query.answer(ok=True)

@dp.message(F.successful_payment)
async def successful_payment(message: Message):
    await bot.send_message(
        ADMIN_ID, 
        f"Пользователь @{message.from_user.username} купил {message.successful_payment.total_amount} звёзд!"
    )
    await message.answer("Оплата прошла! Звёзды зачислены (пока просто тест).")

async def main():
    await dp.start_polling(bot)

if name == "main":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    server.serve_forever()

# Запускаем заглушку в отдельном потоке
Thread(target=run_health_server, daemon=True).start()
