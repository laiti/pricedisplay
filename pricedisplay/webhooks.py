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
            self._lowMessage = options['webhook.log']
        except KeyError as err:
            raise MissingOptionError( err.args )
    
        self._ShouldRunWebhook(self, now, prices)

    def _MakeRequest( self, url, message ):
        content = {'message': message}
        response = requests.post(url, json = content)

    def check( self, now, prices ):


