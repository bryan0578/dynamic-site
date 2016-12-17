'''
Bryan Cash
1/21/2015
DPW
Reusable Library
'''


# Reusable library classes
# Reusable library class called FavoriteGame
class FavoriteGame(object):
    # Constuctor function
    def __init__(self):
        # Empty array to store information from the data object
        self.__games_list = []

    # Function to add games to the empty array
    def add_game(self, g):
        # Appends a game to the game array
        self.__games_list.append(g)
        # tested to make sure it is working
        # print g.game

    # Set up a method to compile the list of items in the array
    def compile_list(self):
        # Set up the output to an empty string to hold the return information
        output = ''
        # Looped through the array of games and compiled a list
        for game in self.__games_list:
            # Information to be used in html code for the list
            output += '<div class="results1">' + game.game
            + '<div class="results4"> ' + game.players + '</div>'
            + '</di><div class="results2"> ' + game.i
            + '</div><div class="results3">' + str(game.s) + '</div>'
        # Return the output to be printed to screen
        return output

    '''Set up a calculation to keep track of the user's high score this
    calculation will give the average high score'''
    def calc_average(self):
        # Set up an empty array to hold the information for the calculation
        s = []
        # Loop to cycle through the list of game to pull out all the scores
        for game in self.__games_list:
            # Put all of the scores into the empty array
            s.append(game.s)
        # Variable num and set it the leangth of the array
        num = len(s)
        # Variable to to hold the sum of all the scores in the array
        total_sum = sum(s)
        # Varaible to hold the average calculation
        average = total_sum/num
        # Return string with score converted to a string
        return '<div id="average">Your average high schore is '
        + str(average) + '</div>'


# Data object
class HighScores(object):
    # Constuctor function
    def __init__(self):
        '''Blueprint for the information from both hardcoded and the
        request.GET information'''
        self.game = ''
        # Score input is treated as integer for average calculation
        self.__score = int()
        self.__initials = ''
        self.players = ''

    # Getter and setter for both scores and initials
    @property
    # Method for getter for score
    def score(self):
        return self.__score

    # Method for setter for score
    @score.setter
    def score(self, s):
        self.score = s

    # Method for getter for initials
    @property
    def initials(self):
        return self.__initials

    # Method for setter for initals
    @initials.setter
    def initials(self, i):
        self.initials = i
