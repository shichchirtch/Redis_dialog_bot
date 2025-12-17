import asyncio
from command_handlers import ch_router
from bot_instans import bot, bot_storage_key, dp
from aiogram_dialog import setup_dialogs
from dialogs import start_dialog, create_dialog
from start_menu import set_main_menu
from zeigen_dialog import zeigen_dialog
# from admin_dialog import admin_dialog


async def main():

    dp.startup.register(set_main_menu)
    await dp.storage.set_data(key=bot_storage_key, data={})

    dp.include_router(ch_router)
    dp.include_router(start_dialog)
    dp.include_router(create_dialog)
    dp.include_router(zeigen_dialog)
    # dp.include_router(admin_dialog)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    setup_dialogs(dp)
    await dp.start_polling(bot)

asyncio.run(main())