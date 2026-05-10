from devtrack.models import BaseEntity

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name:
            raise ValueError("Name is Required")

        if "@" not in self.email:
            raise ValueError("Not a valid email")
