from linux_profile.base import BaseProfile

class Init(BaseProfile):
    """Start of settings
    """
    def __init__(self, email: str, token: str):
        super().__init__(email, token)

    def connect_user(self):
        """Connect User
        """
        pass

    def get_profile(self) -> bool:
        """Get list of registered profiles
        """
        pass
