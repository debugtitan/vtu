from telegram import KeyboardButton, ReplyKeyboardMarkup
from billbuddy.utils import enums
from billbuddy.utils import cfg


def start_menu():
    START_MENU = "CONTINUE " + enums.ReactionType.PROCEED.value
    return ReplyKeyboardMarkup([[KeyboardButton(START_MENU)]], resize_keyboard=True)
