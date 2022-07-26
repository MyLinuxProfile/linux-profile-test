from linux_profile.base import BaseProfile

class Push(BaseProfile):
    """Start of settings
    """
    def setup(self) -> None:
        """Initial setup
        """
        try:
            self.load_config()
            self.load_profile()
        except Exception as error:
            print(error)
            raise ValueError("It is not possible to load the basic settings.")

    def test(self):
        print("----")
