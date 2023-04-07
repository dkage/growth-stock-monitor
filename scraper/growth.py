from bs4 import BeautifulSoup as bSoup
import requests


def get_product():
    """
    :return:
    """

    base_url = "https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931"
    base_url = "https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0',
        'content-type': 'text/html; charset=UTF-8'
    }

    http_return = ''
    try:
        print('getting from {}'.format(base_url))
        http_return = requests.get(base_url, headers=headers)
    except requests.exceptions.ConnectTimeout:
        print("HTTP request timed out for url {}".format(base_url))
    except requests.exceptions.ConnectionError:
        print("HTTP request failed for url {}".format(base_url))

    print('here')
    if http_return == '':
        return False

    try:
        if http_return.content is None:
            raise ValueError
    except ValueError:
        print('The http_return came back blank GET has failed without connection errors. Needs investigation.')
        return 1

    soup = bSoup(http_return.content, 'html.parser')

    print(soup)

    

#     product overview = section -> class: topoDetalhe
#     price = span -> class: topoDetalhe-boxRight-precoDe show-for-large
#     buy =  div -> class: botao-de-compra

get_product()