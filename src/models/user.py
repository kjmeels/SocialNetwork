from sqlalchemy import Column, VARCHAR, INT, DateTime, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Enum as AlchemyEnum

from .choices import MaleState


class User(DeclarativeBase):
    name = Column(VARCHAR(64), nullable=False)
    surname = Column(VARCHAR(64), nullable=False)
    age = Column(INT, nullable=False)
    # date_birthday = DateTime(timezone=True)
    city = Column(VARCHAR(64), nullable=True)
    country = Column(VARCHAR(64), nullable=True)
    male = Column(AlchemyEnum(MaleState), nullable=False, doc="М/Ж")
    phone_number = Column(VARCHAR(64), nullable=True)
    email = Column(String, nullable=True, doc="Email")

    # photo = Column(String, nullable=True)

    def __repr__(self):
        return self.name
