import json
from requests import request, HTTPError
from linux_profile.config.base import Config
from linux_profile.config import URL_API


class BaseRequest(Config):
    """Base class request
    """

    def start(self):
        """
        """
        self.path = URL_API
        self.load_config()
        self.setup_request()

    def url(self):
        """Url
        """
        self.url = self.path

    def header(self):
        """Header
        """
        self.header = {
            'email': self.user.get("email"),
            'x-token': self.user.get("token"),
            'Content-Type': 'application/json'
        }

    def setup_request(self):
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
                 url: str = None,
                 id: str = None) -> request:
        """Make GET
        """
        if not url:
            url = self.url

        if id:
            url = "{url}/{id}".format(
                url=url,
                id=id
            )

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
