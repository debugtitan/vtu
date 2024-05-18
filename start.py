import logging
from telegram import Chat, User
from telegram.ext import Application

log = logging.getLogger(__name__)


class MirkBot:

    def __init__(self, bot: Application, chat: Chat, user: User, conf, *args, **kwargs):
        self.bot = bot
        self.chat = chat
        self.user = user
        self.conf = None
        self.loc = None
