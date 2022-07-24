from linux_profile.actions.base import BaseAction

class Init(BaseAction):
    """Start of settings
    """

    def connect_user(self):
        """Connect User
        """
        raise("Ops")

    def get_profile(self) -> bool:
        """Get list of registered profiles
        """
        return True

