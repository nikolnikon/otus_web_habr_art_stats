# -*- coding: utf-8 -*-

from habr_art_stat.habr_parser import fetch_habr_feed, parse_habr_page
from habr_art_stat.habr_stat import calc_popular_nouns_by_weeks, output_stat


def main():
    articles_info = []
    for raw_page in fetch_habr_feed():
        articles_info += parse_habr_page(raw_page)

    stat = calc_popular_nouns_by_weeks(articles_info)
    output_stat(stat)

    return 0
