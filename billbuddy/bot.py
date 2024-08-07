from contextlib import suppress
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from billbuddy.utils import logger, exceptions
from billbuddy import config
from billbuddy.resources import connection
from billbuddy.actions import (
    start,
    inline_handlers,
    menu,
    localization,
    help_faq,
    balance,
)

connection.Base.metadata.create_all(connection.engine)


class BillBuddyBot:
    def __init__(self, token):
        self.app = self._setup_bot(token)

    def _setup_bot(self, token):
        return Application.builder().token(token).build()

    @exceptions.exception_handlers
    def run(self):
        logger.info("Bot start up!")

        self.app.add_handler(CommandHandler("start", start.start_command_handler))
        self.app.add_handler(CommandHandler("menu", menu.main_menu_handler))

        # CALLBACK QUERY HANDLER
        self.app.add_handler(
            CallbackQueryHandler(
                inline_handlers.language_handler, pattern="^localization#"
            )
        )

        # BUTTON HANDLERS
        self.app.add_handler(
            MessageHandler(
                filters.Regex("^(🌐 Multi-Language Support|🌐 Soporte multilingüe)$"),
                localization.localization_handler,
            )
        )

        self.app.add_handler(
            MessageHandler(
                filters.Regex("^(❓ Help|❓ Ayuda)$"),
                help_faq.help_message_handler,
            )
        )

        self.app.add_handler(
            MessageHandler(
                filters.Regex("^(💳 Check Balance|💳 Consultar saldo)$"),
                balance.balance_handler,
            )
        )

        self.app.run_polling()

    def stop(self):
        self.app.stop_running()

    @staticmethod
    @exceptions.exception_handlers
    def start(token):
        with suppress(KeyboardInterrupt):
            token: str = config.BOT_TOKEN
            bot = BillBuddyBot(token)
            bot.run()
