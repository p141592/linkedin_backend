import re

phone_regex = re.compile('^((9|4)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{10}$')


def check_phone(phone):
    return re.match(phone_regex, str(phone)) is not None


def check_email(email):
    p = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)
    m = p.match(email)
    if m:
        return True
    else:
        return False

