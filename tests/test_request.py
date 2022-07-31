from tests.utils.api import start, stop
from linuxp.utils.request import BaseRequest


class Request(BaseRequest):

    def url(self):
        """Url
        """
        self.url = "http://0.0.0.0:8000/"

start()
request = Request()


def test_meke_get():
    response = request.make_get()
    assert response.status_code == 200


def test_meke_post():
    response = request.make_post(payload={})
    assert response.status_code == 201


def test_meke_put():
    response = request.make_put(payload={})
    assert response.status_code == 200


def test_meke_delete():
    response = request.make_delete()
    assert response.status_code == 200


stop()
