from aiogram.types import BotCommand


async def set_main_menu(bot):
    main_menu_commands = [
        BotCommand(command='/basic_menu',
                   description='Zurück zum Grundmenu'),

        BotCommand(command='/help',
                   description='Info über Bot')

    ]
    await bot.set_my_commands(main_menu_commands)
