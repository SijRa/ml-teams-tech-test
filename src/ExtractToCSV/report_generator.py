import logging

from typing import Tuple

from utils import get_phone_group, extract_date
from data_loader import DataLoader
from operator_table import OperatorsTable

logger = logging.getLogger(__name__)

def generate_report_data_list(calls_file:str, operators_file:str) -> Tuple[list[str], list[str], list[str], list[str], list[str]]:
    """
    Returns a tuple of lists containing id, date, number, operator and riskScore from calls and operators.
    """
    # Initialise empty lists
    id_list = []
    date_list = []
    number_list = []
    operator_list = []
    riskScore_list = []

    # Extract data from files
    loader = DataLoader()
    calls = loader.extract_json_from_file(calls_file)
    operators = loader.extract_json_from_file(operators_file)


    # Create operator table for querying
    operator_table = OperatorsTable(operators)

    logger.info('All data loaded successfully.')

    # Assemble report data list
    for call in calls:

        logger.debug('call data: %s', call)
        
        id_list.append(call['id']) # ID
        
        date_list.append(extract_date(call['attributes']['date'])) # DATE
        
        try:
            number = call['attributes']['number'] 
        except KeyError:
            number = 'Withheld'
        number_list.append(number) # NUMBER

        operator = 'Unknown'
        if number != "Withheld":
            group = get_phone_group(number[1:]) # skip '+' char
            operator = operator_table.find_operator(group)
        operator_list.append(operator) # OPERATOR

        riskScore = call['attributes']['riskScore']
        if call['attributes']['redList'] == True:
            riskScore = 0
        riskScore_list.append(str(riskScore)) # RISK SCORE

        logger.debug('%s \t %s \t %s \t %s \t %s', id_list[-1], date_list[-1], number_list[-1], operator_list[-1], riskScore_list[-1])
    
    logger.info('Report data list assembled.')

    return id_list, date_list, number_list, operator_list, riskScore_list