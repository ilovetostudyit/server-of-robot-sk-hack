# Dialogflow - sample webhook implementation in Python

This is a really simple webhook implementation that gets Dialogflow classification JSON (i.e. a JSON output of Dialogflow /query endpoint) and returns a fulfillment response.

More info about Dialogflow webhooks could be found here:
[Dialogflow Webhook](https://dialogflow.com/docs/fulfillment)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a weather information fulfillment service that uses [Yahoo! Weather API](https://developer.yahoo.com/weather/).
The services takes the `geo-city` parameter from the action, performs geolocation for the city and requests weather information from Yahoo! Weather public API.

The service packs the result in the Dialogflow webhook-compatible response JSON and returns it to Dialogflow.
