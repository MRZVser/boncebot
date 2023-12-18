import asyncio
from aiogram import Bot, Dispatcher, types
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

async def start_game(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}!\n Начинаем игру!")
    await asyncio.sleep(1)

    bot_data = (await bot.send_dice(message.from_user.id))['dice']['value']
    await asyncio.sleep(5)

    user_data = (await bot.send_dice(message.from_user.id))['dice']['value']
    await asyncio.sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Вы проиграли!")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, "Вы выйграли!")
    else:
        await bot.send_message(message.from_user.id, "Ничья!")

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await start_game(message)

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
