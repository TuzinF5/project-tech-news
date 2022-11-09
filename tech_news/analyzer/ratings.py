from tech_news.database import db


# Requisito 10
def top_5_news():
    notices = list(
        db.news.find(
            {},
            {
                "_id": False,
                "title": True,
                "url": True,
                "comments_count": True,
            },
        )
        .sort("comments_count", -1)
        .limit(5)
    )

    response = []

    for notice in notices:
        response.append((notice["title"], notice["url"]))

    return response


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
