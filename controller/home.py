import webapp2
import os

from google.appengine.ext.webapp import template

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../views' ,'home.html')

        self.response.headers['Content-Type'] = 'text/html'

        obj = {
            'statuses': [
                { 'name': 'hokaido', 'status': 'OK' },
                { 'name': 'web', 'status': 'OK' }
            ]
        }



        self.response.write(template.render(path, obj));
