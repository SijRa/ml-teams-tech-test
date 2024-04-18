import logging

from datetime import datetime

logger = logging.getLogger(__name__)

def get_phone_group(number:str) -> int:
    """
    Returns the phone group number i.e. 447138423818 -> 3842
    """
    phone_group = number[::-1][:8]
    group = int(phone_group[::-1][:4])
    logger.debug('\tGroup conversion: %s -> %s', number, group)
    return group

def create_dict_from_lists(ids:list[str], dates:list[str], numbers:list[str], operators:list[str], riskScores:list[str]) -> list[dict]:
    """
    Returns a sorted list of dictionarys from lists of data
    """
    data_dict = []
    for i in range(len(ids)):
        row = {'id':ids[i], 'date':dates[i], 'number':numbers[i], 'operator': operators[i], 'riskScore': riskScores[i]}
        data_dict.append(row)
        logger.debug('Appending to dict from lists: %s', row)
    return data_dict

def sort_by_ascending(data: list[dict]) -> dict:
    """
    Returns list of dict in ascending order by date
    """
    data.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    return data

def extract_date(long_date:str) -> str:
    """
    Returns YYYY-MM-DD from RFC3339 i.e. 2019-10-12T07:20:50.52Z -> 2019-10-12
    """
    processed_date = long_date.split('T')[0]
    logger.debug('Date processed from: \t %s -> %s', long_date, processed_date)
    return processed_date