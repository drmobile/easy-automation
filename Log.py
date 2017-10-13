import inspect


def log_d(msg=''):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('[Debug][{0}]{1} '.format(calframe[1][3], msg))

def log_e(msg=''):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('[Error][{0}]{1} '.format(calframe[1][3], msg))