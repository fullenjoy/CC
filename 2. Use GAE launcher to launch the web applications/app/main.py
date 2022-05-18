# Open cloud sdk shell and type
# google-cloud-sdk\bin\dev_appserver.py "C:\Users\Harshsk\Desktop\CC\CC Fullenjoy\1. Google Engine(Hello world)\app"
# Now open browser and enter
# localhost:8000
# or go live on vs
import os
import json
import urllib
import google.appengine.ext.webapp
import webapp2
import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out
        write(template.render(path, template_values))
        app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
