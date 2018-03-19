# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #


# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string):
    h = 0
    network = []          #create an empty list for the network data
    while h < len(string)-1:
        lst = []          #create a new list, for each player
        #for entry player in the network:
        place = string.find("is", h)          #find player in the string and append it to list lst
        player = string[h : place - 1]
        lst.append(player)
        #find connections of that player and create a list of connections
        c = string.find("to", place)
        e = string.find(".", c)
        connections = string[c+3 : e]
        connections = connections.split(", ")
        lst.append(connections)                 #append list of connections to list lst, which represents the player
        #find players games and create a list of games
        g = string.find("play", place)
        h = string.find(".", g)
        games = string[g+5: h]
        games = games.split(", ")
        lst.append(games)                         #append list of games to list lst
        network.append(lst)                       #append list lst with player's info to the network
        h = h + 1
    return network

#create a list of all players
def list_players(network):
    n = len(network)
    i = 0
    lst = []
    while i < n:             #find all players in the network and append them to the list lst
        a = network[i][0]
        lst.append(a)
        i = i + 1
    return lst

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    for entry in network:
        if entry[0] == user:        #if player is in the network, return their connections
            if len(entry[1]) > 0:
                return entry[1]
            #if player doesn't have any connections, return an empty list
            return []

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.

def get_games_liked(network,user):
    for entry in network:
        if entry[0] == user:          #if player is in the network, return games they play
            if len(entry[2]) > 0:
                return entry[2]
            #if player doesn't play any games, return an empty list
            return []


# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

def add_connection(network, user_A, user_B):
    lst = list_players(network)
    if user_A == user_B:
        return network      
    if user_A in lst and user_B in lst:     #check if both players exist in the network
            for entry in network:
                if entry[0] == user_A:     #if player A is in the network, see if player B is in his connections
                    if user_B in entry[1]:
                        return network
                    #if player B is not in player A's connections, add him
                    entry[1].append(user_B)        
                    return network
    #if player A or player B is not in the network, return False
    return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)

def add_new_user(network, user, games):
    new_lst = []
    net = list_players(network)
    if user not in net:         #if player isn't already in the network, add them
        new_lst.append(user)
        new_lst.append([])      #append an empty list, because new player has no connections (yet)
        new_lst.append(games)
        network.append(new_lst)    #append list with new player, empty list of connections and list of games to the network
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    second_connections = []
    players = list_players(network)
    if user not in players:            #if the player is not in the network, return None
        return None
    else:
        for entry in network:
            if entry[0] == user:         #if player is in network, find his connections
                first_connections = entry[1]
                if len(first_connections) > 0:
                    for friend in first_connections:          #for each connection/friend, in player's first connections, find their connections
                        for j in network:                     #find each connection/friend, of player's first connections, in the network
                            if j[0] == friend:                #find their (friends) connections and append them to the list second_connections
                                if len(j[1]) > 0:              #create a list of all connections of each player A's friend
                                    for k in j[1]:             #for each player in friend's connections, see if he/she already is in second connections
                                        if k not in second_connections:     #if he/she is not in second connections, append him/her
                                            second_connections.append(k)
                                #else:              #if there are no connections, skip it and go to next connection
                                    #skip
                    #if len(second_connections) == 1:
#                        return second_connections[0]
                    return second_connections
                #if player doesn't have first connections, return an empty list
                return []

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.

def count_common_connections(network, user_A, user_B):
    players = list_players(network)
    if user_A not in players or user_B not in players:      #see if both players exist in the network, if not return False
        return False
    else:
        count = 0
        connection_A = get_connections(network, user_A)     #get player A's first connections
        connection_B = get_connections(network, user_B)     #get player B's first connections
        for i in connection_A:         #for each connection/friend in player A's connections, look if it is also in player B's connections
            if i in connection_B:
                count = count + 1      #if connection/friend is in both connections, then count it
        return count
# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
path = []

def find_path_to_friend(network, user_A, user_B):
    players = list_players(network)
    if user_A not in players or user_B not in players:   #if both players are not in the network, return None
        return None
    else:
        if user_A in path:      #if player A is in list path, it means that we already checked him and we can move to next player
            return None
        #if player A is not in list path, add him
        path.append(user_A)      
        if user_A == user_B:     #check if both players are the same
            return path
        else:
            final_path = []
            first_connect = get_connections(network, user_A)        #get first connections of player A and look if player B is in there
            if user_B in first_connect:
                return [user_A, user_B]       #if player B is in player A's connections, it means we are done, return a list with both players
            #if user_B is not in first_connect
            for entry in first_connect:     #if player B is not in player A's connections, find connections for each player in player A's connections (new path)
                new_path = find_path_to_friend(network, entry, user_B)
                if new_path != None:    #if we find a path to end player B, add this path to player A 
                    final_path = [user_A] + new_path
    if len(final_path) > 0 :    #if we find the path to player B, finish by returning the whole path
        return final_path
    return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# common_games(network, user_A, user_B):: 
#   Finds games that user_A and user_B have in common.

# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   A list of all games they have in common.
#   If user_A or user_B is not in network, return False.

def common_games(network, user_A, user_B):
    players = list_players(network)             #list of all players in the network
    common_games = []
    if user_A in players and user_B in players:    #check if both players exist in the network
        games_A = get_games_liked(network, user_A)    #games user_A likes to play
        games_B = get_games_liked(network, user_B)    #games user_B likes to play
        for game in games_B:                   #compare games: for each game of user_B, see if user_A is also playing
            if game in games_A:                #for each game they have in common, append it to the list common_games
                common_games.append(game)
    if len(common_games) > 0:                  #if players have any games in common, return common_games, else return None
        return common_games
    return None


net = create_data_structure(example_input)
#print net
#print (get_connections(net, "John"))
#print (get_connections(net, "Walter"))
#print (get_games_liked(net, "Debra"))
#print (add_connection(net, "Lev", "Levi"))
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print (get_secondary_connections(net, "Deb"))
#print (count_common_connections(net, "John", "Mercedes"))
print (find_path_to_friend(net, "John", "Mercedes"))
#print (common_games(net, "John", "John"))

