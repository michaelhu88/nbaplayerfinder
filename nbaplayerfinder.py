from flask import Flask
import requests
import pprint

url = "https://www.balldontlie.io/api/v1/players"

get_players = requests.get(url)
get_players_json = get_players.json()
pprint.pprint(get_players_json)



app = Flask(__name__)

@app.route("/")
def home():
    get_players = requests.get(url)
    get_players_json = get_players.json()
    pprint.pprint(get_players_json)

if __name__ == "__main__":
    app.run()
