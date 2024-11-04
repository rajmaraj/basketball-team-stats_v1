from constants import TEAMS
from constants import PLAYERS
# Import data from dictionaries under constants file

def clean_data(players): # Using players data set
    cleaned = [] # Empty list
    for player in players: # Iterating through the players list
        fixed = {} # Empty dictionary
        fixed['name'] = player['name'] # Maps "name" from constants to "name" in app
        fixed['guardians'] = player['guardians'].split(' and ') # Maps "guardians" and splits the string into a list at 'and'
        fixed['experience'] = player['experience'] # Maps "experience" from constants to "experience" in app
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False # Translates "YES/NO" into a boolean value of True or False via if/else statement
        # fixed['height'] = int(player['height'])
        fixed['height'] = int(player['height'].split()[0]) # Translates string into integer value and removes "inches"
        cleaned.append(fixed) # Appends the fixed dictionary to the cleaned list
    return cleaned # Returns the cleaned list
# print(clean_data(PLAYERS)) # Prints the cleaned list

cleaned_players = clean_data(PLAYERS) # Assigns the cleaned list to a variable
def assign_to_teams(players, teams):
    team_rosters = {team: [] for team in teams}
    team_index = 0 # Creates a dictionary with the teams as keys and empty lists as values
    
    for player in players:
        team_name = teams[team_index]  # Get the current team by index
        team_rosters[team_name].append(player)  # Add player to the team roster
        team_index = (team_index + 1) % len(teams) 
    return team_rosters
assigned_teams = assign_to_teams(cleaned_players, TEAMS)
# print(assigned_teams)

for team, players in assigned_teams.items():
    print(f"{team}:")
    player_names = [player['name'] for player in players]  # Extract only the names
    print(player_names)






# # Assign players to 3 teams so the teams are evenly balanced by total players.
# def balance_teams(players, teams): # Using players data set and TEAMS list
#     num_players_team = len(players) // len(teams) # Divides the total number of players by the number of teams
#     team_players = [] # Empty list
#     for i in range(0, len(players), num_players_team): # Iterates through the players list by the number of players per team
#         team_players.append(players[i:i + num_players_team]) # Appends the players to the team_players list
#     return team_players # Returns the team_players list
# print(balance_teams(clean_data(PLAYERS), TEAMS)) # Prints the team_players list
