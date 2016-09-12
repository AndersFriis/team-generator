from flask import render_template

from app import app
from app.lib.teams import GroupOfTeams

@app.route("/")
@app.route("/index")
def index():
    group_of_teams = GroupOfTeams()

    return render_template("index.html", group_of_teams=group_of_teams)
