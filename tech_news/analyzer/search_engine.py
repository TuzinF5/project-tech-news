# Requisito 6
from tech_news.database import find_news


def search_by_title(title):
    notices = find_news()
    response = []

    for notice in notices:
        if title.upper() in notice["title"].upper():
            response.append((notice["title"], notice["url"]))

    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    notices = find_news()
    response = []

    for notice in notices:
        if category.upper() in notice["category"].upper():
            response.append((notice["title"], notice["url"]))

    return response
