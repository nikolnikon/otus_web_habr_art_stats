# -*- coding: utf-8 -*-

import sys
from habr_art_stat.habr_parser import fetch_habr_feed, parse_habr_page
from habr_art_stat.habr_stat import calc_popular_nouns_by_weeks, output_stat
from argparse import ArgumentParser


def main():
    parser = ArgumentParser('Подсчет самых популярных существительных в заголовках статей с сайта habr.com')
    parser.add_argument('-p', '--pages', nargs='?', default=5, type=int,
                        help='Количество страниц сайта habr.com, с которых будут получены заголовки статей')
    args = parser.parse_args(sys.argv[1:])
    articles_info = []
    for raw_page in fetch_habr_feed(pages=args.pages):
        articles_info += parse_habr_page(raw_page)

    stat = calc_popular_nouns_by_weeks(articles_info)
    output_stat(stat)

    return 0
