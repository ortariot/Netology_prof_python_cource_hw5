import datetime


# case - 1
def logger(func):

    def _logger(*args, **kwars):
        time = datetime.datetime.now()
        result = func(*args, **kwars)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write((f'{time} - {func.__name__} - "args": {args}'
                    f' - "kwars": {kwars} - "result": {result}\n'
                     )
                     )
            f.close
        return result
    return _logger


# case - 2
def target_logger(path):

    def logger(func):

        def _logger(*args, **kwars):
            time = datetime.datetime.now()
            result = func(*args, **kwars)
            with open(path, 'a', encoding='utf-8') as f:
                f.write((f'{time} - {func.__name__} - "args": {args}'
                        f' - "kwars": {kwars} - "result": {result}\n'
                         )
                        )
                f.close
            return result
        return _logger

    return logger


if __name__ == '__main__':
    @target_logger('log.txt')
    def printer(input):
        print(input)
        return(input)

    printer('I am printer')
