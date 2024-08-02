from contextlib import suppress
from telegram.ext import Application, CommandHandler

from billbuddy.utils import logger
from billbuddy import config


class BillBuddyBot:
    def __init__(self, token):
        self.updater = self._setup_bot(token)

    def _setup_bot(self, token):
        return Application.builder().token(token).build()

    def run(self):
        logger.info("Bot start up!")
        self.updater.run_polling()


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        token: str = config.BOT_TOKEN
        bot = BillBuddyBot(token)
        bot.run()
