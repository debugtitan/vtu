import logging
import sys
import time
from telegram.error import Forbidden, InvalidToken, NetworkError, TimedOut, BadRequest

from billbuddy import config

log = logging.getLogger(__name__)


def exception_handlers(func):
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

            # when bot send bad request
            except BadRequest:
                log.debug(f"BadRequest call {func.__name__}(), skipping.")
                continue

            # raised when a request took too long to finish
            except TimedOut:
                log.warning(
                    f"Timed out while calling {func.__name__}(),"
                    f" retrying in {config.TIMED_OUT_PAUSE} secs..."
                )
                time.sleep(config.TIMED_OUT_PAUSE)
                continue

            # due to networking errors
            except NetworkError as error:
                log.error(
                    f"Network error while calling {func.__name__}(),"
                    f" retrying in {config.TIMED_OUT_PAUSE} secs...\n"
                    f"Full error: {error.message}"
                )
                time.sleep(config.TIMED_OUT_PAUSE)
                continue

    return result_func
