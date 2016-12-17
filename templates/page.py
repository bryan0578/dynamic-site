'''
Bryan Cash
1/21/2015
DPW
Reusable Library
'''


# Created Page object
class Page(object):
    # Constructor function that initializes the class
    def __init__(self):
        # Title attribute that contains the welcome text
        self.title = "Welcome!"
        # Created css attribute this points to the css file in html
        self.css = "css/styles.css"
        # Created head attribute
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        # Input view, this holds all the html for the form view
        self.input = '''
        <div id="head">
            <h1>High Score Tracker</h1>
            <p>Keep track of your high scores. Just enter the name of the game
 your high score your initials and select multiplayer or single player, hit add
 game and see all of your high scores</p>
        </div>
        <div id="form">
            <h2>Keep track of your High Scores</h2>
            <form method="GET">
                <div class="i">
                    <label>Name of Game: </label><input class="input"
type="text" name="game" /><br />
                </div>
                <div class="i">
                    <label>Your High Score: </label><input class="input"
 type="number" name="score" /><br />
                </div>
                <div class="i">
                    <label>Your Initials: </label><input class="input"
 type="text" name="initials" /><br />
                </div>
                <div class="i">
                    <label>Players: </label>
                        <select class="input" name="players">
                            <option>Single Player</option>
                            <option>Multiplayer</option>
                        </select><br />
                </div>
                <div id="button">
                    <input type="submit" value="Add Game" class="btn" />
                </div>
            </form>
        </div>'''
        '''Attribute that will hold the heading and beginning of a div
        container for the results view'''
        self.container_head = '''<h2>Here is your list of High Scores</h2>
        <div id="container">

        '''
        '''Results attribute I left this as an empty string so that the output
        from the library could fill it in'''
        self.results = ''
        # Closed the container div by making a container_close attribute
        self.container_close = '</div>'
        # Close attribute which will contain the ending html code
        self.close = '''
    </body>
<html>'''

    # Method to print all the html elements for the form view to the page
    def print_out(self):
        form_view = self.head + self.input + self.close
        form_view = form_view.format(**locals())
        return form_view

    # Method to print all of the html elements for the results view to the page
    def print_results(self):
        self.results = self.head + self.container_head + self.results
        + self.container_close + self.close
        self.results = self.results.format(**locals())
        return self.results
