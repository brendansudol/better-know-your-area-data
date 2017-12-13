def chunks(li, n=40):
    for i in range(0, len(li), n):
        yield li[i:i + n]


def flatten(li):
    return [item for sub_li in li for item in sub_li]
