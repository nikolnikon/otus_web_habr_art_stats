class ParseError(Exception):
    def __init__(self, message=None):
        super(ParseError, self).__init__('Ошибка при парсинге сайта habr.com. {}'.format(message))
