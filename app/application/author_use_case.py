from app.repositories.author_repository_postgre import AuthorRepositoryPostgre


class AuthorUseCase:
    def __init__(self):
        self.author_repository = AuthorRepositoryPostgre()

    def get_all(self):
        return self.author_repository.get_all()

    def get_by_id(self, id):
        return self.author_repository.get_by_id(id)

    def add(self, author_in):
        return self.author_repository.add(author_in)

    def update(self, author_in, id):
        return self.author_repository.update(author_in, id)

    def delete(self, id):
        return self.author_repository.delete(id)
