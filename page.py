'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''

#created a page class to hold the universal html code that will be apart of every page
#this will become a super class
class Page(object):
    #constructor function that initializes the class
    def __init__(self):
        #here I created the beginning portion of the html code with the _head attribute
        self._head = '''

<!DOCTYPE HTML>
<html>
    <head>
        <title>Python WebStore</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/normalize/4.1.1/normalize.min.css" rel="stylesheet" />
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
        <link href='https://fonts.googleapis.com/css?family=Cardo:400,400italic,700' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        #This holds the part of the body html code that will be apart of every page
        self._body = '''
        <nav class="navbar navbar-inverse">
          <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">PYTHONwebstore.com</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">

              <form class="navbar-form navbar-left" role="search">

                  <div class="input-group">
                    <input class="form-control" name="fields[]" type="text" placeholder="Search for something" />
                      <span class="input-group-btn">
                        <button class="btn btn-info btn1" type="button"><span class="glyphicon glyphicon-search"></span></button>
                      </span>
                  </div>


              </form>
              <ul class="nav navbar-nav navbar-right">
                <li><a href="#">HISTORY</a></li>
                <li><a href="#">YOUR ACCOUNT</a></li>
                <li><a href="#"><span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span></a></li>
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
        </nav>

        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-3 col-md-2 sidebar">
                    <h2>BENEATH THE SKY</h2>
                    <ul class="nav nav-sidebar">
                        <li class="active"><a href="?id=victorian_woman">Victorian Woman</a></li>
                        <li><a href="?id=three_b">The Three B's</a></li>
                        <li><a href="?id=metal_skull">Metal Skull</a></li>
                        <li><a href="?id=f_bomb">F-Bomb</a></li>
                        <li><a href="?id=hoody">The Hoody</a></li>
                    </ul>
                </div>




        '''
        #This holds the closing html tags
        self._close = '''
    </body>
</html>'''

    #this is the method used to print out the basic structure of the page without the content pages
    def print_out(self):
        return self._head + self._body + self._close


#here I created a class that inherits from the page class making the page class a super class
#I used the Page object to show that the ContentPage will inherit from the Page class
class ContentPage(Page):
    #This is the constructor function that will initialize the class
    def __init__(self):
        #here is the constructor for the super class
        super(ContentPage, self).__init__()

        #this is where I set up the place where the content will be and a number for the array
        #this is a private attribute so a getter and setter will be needed
        self.__list_content = ''
        self.num = 0

        #Here I set up the part of the html that will be at the beginning of the content
        self.content_head = '''

           <div class="col-sm-9 col-md-10">
                <div class="content">
                    <h3>About This Product</h3>
            '''
        #This is the html code that will be incorporated with the content from the data objects to create the content
        #This and the information from the data objects will create the content pages
        self.content_name = '<p><strong>Name: </strong>'
        self.content_size = '<br /><p><strong>Sizes: </strong>'
        self.content_img = '<div id="img"><img src="'
        self.content_img2 = ' "width="300"></div>'
        self.content_description = '<strong>Description: </strong>'
        self.content_price = '</br></br><strong>Original Price: </strong>'
        self.content_sale = '</br></br><strong>Sale Price: </strong>'
        self.content_button ='</br></br><button class="btn btn-primary"><span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> Add to Cart</button>'
        self.content_close = '</p></div></div></div></div>'

    #this is the where I created a setter for the private attribute __list_content
    #this will make it readable
    @property
    #this is the method to read the attribute
    def content(self):
        #here is where it is returned
        return self.__list_content

    #here I created a setter this will make the private attribute writeable so that we can change it
    @content.setter
    #here I set up the method to pull the attribute and an array
    def content(self, arr):
        #here is where the array will be located
        self.content = arr
        #this for loop will loop through the array and get the content by the item in each array
        for item in arr:
            self.__list_content += item[self.num]

    #This is the method that will override the previous print out method through polymorphism and return all of the content separated by the arrays
    #This will allow me to pull the information from each array independently creating 5 different content pages.
    def print_out(self):
        return self._head + self._body + self.content_head + self.content_name + self.data.name + self.content_size + self.data.size + self.content_img + self.data.img + self.content_img2 +self.content_description + self.data.description + self.content_price + self.data.price + self.content_sale + self.data.final_price + self.content_button + self.content_close + self._close






