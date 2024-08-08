from decimal import Decimal
from sqlalchemy import Column, String, Boolean, DECIMAL, Enum, Integer

from billbuddy.resources.connection import Base
from billbuddy.utils import enums


class Users(enums.BaseModelMixin, Base):
    """Default user models for billbuddy telegram app"""

    first_name = Column(String)
    # last_name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=True)
    tg_id = Column(Integer, unique=True)
    email = Column(String, nullable=True)
    balance = Column(
        DECIMAL(precision=20, scale=2), default=lambda: Decimal("0.00"), nullable=False
    )
    buddy_points = Column(Integer, default=0)
    account_type = Column(
        Enum(enums.AccountType), default=enums.AccountType.CLIENT.value, nullable=False
    )
    language_code = Column(String, default="es", nullable=False)
    phone_number = Column(String, nullable=True)
    wallet = Column(String, nullable=True)
    is_restricted = Column(Boolean, default=False)
    navigator_id = Column(Integer, default=0)

    @property
    def is_admin(self):
        return self.account_type != enums.AccountType.CLIENT.value

    @property
    def is_owner(self):
        return self.account_type == enums.AccountType.OWNER.value
