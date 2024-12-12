from src.database.orm.player import Player

from src.modes.Swiss.dataclasses.config import SwissConfig
from src.modes.base.tournament_mode import TournamentMode
from src.modes.tools.enums.gamemodes import GameModes


class SwissMode(TournamentMode):
    def __init__(self, players: list[Player]):
        super().__init__(players, GameModes.swiss)
        self.config: SwissConfig = SwissConfig(len(players))
        
    def configure_tournament(self):
        while True:
            try:
                self.config.players_per_game = int(input("Bitte geben Sie die Spieler pro Spiel an: "))
                break
            except AttributeError as e:
                print(e.args[0])

        while True:
            try:
                self.config.winners_per_game = int(input("Bitte geben Sie die Anzahl der Gewinner pro Spiel an: "))
                break
            except AttributeError as e:
                print(e.args[0])
        
    def start_tournament(self):
        
        return super().start_tournament()