from os import getenv

def fetch_player_names():
    with open(f"{getenv('LOCALAPPDATA')}/OmegaStrikers/Saved/Logs/OmegaStrikers.log", encoding="utf-8") as f:
        f=f.read()
        texts=f.split("' equipping trainings")[-7:-1]#6 most recent players in log
        i = 0
        player_list = {}
        for text in texts:
            i+=1
            text = text.split("LogPMPlayerState: Player '")[-1]
            player_list[i] = [text]
    return player_list  