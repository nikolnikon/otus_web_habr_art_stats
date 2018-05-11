# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser
from habr_art_stat.exceptins import ParseError
from habr_art_stat.habr_parser import fetch_habr_feed, parse_habr_page
from habr_art_stat.habr_stat import calc_popular_nouns_by_weeks, output_stat


def main():
    try:
        return_code = 0
        parser = ArgumentParser('Подсчет самых популярных существительных в заголовках статей с сайта habr.com')
        parser.add_argument('-p', '--pages', nargs='?', default=5, type=int,
                            help='Количество страниц сайта habr.com, с которых будут получены заголовки статей')
        parser.add_argument('-t', '--top', nargs='?', default=3, type=int,
                            help='Количество существительных, выводимых в статистике')
        args = parser.parse_args(sys.argv[1:])
        articles_info = []
        for raw_page in fetch_habr_feed(pages=args.pages):
            articles_info += parse_habr_page(raw_page)

        stat = calc_popular_nouns_by_weeks(articles_info, args.top)
        output_stat(stat)
    except ParseError as e:
        print(e)
        return_code = 2
    except Exception as e:
        print('Неопределенная ошибка в приложении: {exception}'.format(exception=e))
        return_code = 1

    return return_code
