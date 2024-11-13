# -*- coding: UTF-8 -*-

import requests
from .exceptions import MissingOptionError

__version__ = '0.7.0'

class WebHook:
    """Class for making webhook requests"""

    def __init__( self, options ):
        try:
            self._baseUrl = options['webhook.url']
            self._toHighMessage = options['webhook.tohigh']
            self._toLowMessage = options['webhook.tolow']
            self._fromHighMessage = options['webhook.fromhigh']
            self._fromLowMessage = options['webhook.fromlow']
            self._highTrigger = options['webhook.highTrigger']
            self._lowTrigger = options['webhook.lowTrigger']
        except KeyError as err:
            raise MissingOptionError( err.args )

    def _MakeRequest( self, url, message ):
        content = {'message': message}
        response = requests.post(url, json = content)

    # Check if the webhook should be run
    def check( self, now, prices ):
        # Webhook should be run if price for last hour is below the high trigger
        # but price for this hour is above it
        price_now = prices[now.hour]
        price_prev = prices[now.hour - 1]
        if price_prev < self._highTrigger and price_now >= self._highTrigger:
            self._MakeRequest(self._baseUrl, self._toHighMessage + " Value is now " + str(price_now))
        elif price_prev > self._lowTrigger and price_now <= self._lowTrigger:
            self._MakeRequest(self._baseUrl, self._toLowMessage + " Value is now " + str(price_now))
        # Mention also if we go over low threshold or below high threshold
        elif price_prev < self._lowTrigger and price_now >= self._lowTrigger:
            self._MakeRequest(self._baseUrl, self._fromLowMessage + " Value is now " + str(price_now))
        elif price_prev > self._highTrigger and price_now <= self._highTrigger:
            self._MakeRequest(self._baseUrl, self._fromHighMessage + " Value is now " + str(price_now))