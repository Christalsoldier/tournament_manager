from typing import Final

from src.database.db_handler import DBHandler
from src.modes.Swiss.mode import SwissMode


databasefile: Final[str] = "sqlite:///temp/database.db"

if __name__ == "__main__":
    db = DBHandler(databasefile)
    mode = SwissMode(db.get_all_player())
    mode.configure_tournament()
    mode.start_tournament()
    input("waiting in the end")