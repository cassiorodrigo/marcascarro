import requests
from bs4 import BeautifulSoup
import pprint
import os


class Pesquisa:
    def __init__(self, marca):

        self.marca = marca
        # self.loader()
        # resultado = requests.get(f"https://www.google.com/search?q={marca}")
        # soup = BeautifulSoup(resultado.content, "html.parser")
        # print(soup)
        # self.writer(soup.contents)

    def writer(self, soup):
        path_to_file = "dados/"
        file = "pesquisa.html"
        if os.path.exists(path_to_file):
            if os.path.exists(f"{path_to_file}/{file}"):
                with open(f"{path_to_file}/{file}", "w") as file:
                    file.write(soup)
            else:
                with open(f"{path_to_file}/{file}", "x") as file:
                    file.close()
        else:
            os.mkdir(path_to_file)

    def get_links(self):
        path_to_file = "dados/"
        with open(f"{path_to_file}/pesquisa{self.marca}.html") as file:
            soup = BeautifulSoup(file.read())
            links = soup.find_all("a", href=True)
            # for link in links:
                # print(link.get('href'))
            return [link.get('href') for link in links]

    def unique_links(self):
        links = self.get_links()[1:]
        stringlist = ''.join(links)
        # for e in links:
        #     if 'google' not in e:
        #         print(e)
        ulink = filter(lambda x: True if 'google' not in x and 'ferrari.com' not in x else False, links)
        return ulink


class CadaPagina(Pesquisa):
    def __init__(self, marca):
        super().__init__(marca)

    def acessar_pesquisa(self):
        for resultado in self.unique_links():
            res = requests.get(resultado)
            yield res.text

    def sentimento_da_pagina(self):
        for html in self.acessar_pesquisa():
            pass
            # processar html aqui


class DeterminarSentimento(CadaPagina):
    def __init__(self, marca):
        super().__init__(marca)
        self.links = self.acessar_pesquisa()
        for _ in self.links:
            print(self.links.__next__())


if __name__ == "__main__":
    p = DeterminarSentimento("ferrari").unique_links()