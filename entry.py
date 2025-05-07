class Entry:
    def __init__(self, site:str, username:str, password:str):
        self.site = site
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password": self.password
        }

    def __repr__(self):
        return f"<Entry site='{self.site}' username='{self.username}'>"