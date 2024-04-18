import sys
import logging
import json

from io import TextIOWrapper

logger = logging.getLogger(__name__)

class DataLoader:
    """
    Class that manages loading of data files, 
    currently supporting:

    -   JSON

    """
    def __init__(self) -> None:
        """
        Constructor for DataLoader class, currently takes no parameters
        """
        pass

    def __open_json_file(self, filename:str) -> TextIOWrapper:
        """
        Returns TextIOWrapper from opening file using filename
        """
        logger.debug(f'File {filename} JSON opened')
        return open(filename)
    
    def extract_json_from_file(self, filename:str, default_key='data'):
        """
        Returns JSON contents from given filename using default extraction key
        """
        filename_with_extension = filename.split('/')[-1]
        file = self.__open_json_file(filename)
        try:
            json_contents = json.load(file)[default_key]
        except KeyError:
            logger.error('Failed to extract data from %s', filename_with_extension)
            sys.stdout('Failed to extract data from %s. Error key: \'%s\'', filename_with_extension, default_key)
            sys.exit(1) # non-successful termination
        logger.info('JSON Extraction successful (%s)', filename_with_extension)
        return json_contents
