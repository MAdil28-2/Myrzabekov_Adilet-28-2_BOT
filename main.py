from aiogram.utils import executor
from handlers import admin, extra, clients, callback
from config import dp
import logging

admin.register_handlers_admin(dp)
clients.register_clients(dp)
callback.register_handlers_callback(dp)
extra.register_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
