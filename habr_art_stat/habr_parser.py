# -*- coding: utf-8 -*-

import bs4
import dateparser
import requests

from habr_art_stat.exceptins import ParseError


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
            'publication_date_time': dateparser.parse(date_block.text)
        })

    return articles_info


def _fetch_habr_page(page_number):
    url = 'https://habr.com/all/'
    if page_number:
        url += 'page{number}'.format(number=page_number)

    try:
        response = requests.get(url)
        if 400 <= response.status_code < 600:
            raise ParseError(response.status_code)
    except requests.ConnectionError as e:
        raise ParseError('Ошибка при соединении с habr.com') from e

    return response.text
