import logging
from telegram import Chat, User
from telegram.ext import Application
from mkconfig import ConfigManager

log = logging.getLogger(__name__)


class MirkBot:

    def __init__(
        self,
        bot: Application,
        chat: Chat,
        user: User,
        conf: ConfigManager,
        *args,
        **kwargs
    ):
        self.bot = bot
        self.chat = chat
        self.user = user
        self.conf = conf
        self.loc = None
