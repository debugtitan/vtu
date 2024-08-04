from typing import Optional

from telegram import User
from billbuddy.resources.users import Users
from billbuddy.resources.connection import db_dependacy, Session


async def user_exists(tg_id: int, db=db_dependacy):
    exist = db.query(Users).filter(tg_id == Users.tg_id).first()
    return exist is not None


async def add_user(
    first_name: str, tg_id: int, username: Optional[str] = None, db=db_dependacy
):
    if await user_exists(tg_id):
        return
    new_user = Users(first_name=first_name, tg_id=tg_id, username=username)

    db.add(new_user)
    db.commit()
    return


async def get_user(tg_id: int, db=db_dependacy):
    user = db.query(Users).filter(Users.tg_id == tg_id).first()
    return user


async def setup_user_language(tg_id: int, lang_code: str, db=db_dependacy):
    user = db.query(Users).filter(Users.tg_id == tg_id).first()
    if user:
        user.language_code = lang_code
        db.commit()
        return
