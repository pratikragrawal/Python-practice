import numpy as np
import pandas as pd

class FootballClub:
    def __init__(self, name):
        self.name = name
        self.players = pd.DataFrame(columns=['Name', 'Position', 'Age', 'Nationality'])
    
    def add_player(self, player_info):
        self.players = self.players.append(player_info, ignore_index=True)
    
    def get_players_by_position(self, position):
        return self.players[self.players['Position'] == position]
    
    def get_average_age(self):
        return np.mean(self.players['Age'])

# Usage example
club_name = input("Enter the name of your football club: ")
club = FootballClub(club_name)
while True:
    player_name = input("Enter the player's name (or 'q' to quit): ")
    if player_name == 'q':
        break
    
    player_position = input("Enter the player's position: ")
    player_age = int(input("Enter the player's age: "))
    player_nationality = input("Enter the player's nationality: ")
    
    club.add_player({'Name': player_name, 'Position': player_position, 'Age': player_age, 'Nationality': player_nationality})

position = input("Enter a position to get players: ")
players_by_position = club.get_players_by_position(position)
average_age = club.get_average_age()

print(f"The players in the {position} position are:\n{players_by_position}")
print(f"The average age of the players is: {average_age}")
