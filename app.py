import os
import sys
import asyncio

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_setup")

import threading
from pathlib import Path
from mkconfig import ConfigManager
from utils.mirkbot import bot_factory
from utils import logger


BASE_DIR = Path(__file__).resolve(strict=True).parent
config_dir = os.path.join(BASE_DIR, "config", "config.toml")


def setup_core_app():
    # Setup Database
    import django

    django.setup()
    from django.core.management import call_command

    # Make Migrations
    logger.info("Running makemigrations...")
    call_command("makemigrations", "database")

    # Apply migrations
    logger.info("Running migrate...")
    call_command("migrate", "database")
    logger.info("Migrate completed.")
    asyncio.run(main())


async def main():

    # Rename the main thread for presentation purposes
    threading.current_thread().name = "App"

    # Ensure the template config file exists
    if not os.path.exists(config_dir):
        logger.debug("config/config.toml does not exist.")

        with open(
            "config/config.example.toml", encoding="utf8"
        ) as template_cfg_file, open(config_dir, "w", encoding="utf8") as user_cfg_file:
            # Copy the template file to the config file
            user_cfg_file.write(template_cfg_file.read())

        logger.fatal(
            "A config file has been created at config/config.toml"
            " Customize it, then restart!"
        )
        exit(1)

    # Finish logging setup
    user_cfg = ConfigManager(config_dir)

    # bot instance
    bot = bot_factory(user_cfg)()

    # Test the specified token
    logger.debug("Testing bot token...")
    me = await bot.get_me()
    if me is None:
        logger.fatal(
            "The token you have entered in the config file is invalid. Fix it, then restart greed."
        )
        sys.exit(1)
    logger.debug("Bot token is valid!")

    # Notify on the console that the bot is starting
    logger.info(f"@{me.username} is starting!")
    



# Run the main function only in the main process
if __name__ == "__main__":
    setup_core_app()
