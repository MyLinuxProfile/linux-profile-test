from linux_profile.base import BaseProfile

class Pull(BaseProfile):
    """Start of settings
    """
    def setup(self) -> None:
        """Initial setup
        """
        try:
            self.load_config()
        except Exception as error:
            print(error)
            raise ValueError("It is not possible to load the basic settings.")

    def test(self):
        print("----")
