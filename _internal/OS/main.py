import Matchmaking as mm
from texttable import Texttable
import os

def displayTable(players):
    t = Texttable()
    t.add_row(["#", "NAME", "RANK", "LP"])
    for key, val in players.items():
        t.add_row([key, val[0], val[1], val[2]])
    print(t.draw())

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        clear()
        print(f"""
{'='*30}
Omega Strikers Match Checker
{'='*30}

To use this program, wait until the match countdown begins (Meaning: After ban/pick phase).
It takes approx 17s until each player has been scraped and listed. (Python is slow.)

Credits: KiraKiraNoNeko, Based upon ***I BELIEVE*** ATAH (Sorry if im wrong.)
Last Updated: 06/11/2024 20:30
            """)

        while True:
            x = input("Start program? (y/n): ")
            if x != "y": 
                break

            clear()
            print("Running player checks...")
            players = mm.fetch_player_names()
            mm.fetch_player_ranks(players)
            print("Player Data found!\n")
            displayTable(players)
            print("\n\n")
    except:
        pass
    print("program stopped3.")