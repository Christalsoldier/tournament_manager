
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.orm.base import Base


class Player(Base):
    __tablename__ = "player"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    nick_name: Mapped[Optional[str]]
