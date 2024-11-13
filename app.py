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
    for num, player in enumerate(inexperienced, start=1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors

# Call to populate each team
# draft_players function within clean_data of the PLAYERS parameter
draft_players(clean_data(PLAYERS))

def team_stats(team_name): # Function to print team stats
    team = [] # Empty list
    guardians = [] # Empty list
    height = [] # Empty list 
    inexperienced_player = 0 # Counter 
    experienced_player = 0 # Counter
    for player in team_name: # Iterates through the team name
        # team.append(player['name']) # Appends the player name to the team list
        team.append({'name': player['name'], 'height': player['height']})  # Include name and height together
        guardians.extend(player['guardians']) # Appends the player guardians to the guardians list
        height.append(player['height']) # Appends the player height to the height list
        if player['experience']: # If the player is experienced
            experienced_player += 1 # Adds 1 to the experienced list
        else:
            inexperienced_player += 1 # Adds 1 to the inexperienced list
    avg_height = sum(height) / len(height) # Calculates the average height of the team
    # List players height from shortest to tallest
    short_to_tall = sorted(height)
    return team, guardians, avg_height, inexperienced_player, experienced_player # Returns the team, guardians, and average height
#print(team_stats(bandits)) # Prints the team stats


"""
Present menu to the user with the following options:
1) Display Team Stats
2) Quit
Display Team Stats:
    1) Panthers
    2) Bandits
    3) Warriors
Sort players by height, average height, exp or not exp, guardians.
The program should be able to display the stats for a given team.
The program should not crash if the user enters an incorrect option.
"""

def menu(): # Function to print the menu
    print("\nBASKETBALL TEAM STATS TOOL\n") # Prints the menu
    print("------- MENU -------\n") # Prints the menu
    print("1) Display Team Stats") # Prints the menu
    print("2) Quit\n") # Prints the menu
    print("\nPlease select an option: \n") # Prints the menu
    option = input() # Gets the user input
    if option == '1': # If the user selects 1
        print("\n1) Panthers\n2) Bandits\n3) Warriors\n") # Prints the menu
        print("\nPlease select a Team: \n") # Prints the menu
        team_option = input() # Gets the user input
        if team_option == '1': # If the user selects 1
            print("\nTeam: Panthers Stats\n--------------------\n") # Prints the menu
            #print("\nPlayers: ", ', '.join(team_stats(panthers)[0])) # Prints player as a string separated by comma space
            print("\nPlayers: ", ', '.join(player['name'] for player in sorted(team_stats(panthers)[0], key=lambda x: x['height']))) 
            # Access height value in team_stats function, searches for 'height' in dictionary, then sorts lowest to highest by key value of 'height'
            # Then sort extracts the associated 'name' of each 'height' value, finally joins values into a string and prints
            print("\nGuardians: ", ', '.join(team_stats(panthers)[1])) # Prints guardians as a string separated by comma space
            print("\nAverage Height: ", round(team_stats(panthers)[2])) # Prints rounded height 
            print("\nNumber of Players: ", int(len(team_stats(panthers)[0]))) # Prints integer or players
            print("\nNumber of Inexperienced Players: ",team_stats(panthers)[3]) # Prints inexp players amount
            print("\nNumber of Experienced Players: ",team_stats(panthers)[4]) # Prints exp players amount
            menu() # Calls the menu function
        elif team_option == '2': # If the user selects 2
            print("\nTeam: Bandits Stats\n--------------------\n") 
            # print("\nPlayers: ", ', '.join(team_stats(bandits)[0]))
            print("\nPlayers: ", ', '.join(player['name'] for player in sorted(team_stats(bandits)[0], key=lambda x: x['height'])))
            print("\nGuardians: ", ', '.join(team_stats(bandits)[1])) 
            print("\nAverage Height: ", round(team_stats(bandits)[2])) 
            print("\nNumber of Players: ", int(len(team_stats(bandits)[0]))) 
            print("\nNumber of Inexperienced Players: ", team_stats(bandits)[3]) 
            print("\nNumber of Experienced Players: ", team_stats(bandits)[4])
            menu() # Calls the menu function
        elif team_option == '3': # If the user selects 3
            print("\nTeam: Warriors Stats\n--------------------") 
            # print("\nPlayers: ", ', '.join(team_stats(warriors)[0]))
            print("\nPlayers: ", ', '.join(player['name'] for player in sorted(team_stats(warriors)[0], key=lambda x: x['height'])))
            print("\nGuardians: ", ', '.join(team_stats(warriors)[1])) 
            print("\nAverage Height: ", round(team_stats(warriors)[2]))
            print("\nNumber of Players: ", int(len(team_stats(warriors)[0])))
            print("\nNumber of Inexperienced Players: ", team_stats(warriors)[3])
            print("\nNumber of Experienced Players: ", team_stats(warriors)[4])
            menu() # Calls the menu function
        else:
            print("\n!! Invalid option. Please try again !!\n") # Prints if option is not selected
            menu() # Calls the menu function
    elif option == '2': # If the user selects 2
        print("\nGoodbye!\n") # Prints quit message
        exit() # Exits the program
    else:
        print("\n!! Invalid option. Please try again !!\n") # Prints if option is not selected
        menu() # Calls the menu function
    return input() # Returns the user input


menu() # Calls the menu function
