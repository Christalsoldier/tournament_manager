from typing import TYPE_CHECKING, Iterator

from src.database.orm.player import Player
from src.database.session_handler import SessionHandler


class DBHandler(object):

    def __init__(self, engine_url: str):
        self.session_handler = SessionHandler(engine_url)


    def add_player(self, player: Player):
        with self.session_handler as s:
            s.add(player)

    def get_all_player(self) -> Iterator[Player]:
        ret: list[Player]
        with self.session_handler as s:
            ret = s.query(Player).all()
        return ret




if __name__ == "__main__":
    handler = DBHandler("sqlite:///temp/database.db")
    handler.add_player(Player(first_name="Hendrik", last_name="Marske"))
    handler.add_player(Player(first_name="Christoph", last_name="Stiefel"))
    handler.add_player(Player(first_name="Kevin", last_name="Buchner"))
    handler.add_player(Player(first_name="Patrick", last_name="Marske"))
    handler.add_player(Player(first_name="Helmut", last_name="Stiefel"))
    handler.add_player(Player(first_name="Tobias", last_name="Buchner"))
    handler.add_player(Player(first_name="Hannes", last_name="Marske"))
    handler.add_player(Player(first_name="Michael", last_name="Stiefel"))
    handler.add_player(Player(first_name="Markus", last_name="Buchner"))
    handler.add_player(Player(first_name="Daniel", last_name="Marske"))
    handler.add_player(Player(first_name="Andreas", last_name="Stiefel"))
    handler.add_player(Player(first_name="Klaus-Dieter", last_name="Buchner"))
    handler.add_player(Player(first_name="Heiko", last_name="Marske"))
    handler.add_player(Player(first_name="Rasoul", last_name="Stiefel"))
    handler.add_player(Player(first_name="Stefan", last_name="Buchner"))

    for a in handler.get_all_player():
        print(a.first_name)
        input()
