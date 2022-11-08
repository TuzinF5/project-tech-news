import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_urls = selector.css(".cs-overlay-link::attr(href)").getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    notice = dict()

    selector = Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    notice["url"] = url

    title = selector.css(".entry-title::text").get()

    if title.endswith(" "):
        title = title[:-1]

    if title.endswith("\xa0\xa0\xa0"):
        title = title[:-3]

    notice["title"] = title

    timestamp = selector.css(".meta-date::text").get()
    notice["timestamp"] = timestamp

    writer = selector.css(".url.fn.n::text").get()
    notice["writer"] = writer

    comments_count = selector.css(".comment-body").getall()
    notice["comments_count"] = len(comments_count)

    tags = selector.css("a[rel='tag']::text").getall()
    notice["tags"] = tags

    category = selector.css(".category-style span.label::text").get()
    notice["category"] = category

    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()

    summary = "".join(summary)

    if summary.endswith(" ") or summary.endswith("\xa0"):
        summary = summary[:-1]

    notice["summary"] = summary

    return notice


# Requisito 5
def get_tech_news(amount):
    website_content = fetch("https://blog.betrybe.com")
    next_page_link = ""
    all_news_from_the_site = []

    while next_page_link is not None:
        if len(all_news_from_the_site) >= amount:
            break

        all_news_from_the_site.extend(scrape_novidades(website_content))
        next_page_link = scrape_next_page_link(website_content)
        website_content = fetch(next_page_link)

    all_news_from_the_site = all_news_from_the_site[:amount]

    notices = []
    for notice in all_news_from_the_site:
        website_content = fetch(notice)
        notices.append(scrape_noticia(website_content))

    create_news(notices)

    return notices
