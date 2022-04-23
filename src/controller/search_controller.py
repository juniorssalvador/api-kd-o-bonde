from flask import Blueprint, make_response
from transfer_models.search_return import SearchModel
from util.json_util import JsonUtil
from util.persistence_mxns import PersistenceUtil

search_controller = Blueprint('search_controller', __name__)


@search_controller.route('/search/linha_or_pit/<query>', methods=["GET"])
def create_query(query):
    search_result = []

    data = PersistenceUtil.get_engine().execute("select l.*, pit.descricao from kd_o_bonde.linha l "
                                                "join kd_o_bonde.itinerario it on l.id = it.linha_id "
                                                "join kd_o_bonde.ponto_itinerario pit on it.id = pit.itinerario_id "
                                                "where upper(pit.descricao) like '%%{0}%%' or "
                                                "upper(l.name) like '{0}%%'"
                                                .format(query.upper(), query.upper()))

    for linha in data:
        sm = SearchModel(ident=linha[0], title=linha[1],
                         sub_title=linha[2], data=linha[3],
                         typee="Linha" if str(linha[1]).__contains__(query) else "Ponto")

        search_result.append(sm)

    response = make_response(JsonUtil().list_to_json(search_result))
    response.headers['Content-Type'] = 'application/json'
    return response
