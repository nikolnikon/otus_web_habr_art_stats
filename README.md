# habr_art_stat

Приложение для получения статистики с сайта habr.com. Умеет считать самые популярные существительные в заголовках статей

## Установка

С использованием git и easy_install:
```bash
$ git clone https://github.com/nikolnikon/otus_web_habr_art_stats.git
$ cd otus_web_habr_art_stats
$ sudo python setup.py install
```

С использованием git и установкой зависимостей из requirements.txt (для разработки):
```bash
$ git clone https://github.com/nikolnikon/otus_web_habr_art_stats.git
$ cd otus_web_habr_art_stats
$ pip install -r requirements.txt
```

## Пример использования

```bash
$ /usr/bin/habr_art_stat --pages=50

Начало недели | Конец недели | Популярные слова из заголовков    
-----------------------------------------------------------------
2018-05-07    | 2018-05-11   | работа: 9, система: 8, день: 7
2018-04-30    | 2018-05-06   | часть: 9, система: 6, модель: 5
2018-04-23    | 2018-04-29   | часть: 15, система: 9, роскомнадзор: 8
```

## Версионирование
Используется подход [semantic versioning](https://github.com/dbrock/semver-howto/blob/master/README.md).

## Лицензия
Проект распространяентся под лицензией MIT. Подробная информация в файле
[LICENSE](https://github.com/nikolnikon/otus-web-refactoring/blob/master/LICENSE)
