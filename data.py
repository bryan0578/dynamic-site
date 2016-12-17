'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''

#I created a data object to hold data
class TShirts(object):
    #This is the constructor function that initializes the class
    def __init__(self):
        self.id = ''
        self.name = ''
        self.size = ''
        self.img = ''
        self.description = ''
        self.price = ''
        self.final_price = ''


#Created a class of data that use the data object
class Shirt(object):
    #This is the constructor function that initializes the class
    def __init__(self):
        #This is the first instance of the TShirts class
        woman = TShirts()
        #I created data that will use the data object
        woman.id = 'victorian_woman'
        woman.name = 'Victorian Woman'
        woman.size = '<select><option>Xs</option><option>Sm</option><option>Med</option><option>Lg</option><option>XL</option><option>XXL</option></select>'
        woman.img = 'images/bts-woman.png'
        woman.description = 'Black shirt with a victorian woman in a dress and umbrella and a skull face. This shirt is pres-hrunk and is machine washable.'
        woman.price = '$15'
        woman.final_price = '$7.50'

        #This is my second instance of the the TShirts data object
        skull = TShirts()
        #I created a second set of data that will use the data object
        skull.id = 'metal_skull'
        skull.name = 'Metal Skull'
        skull.size = '<select><option>Xs</option><option>Sm</option><option>Med</option><option>Lg</option><option>XL</option><option>XXL</option></select>'
        skull.img = 'images/bts-fire.png'
        skull.description = 'Black shirt with a stretched bloody skull with fangs. This shirt is for the extreme metal heads. '
        skull.price = '$15'
        skull.final_price = '$7.50'

        #This is my third instance of the TShirts class
        three_b = TShirts()
        #Here I created a third set of data for the data object
        three_b.id = "three_b"
        three_b.name = "Three B's"
        three_b.size = '<select><option>Xs</option><option>Sm</option><option>Med</option><option>Lg</option><option>XL</option><option>XXL</option></select>'
        three_b.img = 'images/bts-3b.png'
        three_b.description = 'Black shirt with orange and grey background, with Beneath the Sky logo on the back on top of a pile of skulls.'
        three_b.price = '$15'
        three_b.final_price = '$7.50'

        #This is my fourth instance of the TShirts class
        f_bomb = TShirts()
        #I created a fourth set of data for the data object
        f_bomb.id = "f_bomb"
        f_bomb.name = 'F-Bomb'
        f_bomb.size = '<select><option>Xs</option><option>Sm</option><option>Med</option><option>Lg</option><option>XL</option><option>XXL</option></select>'
        f_bomb.img = 'images/bts-fshirt.png'
        f_bomb.description = 'Black shirt with Blue and purple background, following the traditional "F-Bomb shirts many metal bands are using today but with a little twist.'
        f_bomb.price = '$15'
        f_bomb.final_price = '$7.50'

        #This is my fifth instance of the TShirts class
        hood = TShirts()
        #I created a fifth set of data for the data object
        hood.id = 'hoody'
        hood.name = 'Respect for the Dead'
        hood.size = '<select><option>Xs</option><option>Sm</option><option>Med</option><option>Lg</option><option>XL</option><option>XXL</option></select>'
        hood.img = 'images/bts-hoody.png'
        hood.description = 'One of the most popular is the Beneath the Sky hoodie featuring a line from the song Respect for the Dead on the hood.'
        hood.price = '$55'
        hood.final_price = '$35'

        #since I used variables instead of attributes they are not accessible outside of the class
        #Here I created an attribute that will hold all of the variables in an array
        #This makes the variables accessible outside of the class
        self.shirts = [woman, skull, three_b, f_bomb, hood]

        #All of the data created here will be used by to fill in the content portion of the pages
        #I created five sets of data for the data object so I will have five different pages
        #All information here was taken created by me
        #The images used were taken from my band.


















