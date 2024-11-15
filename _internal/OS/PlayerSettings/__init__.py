__all__ = ["DisplayCurrentMatchNames"]

from .GetCurrentPlayers import *
from .GetPlayerRanks import *

if __name__ == "__main__":
    print("Matchmaking package loaded.")
    print("Displaying current match names:")
    players = fetch_player_names()
    display_players(players)

    print("Displaying player ranks:")
    

    print("Done.")