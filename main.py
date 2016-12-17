'''
Bryan Cash
1/28/2015
DPW
Dynamic Site
'''


import webapp2

#I imported the ContentPage class from the page.py file
from page import ContentPage
#Imported the Shirt class from the data.py file
from data import Shirt

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #I created an instance of Shirt
        s = Shirt()
        #I created an instance of Content Page
        cp = ContentPage()

        #started the conditional to handle the appropriate content
        if self.request.GET:
            #If the request.GET has an id that is equal to victorian_woman then the content page data will grab the matching information in the array and will print out the information using the print out method.
            if self.request.GET['id'] == "victorian_woman":
                cp.data = s.shirts[0]
                self.response.write(cp.print_out())
            #If the request.GET has an id that is equal to metal_skull then the content page data will grab the matching information in the array and will print out the information using the print out method.
            elif self.request.GET['id'] == "metal_skull":
                cp.data = s.shirts[1]
                self.response.write(cp.print_out())
            #If the request.GET has an id that is equal to three_b then the content page data will grab the matching information in the array and will print out the information using the print out method.
            elif self.request.GET['id'] == "three_b":
                cp.data = s.shirts[2]
                self.response.write(cp.print_out())
            #If the request.GET has an id that is equal to f_bomb then the content page data will grab the matching information in the array and will print out the information using the print out method.
            elif self.request.GET['id'] == "f_bomb":
                cp.data = s.shirts[3]
                self.response.write(cp.print_out())
            #If the request.GET has an id that is equal to hoody then the content page data will grab the matching information in the array and will print out the information using the print out method.
            elif self.request.GET['id'] == "hoody":
                cp.data = s.shirts[4]
                self.response.write(cp.print_out())
        #Otherwise it will print out the the fist set of data in the array
        else:
            cp.data = s.shirts[0]
            self.response.write(cp.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
