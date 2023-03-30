from app.repositories.book_repository_postgre import BookRepositoryPostgre


class BookUseCase:
    def __init__(self):
        self.book_repository = BookRepositoryPostgre()

    def get_all(self):
        return self.book_repository.get_all()

    def get_by_id(self, id):
        return self.book_repository.get_by_id(id)

    def add(self, book_in):
        return self.book_repository.add(book_in)

    def update(self, book_in, id):
        return self.book_repository.update(book_in, id)

    def delete(self, id):
        return self.book_repository.delete(id)
