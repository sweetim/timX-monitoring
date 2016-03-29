import webapp2
import urllib2
import json
import os

from google.appengine.ext.webapp import template

from config import config

path = os.path.join(os.path.dirname(__file__), '../views' ,'home.html')

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        statuses = []

        for service_name in config.URLS.keys():
            service_url = self.request.url + 'service/' + service_name
            statuses.append(service_url)
            response = urllib2.urlopen(service_url)
            statuses.append(json.load(response))

        obj = {
            'statuses': statuses
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(path, obj));
