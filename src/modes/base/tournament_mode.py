from src.database.orm.player import Player

from src.modes.tools.enums.gamemodes import GameModes


class TournamentMode(object):

    def __init__(self, players: list[Player], mode: GameModes):
        self.playercount: list[Player] = players
        self.gamemode: GameModes = mode

    def start_tournament(self):
        pass

    def cancel_tournament(self):
        pass

    def finish_round(self):
        pass
