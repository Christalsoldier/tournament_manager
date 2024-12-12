from dataclasses import dataclass
from math import ceil

class SwissConfig:
    def __init__(self, max_players: int):
        self.player_count = max_players
        self.__players_per_game = 0
        self.__winners_per_game = 0
        self.__rounds: int = 0
    
    @property
    def players_per_game(self)-> int:
        return self.__players_per_game
    
    @players_per_game.setter
    def players_per_game(self, count: int):
        if count > self.player_count:
            raise AttributeError("There cannot be more players in a game than total players")
        self.__players_per_game = count
    
    
    @property
    def winners_per_game(self)-> int:
        return self.__winners_per_game
    
    @winners_per_game.setter
    def winners_per_game(self, count: int):
        if count > self.__players_per_game:
            raise AttributeError("There cannot be more winner per game than total players")
        self.__winners_per_game = count
        
    @property
    def rounds(self) -> int:
        first_number_of_rounds = self.player_count / self.players_per_game
        
        
    def games_per_round(round_number: int) -> int:
        return 0
    
def draw_pyramid(height):
    for i in range(1, height + 1):
        # Erzeuge die Zeile der Pyramide mit Sternen
        line = '*' * i
        print(line)
    for i in range(height - 1, 0, -1):
        # Erzeuge die abnehmenden Zeilen der Pyramide
        line = '*' * i
        print(line)

if __name__ == "__main__":
    c = SwissConfig(20)
    c.players_per_game = 4
    c.winners_per_game = 2
    
    number_of_end_winners = 8
    needed_number_of_wins = ceil(c.player_count / number_of_end_winners)
    print(f"number of wins to advance/drop out: {needed_number_of_wins}")
    
    number_of_rounds = (needed_number_of_wins * 2) - 1
    print(f"number of rounds {number_of_rounds}")
    draw_pyramid(number_of_rounds)
    
    first_number_of_games = c.player_count / c.players_per_game
    print(f"games in the first round {first_number_of_games}")
          
          