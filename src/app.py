from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.controller.linha_controller import linha_controller
from src.controller.onibus_controller import onibus_controller

app.register_blueprint(linha_controller)
app.register_blueprint(onibus_controller)


@app.errorhandler(404)
def url_404(e):
    return 'not found'


app.register_error_handler(404, url_404)
if __name__ == '__main__':
    app.run(debug=True)
