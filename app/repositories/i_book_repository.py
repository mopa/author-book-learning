from abc import ABC, abstractmethod


class IBookRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add(self, book):
        pass

    @abstractmethod
    def update(self, book):
        pass

    @abstractmethod
    def delete(self, id):
        pass
