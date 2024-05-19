import logging
import sys
import time
import mkconfig
from telegram import Chat, User, Bot
from telegram.error import (
    Forbidden,
    InvalidToken,
    NetworkError,
    TimedOut,
)
from start import MirkBotWorker


log = logging.getLogger(__name__)


def bot_factory(cfg: mkconfig.ConfigManager):

    def exception_handlers(func):
        """Decorator, can be applied to any function to retry in case of Telegram errors."""

        def result_func(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                # Bot token is invalid
                except InvalidToken:
                    log.fatal(f"Invalid Bot Token {func.__name__}(), exiting")
                    sys.exit(1)

                # Bot has not enough rights to perform the requested action
                except Forbidden:
                    log.debug(f"Unauthorized to call {func.__name__}(), skipping.")
                    return None

                # raised when a request took too long to finish
                except TimedOut:
                    log.warning(
                        f"Timed out while calling {func.__name__}(),"
                        f" retrying in {cfg.get('Telegram')['timed_out_pause']} secs..."
                    )
                    time.sleep(cfg.get("Telegram")["timed_out_pause"])
                    continue

                # due to networking errors
                except NetworkError as error:
                    log.error(
                        f"Network error while calling {func.__name__}(),"
                        f" retrying in {cfg.get('Telegram')['error_pause']} secs...\n"
                        f"Full error: {error.message}"
                    )
                    time.sleep(cfg.get("telegram")["error_pause"])
                    continue

        return result_func

    class MirkBot:
        def __init__(self, *args, **kwargs):
            self.cfg = cfg
            self.updater = self.setup_bot()
            self.read_timeout = self.cfg.get("Telegram")["read_timeout"]
            self.chat_workers = {}

        @exception_handlers
        def setup_bot(self):
            return Bot(self.cfg.get("Telegram")["token"])

        @exception_handlers
        def get_me(self):
            """ returns information about the bot from the updater. """
            return self.updater.get_me()

    return MirkBot
