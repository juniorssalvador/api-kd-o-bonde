import requests
from bs4 import BeautifulSoup
from app import db


def _get_id_itinerario(sentido=None, identi_linha=None):
    id = db.engine.execute(
        "select it.id from kd_o_bonde.itinerario it join kd_o_bonde.linha li on it.linha_id = li.id where it.sentido = '{0}' and li.identificacao_linha = '{1}'".format(
            sentido, identi_linha))

    for a in id:
        return a[0]


def _process_linhas(soup_params):
    for i in range(2, 100):
        try:
            corpo = soup_params.select(f"#Blog1 > div.blog-posts.hfeed > div:nth-child(1) > div > div:nth-child({i})")
            linha_title = corpo[0].h3.a.get_text()
            infos = corpo[0].find(itemprop="description articleBody").find_all("span")

            ida_list = str(corpo[0].find(itemprop="description articleBody").get_text()).split("\n")[1].split(",")
            volta_list = infos[0].get_text().split(",")

            idIti = _get_id_itinerario(sentido="IDA", identi_linha=linha_title.replace(" ", "").replace(":", "")[5:8])
            contador = 0
            for ida in ida_list:
                if not ida.strip(" ").__contains__("Sentido"):
                    if idIti is not None:
                        print("{0},{1},{2}".format(idIti, ida.strip(" "), contador))
                        contador += 1

            idIti = _get_id_itinerario(sentido="VOLTA", identi_linha=linha_title.replace(" ", "").replace(":", "")[5:8])
            contador = 0
            for volta in volta_list:
                if not volta.strip(" ").__contains__("Sentido"):
                    if idIti is not None:
                        print("{0},{1},{2}".format(idIti, volta.strip(" "), contador))
                        contador += 1

            if idIti is not None:
                idIti = _get_id_itinerario(sentido="TERMINAL",
                                           identi_linha=linha_title.replace(" ", "").replace(":", "")[5:8])

                print("{0},{1},{2}".format(idIti, infos[2].get_text(), 0))

            # print(infos)

        except:
            break


page = requests.get(
    "http://rotadosonibus.blogspot.com/search?updated-max=2022-10-29T10:07:00-07:00&max-results=300&start=123&by-date"
    "=false")
soup = BeautifulSoup(page.content, 'html.parser')

_process_linhas(soup_params=soup)

page = requests.get(
    'http://rotadosonibus.blogspot.com/search?updated-max=2009-10-29T10:07:00-07:00&max-results=300&start=226&by-date'
    '=false')
soup = BeautifulSoup(page.content, 'html.parser')

_process_linhas(soup_params=soup)
