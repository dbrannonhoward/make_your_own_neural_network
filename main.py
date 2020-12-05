import logging
this_log = logging.getLogger(__name__)


def configure_log():
    log_('configure logger')
    filename_ = 'event.log'
    format_ = get_log_record_attributes()
    level_ = logging.INFO
    logging.basicConfig(filename=filename_, format=format_, level=level_)


def get_log_record_attributes():
    log_('get log record attributes')
    attributes_ = '%(name)s %(asctime)s %(funcName)s %(levelname)s %(message)s'
    return attributes_


def is_string(item_to_check):
    log_('is string? : ' + str(item_to_check))
    if isinstance(item_to_check, str):
        return True
    return False


def log_(msg='logging event', level=logging.INFO):
    this_log.log(level=level, msg=msg)


def main(name_):
    try:
        log_('try, configure log')
        configure_log()
    except RuntimeError:
        log_('try, configure log, failed')
        raise RuntimeError
    if is_string(name_):
        log_('print message')
        print('hi ' + name_)


if __name__ == '__main__':
    main('man')
