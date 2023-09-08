from flask import Flask, redirect, request, url_for, render_template
import json
import requests
import pprint


app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    
    name = input("Enter NBA player name: ")
    url = "https://www.balldontlie.io/api/v1/players?search=" + str(name)
    player_info = requests.get(url)
    player_info_json = player_info.json()
    player_statistics = player_info_json['data']
    pprint.pprint(player_statistics)
    return render_template("input.html")



if __name__ == "__main__":
    app.run()

#what do i have to do? 
# the end user inputs a NBA Player, i take that information and return the player's stats

