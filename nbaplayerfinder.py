from flask import Flask, redirect, request, url_for, render_template
import requests
import pprint


url = "https://www.balldontlie.io/api/v1/players?page=1&per_page=10"



app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    #get_players = requests.get(url)
    #get_players_json = get_players.json()
    #pprint.pprint(get_players_json)
    return render_template("input.html")

if __name__ == "__main__":
    app.run()

#what do i have to do? 
# the end user inputs a NBA Player, i take that information and return the player's stats

