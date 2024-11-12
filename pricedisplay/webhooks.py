# -*- coding: UTF-8 -*-

import requests
from .exceptions import MissingOptionError

__version__ = '0.7.0'

class WebHook:
    """Class for making webhook requests"""

    def __init__( self, options ):
        try:
            self._baseUrl = options['webhook.url']
            self._highMessage = options['webhook.high']
            self._lowMessage = options['webhook.low']
            self._highTrigger = options['webhook.highTrigger']
            self._lowTrigger = options['webhook.lowTrigger']
        except KeyError as err:
            raise MissingOptionError( err.args )
    
        self._ShouldRunWebhook(self, now, prices)

    def _MakeRequest( self, url, message ):
        content = {'message': message}
        response = requests.post(url, json = content)

    # Check if the webhook should be run
    def check( self, now, prices ):
        # Webhook should be run if price for last hour is below the high trigger
        # but price for this hour is above it
        if prices[-2] < self._highTrigger and prices[-1] >= self._highTrigger:
            self._MakeRequest(self._baseUrl, self._highMessage + " Value is now " + str(prices[-1]))
        elif prices[-2] > self._lowTrigger and prices[-1] <= self._lowTrigger:
            self._MakeRequest(self._baseUrl, self._lowMessage + " Value is now " + str(prices[-1]))