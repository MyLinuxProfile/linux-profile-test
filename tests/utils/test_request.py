from linux_profile.utils.request import BaseRequest

class Request(BaseRequest):

    def url(self):
        """Url
        """
        self.url = "https://linuxprofile.com/"

def test_meke_get():
    request = Request()
    response = request.make_get()

    assert response.status_code == 200
