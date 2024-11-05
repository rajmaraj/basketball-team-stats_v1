"""
Data Analysis Techdegree
Project 2 - Basketball Team Stats Tool
--------------------------------
"""

from constants import TEAMS, PLAYERS
# Import data from dictionaries under constants file

""" 
This data should be cleaned fom constants,
height should be an integer,
experience should be a boolean value,
guardians should be a split by 'and' string into a list.
"""

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

# # print just 'guardians' from the list of players
# def guardians_list(players):
#     guardian_list = []
#     for player in players:
#         guardian_list.extend(player['guardians'])
#     return guardian_list
# # print(guardians_list(clean_data(PLAYERS)))


# # print just 'name' from the list of players
# def player_list(players):
#     player_list = []
#     for player in players:
#         player_list.append(player['name'])
#     return player_list
# # print(player_list(clean_data(PLAYERS)))



"""
Assign players to each team so the teams are evenly balanced by total players.
The order in which you assign the players does not matter but should be balanced when team assignment is finished.
The same player cannot be assigned to multiple teams.
"""

def draft_players(players): # Function designed to distribute players into 3 teams.
    global panthers, bandits, warriors # Allows function to modify team outside of function.
    experienced = []# Empty list
    inexperienced = []# Empty list
    panthers = []# Empty list
    bandits = []# Empty list
    warriors = []# Empty list

    for player in players: # Iterates through all players and separates them into exp or not exp.
        if player['experience'] == True:
            experienced.append(player) # Sent to exp list
        else:
            inexperienced.append(player) # Sent to non exp list


# This function should assign the players as evenly as possible to all three teams.
# If there are not enough players in one of the experience levels, 
# Then the remaining players should be assigned to the teams with fewer players.
# The distribution method uses division to assign players to teams evenly.
# The * modulo * operator is used to assign players to teams in a round-robin fashion.
    for num, player in enumerate(experienced, start=1): # Starting from 1 assigns each exp player a number
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)


# This function should assign the inexperienced players to the teams with fewer players.
# 
    for num, player in enumerate(inexperienced, start=1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors
#print(draft_players(clean_data(PLAYERS)))
