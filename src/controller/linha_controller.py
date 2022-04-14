from flask import request
from flask import Blueprint, make_response
from util.persistence_mxns import PersistenceUtil
from util.json_util import JsonUtil

linha_controller = Blueprint('linha_controller', __name__)


@linha_controller.route('/linhas/', methods=["GET"])
@linha_controller.route('/linhas/<id>', methods=["GET"])
def linhas(id=None):

    from models.models import Linha

    if id is None:
        response = make_response(JsonUtil().list_to_json(PersistenceUtil.query(Linha).all()))
    else:
        response = make_response(dict(PersistenceUtil.query(Linha).get(id).serialize()))

    response.headers['Content-Type'] = 'application/json'
    return response


@linha_controller.route('/linhas/', methods=["POST"])
def inserir_linhas():
    print(request.json)
    return "Ok"
