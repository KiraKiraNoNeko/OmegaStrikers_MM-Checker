import requests
from bs4 import BeautifulSoup

def fetch_player_ranks(players):
	for key, val in players.items():
		r = requests.get(f"https://stats.omegastrikers.gg/player/{val[0]}")
		soup = BeautifulSoup(r.content, 'html.parser')
		rank = soup.find('h2')
		lp = rank.find_next()
		players[key].append(rank.contents[0])
		players[key].append(lp.contents[0])

	return players