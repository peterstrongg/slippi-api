from flask import Flask
from scraper import get_info
import json

api = Flask(__name__)

@api.route("/player/<code>")
def get_player_data(code):
    return json.dumps(get_info(code))

@api.route("/leaderboard")
def get_leaderboard():
    return "leaderboard"

api.run()
