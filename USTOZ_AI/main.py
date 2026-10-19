import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi! Render Environment Variables ga BOT_TOKEN qo‘shing.")


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "👨‍🏫 USTOZ AI ga xush kelibsiz!\n\n"
        "📚 O‘qituvchilar uchun aqlli test yaratish boti.\n\n"
        "🎓 1–11-sinf darsliklari asosida testlar "
        "tayyorlash uchun yaratilgan.\n\n"
        "⚙️ /help — bot haqida ma'lumot"
    )


@dp.message(Command("restart"))
async def restart_command(message: Message):
    await message.answer(
        "🔄 Jarayon qayta boshlandi!\n\n"
        "📚 Yangi test yaratishni /start orqali boshlang."
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "🤖 USTOZ AI\n\n"
        "👨‍🏫 O‘qituvchilar uchun test yaratish boti.\n\n"
        "📚 BOT NIMALAR QILADI?\n\n"
        "🎓 1–11-sinf darsliklari bilan ishlaydi.\n"
        "📖 Kerakli fan va darslikni tanlash imkonini beradi.\n"
        "📄 Kerakli betlar oralig‘ini qabul qiladi.\n"
        "🧠 Tanlangan betlardan 20 ta test yaratadi.\n"
        "🔤 A, B, C, D variantli savollar beradi.\n"
        "✅ Har bir savolning to‘g‘ri javobini ko‘rsatadi.\n"
        "🔄 Yangi test yaratish imkonini beradi.\n"
        "📄 Keyinchalik testni Word ko‘rinishida olish mumkin bo‘ladi.\n\n"
        "⚙️ BUYRUQLAR\n\n"
        "/start — botni boshlash\n"
        "/restart — jarayonni qayta boshlash\n"
        "/help — bot haqida ma'lumot\n"
        "/join — loyiha haqida"
    )


@dp.message(Command("join"))
async def join_command(message: Message):
    await message.answer(
        "🚀 USTOZ AI loyihasiga xush kelibsiz!\n\n"
        "Bu bot o‘qituvchilarga darsliklardan "
        "foydalangan holda test tayyorlashga yordam beradi."
    )


async def main():
    print("================================")
    print("     USTOZ AI BOT ISHGA TUSHDI")
    print("================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
