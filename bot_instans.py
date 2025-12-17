from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import StorageKey
from aiogram.fsm.state import State, StatesGroup
import redis.asyncio as aioredis
from aiogram.fsm.storage.redis import RedisStorage, Redis as AioredisWrapper

from aiogram.fsm.storage.base import DefaultKeyBuilder
key_builder = DefaultKeyBuilder(with_destiny=True)

r = aioredis.Redis(host="localhost", port=6379, decode_responses=True)

# aiogram wrapper (он сам использует redis внутри)
my_aioredis = AioredisWrapper(host="localhost", port=6379)
redis_storage = RedisStorage(redis=my_aioredis, key_builder=key_builder)

BOT_TOKEN = '<BOT_TOKEN>'

bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

bot_storage_key = StorageKey(bot_id=bot.id, user_id=bot.id, chat_id=bot.id)

dp = Dispatcher(storage=redis_storage)




class FSM_ST(StatesGroup):
    spam = State()
    start = State()
    basic = State()
    vacancies = State()

class CREATE(StatesGroup):
    einstellen = State()
    ask_capture = State()
    enter_capture = State()
    finish = State()


class ZEIGEN(StatesGroup):
    clava = State()
    list_notes = State()
    schlist = State()

class ADMIN(StatesGroup):
    first = State()
