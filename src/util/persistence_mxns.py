from flask_sqlalchemy import BaseQuery, SQLAlchemy
from importe_app import app


class PersistenceUtil:

    @staticmethod
    def query(model) -> BaseQuery:
        return model.query

    @staticmethod
    def get_engine():
        db = SQLAlchemy()
        return db.get_engine(app)
