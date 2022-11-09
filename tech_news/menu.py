import sys
from tech_news.scraper import get_tech_news


def analyzer_menu_get_tech_news():
    amount = input("Digite quantas notícias serão buscadas:")
    print(get_tech_news(int(amount)))


# Requisito 12
def analyzer_menu():
    displays_the_options = {
        "0": lambda: analyzer_menu_get_tech_news(),
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
    }

    options_answer = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    if options_answer == "7":
        print("Encerrando script")
        return

    try:
        displays_the_options[options_answer]()
    except KeyError:
        print(sys.stderr.write("Opção inválida\n"))
