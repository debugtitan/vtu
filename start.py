import os
import threading

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
        
    def run(self):
        log.info(f"Worker for chat {self.chat.id} started")
        while self.running:
            # Here you would add the logic for handling messages or tasks
            log.info(f"Worker {self.chat.id} is running...")
            #time.sleep(1)

    def stop(self):
        self.running = False
        log.info(f"Worker for chat {self.chat.id} stopped")
        
    
        




        
    
        