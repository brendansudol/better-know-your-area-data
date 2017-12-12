import re


PROFILE_FIELD_REGEX = 'DP\d{2}_\d{4}[A-Z]{1,2}'


def chunks(li, n=40):
    for i in range(0, len(li), n):
        yield li[i:i + n]


def extract_fields(expression):
    pattern = re.compile('({})'.format(PROFILE_FIELD_REGEX))
    return pattern.findall(expression)


def flatten(li):
    return [item for sub_li in li for item in sub_li]
