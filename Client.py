import requests
import logging
import os
import simplejson
import json


def j_print(d):
    print(json.dumps(d, indent=4))


class Client:
    """
    To construct an API client the following keywords must be specified:
        email, password
        OR
        access_token
    The following keywords are optional:
        url - the location of the endpoint
            default "https://app-dashboard-api.trakglobal.co.uk/"
        verbosity - default 1, can be overridden by env variable LOG_LEVEL
            0 - Critical
            1 - Error
            2 - Warning
            3 - Info
            4 - Debug
    """

    def __init__(self, email=None, password=None,
                 url="https://app-dashboard-api.trakglobal.co.uk/",
                 access_token=None,
                 verbosity=1):
        """ Constructor for API Client."""

        # Logging configuration
        verbosity_levels = {
            0: logging.CRITICAL,
            1: logging.ERROR,
            2: logging.WARNING,
            3: logging.INFO,
            4: logging.DEBUG
        }
        log = logging.getLogger("123GO-python")
        log_format = "%(asctime)s\t%(levelname)s:%(name)s:%(message)s"
        logging.basicConfig(level=os.environ.get("LOG_LEVEL",
                                                 verbosity_levels[verbosity]),
                            format=log_format,
                            datefmt='%d-%b-%y %H:%M:%S')
        self.api_url = url
        if access_token:
            log.debug("Created client using access token")
            self._access_token = access_token
        elif email and password:
            if not all(map(lambda x: type(x) == str, (email, password))):
                log.error("Invalid value type(s) given for credentials")
                raise TypeError
            log.debug("Credentials accepted as valid.")
            login_params = {"grant_type": "password", "username": email,
                            "password": password, "platform": "Android+1.0.1"}

            def bad_response():
                log.error("Unexpected response, check credentials are correct")
                exit(1)

            try:
                response = requests.post(
                    self.api_url + "login", data=login_params)
                log.debug("Received response:\n" + response.text)
                response_json = response.json()
            except requests.exceptions.ConnectionError:
                log.error("Connection error occurred")
                exit(1)
            except simplejson.errors.JSONDecodeError:
                bad_response()

            if "access_token" not in response_json:
                bad_response()

            log.info("Successfully parsed response as JSON:\n{}"
                     .format(j_print(response_json)))

            self._access_token = response_json['access_token']
        else:
            log.error("No credentials supplied, you must provide "
                      "either an access token or an email/password pair")
            # @TODO (Better exception type needed)
            raise ValueError
        self._request_header = {'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(
                                    self._access_token)}

    def make_request(self, endpoint):

        return requests.post(self.api_url + endpoint,
                             headers=self._request_header).json()

    def make_get_request(self, endpoint, params):
        return requests.get(self.api_url + endpoint, params=params,
                            headers=self._request_header).json()
