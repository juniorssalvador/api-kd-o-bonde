from flask_sqlalchemy import BaseQuery


class PersistenceUtil:

    @staticmethod
    def query(model) -> BaseQuery:
        return model.query
