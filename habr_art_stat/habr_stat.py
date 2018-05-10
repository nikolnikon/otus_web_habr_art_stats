# -*- coding: utf-8 -*-

from datetime import timedelta
import re
import pymorphy2
import collections


def calc_popular_nouns_by_weeks(articles_info, nouns_count=3):
    morph = pymorphy2.MorphAnalyzer()
    words_by_weeks = _group_words_by_weeks(articles_info)
    nouns_by_week = {}
    for week in words_by_weeks:
        words = words_by_weeks[week]
        nouns = []
        for word in words:
            parsed = morph.parse(word)[0]
            if 'NOUN' in parsed.tag:
                nouns.append(parsed.normal_form)
        nouns_by_week[week] = collections.Counter(nouns).most_common(nouns_count)

    return nouns_by_week


def output_stat(nouns_by_week, nouns_count=3):
    print('Начало недели | Конец недели | Популярные слова из заголовков                  ')
    print('-------------------------------------------------------------------------------')
    for week in nouns_by_week:
        nouns = [noun for noun in [stat for stat in nouns_by_week[week]]]
        print('{week_begin}    | {week_end}   | {nouns}'.format(week_begin=week[0], week_end=week[1], nouns=nouns))


def _group_words_by_weeks(articles_info):
    words_by_weeks = {}
    dates = [info['publication_date_time']for info in articles_info]
    dates.sort()
    week_start_date = None
    week_end_date = None
    words = []

    for index, date in enumerate(dates):
        if not week_end_date:
            week_end_date = date.date()
            week_start_date = week_end_date - timedelta(days=week_end_date.weekday())

        if date.date() not in (week_start_date, week_end_date):
            week_start_date = date.date() - timedelta(days=date.weekday())
            week_end_date = date.date() + timedelta(days=6 - date.weekday())
            words = []

        words += re.sub('[^a-zа-я]', ' ', articles_info[index]['title'].lower().strip()).split()
        words_by_weeks[(week_start_date, week_end_date)] = words

    # for index, date in enumerate(dates):
    #     if not week_start_date:
    #         week_start_date = date
    #         words += re.sub('[^a-zа-я]', ' ', articles_info[index]['title'].lower().strip()).split()
    #         continue
    #     if week_start_date.weekday() > date.weekday():
    #         week_end_date = date
    #     elif week_start_date.weekday() <= date.weekday():
    #         words_by_weeks[(week_start_date, week_end_date)] = words
    #         week_start_date = date
    #         words = []
    #     words += re.sub('[^a-zа-я]', ' ', articles_info[index]['title'].lower().strip()).split()

    return words_by_weeks