import webapp2
import urllib2
import json

from config import config

class ServiceHandler(webapp2.RequestHandler):
    def get(self, service_name):
        self.response.headers['Content-Type'] = 'text/plain'

        service_url = config.URLS[service_name]
        response_code = urllib2.urlopen(service_url).getcode()

        obj = {
            'name': service_name,
            'url': service_url,
            'status': response_code
        }

        self.response.write(json.dumps(obj));
