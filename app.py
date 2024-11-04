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
        fixed['height'] = int(player['height'].split()[0]) 
        # Translates string into integer value and removes "inches"
        cleaned.append(fixed) # Appends the fixed dictionary to the cleaned list
    return cleaned # Returns the cleaned list
print(clean_data(PLAYERS)) # Prints the cleaned list