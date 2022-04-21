from flask_migrate import Migrate

from importe_db import app

from controller.linha_controller import linha_controller
from controller.onibus_controller import onibus_controller
from models.models import db, Onibus, PontoItinerario, Itinerario, Linha

app.register_blueprint(linha_controller)
app.register_blueprint(onibus_controller)
Migrate(app, db)


@app.errorhandler(404)
def url_404(e):
    return 'not found'


app.register_error_handler(404, url_404)
if __name__ == '__main__':
    app.run(debug=True)
