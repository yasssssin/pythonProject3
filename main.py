import random

class Team:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        return self.team1 if self.team1.strength > self.team2.strength else self.team2

class Tournament:
    def __init__(self, teams):
        self.teams = teams

    def play_tournament(self):
        winners = []
        for i in range(0, len(self.teams), 2):
            match = Match(self.teams[i], self.teams[i+1])
            winners.append(match.play())
        if len(winners) == 1:
            return winners[0]
        else:
            return Tournament(winners).play_tournament()

print('test de mise a jour du fichier sur github')