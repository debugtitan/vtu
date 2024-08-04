from typing import Optional
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
