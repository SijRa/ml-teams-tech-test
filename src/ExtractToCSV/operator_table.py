import sys
import logging

from math import floor

logger = logging.getLogger(__name__)

class OperatorsTable:
    """
    Dictionary containing operators (e.g. O2, Three) and their respective prefix range
    """

    def __init__(self, operators_json) -> None:
        """
        operators.json required to instantiate the OperatorTable class
        """
        self.__table = self.__build(operators_json)
        logger.info('OperatorTable built successfully')

    def __build(self, operators_json) -> dict[int, str]:
        """
        Build operators table by enumerating through given operators json
        """
        table = {}
        for index, operator in enumerate(operators_json):
            operator = operators_json[index]['attributes']['operator']
            prefix = operators_json[index]['attributes']['prefix']
            table[int(prefix)] = operator
        logger.debug('Operator table successfully built')
        return table
    
    def find_operator(self, number_band:int) -> str:
        """
        Returns operator if found otherwise returns 'Unknown'
        """
        prefix_group = floor(number_band/1000)*1000
        logger.debug(f"Prefix grouping: {number_band} -> {prefix_group}")
        try:
            operator = self.__table[prefix_group]
            logger.debug('Operator found for prefix group: %s -> %s', prefix_group, operator)
        except KeyError:
            logger.warn('Operator NOT found for prefix group: %s', prefix_group)
            return 'Unknown'
        return operator
    
    def __len__(self) -> int:
        """
        Prints size of operators table
        """
        return len(self.__table.values())

    def __str__(self) -> str:
        """
        Prints operators table
        """
        return str(self.__table)