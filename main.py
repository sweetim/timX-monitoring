import webapp2
import urllib2

from controller import home, service

app = webapp2.WSGIApplication([
    ('/', home.HomeHandler),
    ('/service', service.ServiceHandler)
], debug = True);    