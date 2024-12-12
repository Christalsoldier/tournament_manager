from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from database.orm.base import Base


class SessionHandler(object):
    def __init__(self, engine_url: str):
        self._engine: Engine = create_engine(engine_url, echo=True)
        """Engine to use in this sessionHandler"""
        Base.metadata.create_all(self._engine)
        self._context: sessionmaker = sessionmaker(bind=self._engine)
        self._session: Optional[Session] = None
        
    def __enter__(self) -> Session:
        self._session = self._context()
        return self._session
    
    def __exit__(self, exc_type, exc_value, traceback):
        assert(isinstance(self._session, Session))
        self._session.commit()
