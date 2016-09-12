from random import shuffle, choice
import json


class Team():
    def __init__(self, players, team_name):
        self.players = players
        self.name = team_name

class GroupOfTeams():
    def __init__(self):
        self.teams = []
        self.adjectives = []
        self.nouns = []
        self.setup()

    def setup(self):
        self.set_adjectives()
        self.set_nouns()

    def set_adjectives(self):
        with open('assets/adjectives.txt') as inputAdjectives:
            self.adjectives = inputAdjectives
            # Strip Off Newlines
            self.adjectives = [line.rstrip('\n').split(',') for line in self.adjectives]
            # Flatten List
        self.adjectives = [item for sublist in self.adjectives for item in sublist]

    def set_nouns(self):
        with open('assets/nouns.txt') as inputNouns:
            self.nouns = inputNouns
            """ Strip Off Newlines"""
            self.nouns = [line.rstrip('\n').split(',') for line in self.nouns]
            """ Flatten List """
        self.nouns = [item for sublist in self.nouns for item in sublist]

    def get_team_name(self):
        """Returns a single string with an adjective and a noun."""
        noun = choice(self.nouns)
        adjective = choice(self.adjectives)
        return "{} {}".format(noun.capitalize(), adjective.capitalize())

    def get_players(self):
        """Returns a list of all players."""
        with open('assets/students.json', 'r') as f:
            list_of_students = json.load(f)
        return list_of_students

    def get_teams(self):
        # List of tuples for player pairings
        pairs_of_players = []
        full_list_of_players = self.get_players()
        shuffle(full_list_of_players)

        while full_list_of_players:
            first_player = full_list_of_players.pop()
            second_player = full_list_of_players.pop()
            team_name = self.get_team_name()
            new_team = Team(
                [first_player, second_player],
                team_name
            )
            self.teams.append(new_team)
