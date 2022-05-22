import requests
from bs4 import BeautifulSoup
from app import db

root = "https://moovitapp.com/index/pt-br/"


def _get_id_itinerario(identi_linha=None):
    id = db.engine.execute(
        "select it.id from kd_o_bonde.itinerario it join kd_o_bonde.linha li on it.linha_id = li.id where  li.identificacao_linha = '{0}'".format(
            identi_linha))

    for a in id:
        return a[0]


def get_page(url) -> BeautifulSoup:
    page = requests.get(url)
    soupP = BeautifulSoup(page.content, 'html.parser')
    return soupP


soup = get_page("https://moovitapp.com/index/pt-br/transporte_p%C3%BAblico-Belem-3183")

for empresa in soup.select("#agency-type-3")[0].find_all("li"):
    href = empresa.select("a")[0].get("href")
    if not str(href).startswith("http"):
        href = root + href

    empresaSOUP = get_page(str(href))
    empresa = get_page(str(href)).select("#agency-lines")

    if len(empresa) > 0:
        for emp in empresa:
            for li in emp.select("ul"):
                for a in li.select("a"):
                    numero_linha = a.select("div")[1].span.get_text()
                    nome_linha = a.select("div")[2].strong.get_text()

                    itinerario = get_page(a.get("href"))
                    pits = itinerario.select("#main-content > section.content-section.lines > div > "
                                             "div.first-column.info-wrapper.lines-wrapper > div.stops-wrapper > ul")[0]
                    id_linha = _get_id_itinerario(numero_linha)
                    contador = 0
                    for li in pits.select("li"):
                        if id_linha:
                            print("{0};{1};{2}".format(id_linha, li.div.h3.get_text() if li.div is not None else "",
                                                       contador))
                            contador += 1

    # else:

    # print("Linha Única #################################")
    # print(empresaSOUP.select("#main-content > section.hero-section.hero-line > "
    #                          "div > div > div > div > div > div "
    #                          "> img > h1")[0].get_text())
    #
    # for pit in empresaSOUP.select("#main-content")[0].select("ul"):
    #     for li in pit.select("li"):
    #         if li.div is not None:
    #             print(li.div.h3.get_text())
