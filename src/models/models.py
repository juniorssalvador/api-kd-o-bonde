from flask_sqlalchemy import SQLAlchemy
from importe_db import app
from config import Config
from util.json_util import JsonUtil

db = SQLAlchemy(app)


class Linha(db.Model):
    __table_args__ = Config.tbl_args

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    identificacao_linha = db.Column(db.Integer)
    onibus_list = db.relationship('Onibus', backref='linha', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "onibus_list": JsonUtil.instrumented_list_to_json(self.onibus_list)
        }


class Onibus(db.Model):
    __table_args__ = Config.tbl_args

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    numero = db.Column(db.Integer)
    lotacao = db.Column(db.Integer)
    linha_id = db.Column(db.Integer, db.ForeignKey(f'{Config.tbl_args.get("schema")}.linha.id'),
                         nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "numero": self.numero,
            "lotacao": self.lotacao,
            "linha_id": self.linha_id
        }
