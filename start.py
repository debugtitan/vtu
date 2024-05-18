import os
import threading
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_setup')

import logging
from telegram import Chat, User, Bot
from mkconfig import ConfigManager

log = logging.getLogger(__name__)


class MirkBotWorker(threading.Thread):

    def __init__(
        self,
        bot: Bot,
        chat: Chat,
        user: User,
        conf: ConfigManager,
        *args,
        **kwargs
    ):
        # Initialize thread
        super().__init__(name=f"Worker {chat.id}", *args, **kwargs)
        self.bot = bot
        self.chat = chat
        self.user = user
        self.conf = conf
        self.loc = None
        
        #Initialize django migrations
        self._make_django_migrations()
        
    def _make_django_migrations(self):
        
        import django
        try:
            django.setup()
            from django.core.management import call_command
            log.debug("Running makemigrations...")
            call_command('makemigrations', 'database')
            log.debug("Makemigrations completed.")

            # Apply migrations
            log.debug("Running migrate...")
            call_command('migrate','database')
            log.debug("Migrate completed.")

        except Exception as e:
            print(f"An error occurred: {e}")



        
    
        