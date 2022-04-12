from flask import request
from flask import Blueprint, make_response, jsonify

from src.util.json_util import JsonUtil
from src.util.persistence_mxns import PersistenceUtil

onibus_controller = Blueprint('onibus_controller', __name__)


@onibus_controller.route('/onibus/', methods=["GET"])
@onibus_controller.route('/onibus/<id>', methods=["GET"])
def linhas():
    from src.models.models import Onibus

    response = make_response(JsonUtil().list_to_json(PersistenceUtil.query(Onibus).all()))
    response.headers['Content-Type'] = 'application/json'
    return response
