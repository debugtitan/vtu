from contextlib import suppress
from telegram.ext import Application, CommandHandler

from billbuddy.utils import logger, exceptions
from billbuddy import config

from billbuddy.actions import start


class BillBuddyBot:
    def __init__(self, token):
        self.app = self._setup_bot(token)

    def _setup_bot(self, token):
        return Application.builder().token(token).build()

    def run(self):
        logger.info("Bot start up!")

        self.app.add_handler(CommandHandler("start", start.start_command_handler))

        self.app.run_polling()

    @staticmethod
    @exceptions.exception_handlers
    def start(token):
        with suppress(KeyboardInterrupt):
            token: str = config.BOT_TOKEN
            bot = BillBuddyBot(token)
            bot.run()
