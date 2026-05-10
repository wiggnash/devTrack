import json
from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @abstractmethod
    def validate():
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

    @classmethod
    def generate_id(cls, data):
        return len(data) + 1

    @classmethod
    def read_all(cls, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    @classmethod
    def save_all(cls, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file)
