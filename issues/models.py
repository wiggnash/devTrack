from abc import ABC, abstractmethod
class BaseEntity(ABC):
    @abstractmethod
    def validate():
        pass

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

class Issue(BaseEntity):
    def __init__(self, id, title, description, status, priority, reporter_id):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id

    def validate(self):
        pass
