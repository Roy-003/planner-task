"""Importing the required dependencies"""

from typing import Any, Generator
from sqlmodel import SQLModel, Session, create_engine
# from models.events import Event

DATABASE_FILE = "planner.db"
database_connection_string = f'sqlite:///{DATABASE_FILE}'
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string,
                           echo=True, connect_args=connect_args)

def conn()->None:
    """Connect to the database"""
    SQLModel.metadata.create_all(engine_url)

def get_session() -> Generator[Session, Any, None]:
    """Returns a session to interact with the database"""
    with Session(engine_url) as session:
        yield session
        