from random import shuffle

class Team():
    def __init__(self, players):
        self.players = players
        self.name = self.get_team_name()

    def get_team_name(self):
        """Returns a single string with an adjective and a noun."""
        return "A team name"


class GroupOfTeams():
    def __init__(self):
        self.teams = []
        self.get_teams()

    def get_players(self):
        """Returns a list of all players."""
        return ["A list", "of players"]

    def get_teams(self):
        # List of tuples for player pairings
        pairs_of_players = []
        full_list_of_players = self.get_players()
        shuffle(full_list_of_players)

        while full_list_of_players:
            first_player = full_list_of_players.pop()
            second_player = full_list_of_players.pop()
            self.teams.append(Team([first_player, second_player]))
