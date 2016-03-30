### timX Microservices Monitoring

This services monitors all the timX microservices by pinging each of the microservice every hour

The microservices currently monitored is below:
 - guruguru
 - hokaidotrip2015

The main page will summarise the current status of every microservice
 -  [timx-monitoring.appspot.com](http://timx-monitoring.appspot.com)

This application is built using
  - webapp2

and it is hosted in Google App Engine (GAE)

#### Deployment Procedure

To debug in localhost
```
dev_appserver.py .
```

To deploy to GAE server
```
appcfg.py -A timx-monitoring -V v1  update .
```

To update cron tasks in production server
```
appcfg.py update_cron
```
