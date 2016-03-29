import webapp2
import urllib2

DEFAULT_SERVICE_NAME = ''

class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        service_name = self.request.get('hokaido-trip', DEFAULT_SERVICE_NAME)
        
        self.response.headers['Content-Type'] = 'text/plain'
        
        code = urllib2.urlopen('http://hokaidotrip2015.azurewebsites.net/').getcode()
        
        self.response.write(service_name);