import json

from requests import request, HTTPError
from linux_profile.base import BaseProfile
from linux_profile.config import URL_API


class BaseRequest(BaseProfile):
    """Base class request
    """

    def __init__(self) -> None:
        """Construct
        """
        self.path = URL_API
        self.load_config()
        self.setup()

    def url(self):
        """Url
        """
        self.url = self.path

    def header(self):
        """Header
        """
        self.header = {
            'Content-Type': 'application/json'
        }

    def setup(self):
        """Initial setup
        """
        try:
            self.url()
            self.header()

        except Exception as error:
            print(error)
            raise ValueError("Unable to mount the request.")

    def make_request(self,
                     method: str,
                     params: dict = {},
                     payload: dict = {},
                     header: dict = None,
                     url: str = None) -> request:
        """Make Request
        """
        payload = json.dumps(payload)

        kwargs = {
            'method': method,
            'params': params,
            'data': payload,
            'headers': header or self.header,
            'url': url or self.url
        }

        with request(**kwargs) as response:
            try:
                response.raise_for_status()

            except HTTPError as error:
                print(error)
                # raise ValueError("Failed to make the request")

            return response

    def make_get(self,
                 params: dict = {},
                 url: str = None) -> request:
        """Make GET
        """
        result = self.make_request(
            method='GET',
            params=params,
            url=url
        )

        return result

    def make_post(self,
                  payload: dict,
                  header: dict = None,
                  url: str = None) -> request:
        """Make POST
        """
        result = self.make_request(
            method='POST',
            header=header,
            payload=payload,
            url=url,
        )

        return result

    def make_put(self,
                 payload: dict,
                 header: dict = None,
                 url: str = None) -> request:
        """Make PUT
        """
        result = self.make_request(
            method='PUT',
            header=header,
            payload=payload,
            url=url,
        )

        return result

    def make_delete(self,
                    header: dict = None,
                    url: str = None) -> request:
        """Make DELETE
        """
        result = self.make_request(
            method='DELETE',
            header=header,
            url=url,
        )

        return result
