# -*- coding: utf-8 -*-

import requests
import bs4
import dateparser


def fetch_habr_feed(pages=5):
    raw_pages = []
    for page_number in range(pages):
        raw_pages.append(_fetch_habr_page(page_number))

    return raw_pages


def parse_habr_page(raw_page):
    articles_info = []
    soup = bs4.BeautifulSoup(raw_page, 'html.parser')
    for article_block in soup.find_all('article', {'class': 'post post_preview'}):
        title_block = article_block.find('a', {'class': 'post__title_link'})
        date_block = article_block.find('span', {'class': 'post__time'})
        articles_info.append({
            'title': title_block.contents[0],
            'publication_date_time': dateparser.parse(date_block.text)  # Сделать обработку исключения ValueError
        })
    return articles_info


def _fetch_habr_page(page_number):
    url = 'https://habr.com/all/'
    if page_number:
        url += 'page{number}'.format(number=page_number)

    return requests.get(url).text
