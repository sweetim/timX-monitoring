import webapp2
import urllib2

from controller import home, service

app = webapp2.WSGIApplication([
    ('/', home.HomeHandler),
    webapp2.Route('/service/<service_name>', handler = service.ServiceHandler)
], debug = True);
