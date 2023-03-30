from abc import ABC, abstractmethod


class IAuthorRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add(self, author):
        pass

    @abstractmethod
    def update(self, author, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass
