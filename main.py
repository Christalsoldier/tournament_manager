from typing import Final

from database.db_handler import DBHandler


databasefile: Final[str] = "sqlite:///temp/database.db"

if __name__ == "__main__":
    db = DBHandler(databasefile)