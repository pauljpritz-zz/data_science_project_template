import datetime as dt


def generate_dates(start: dt.datetime, end: dt.datetime,
                   buckets_count: int) -> [dt.datetime]:
    """Generates a list of ``buckets_count + 1`` dates between
    ``start`` and ``end``

    :param start: the first date of the sequence to generate
    :param end: the last date of the sequence to generate
    :param buckets_count: the number of dates to generate - 1

    :return list of blabla
    """
    diff = (end - start) / buckets_count
    for i in range(buckets_count):
        yield start + diff * i
    yield end