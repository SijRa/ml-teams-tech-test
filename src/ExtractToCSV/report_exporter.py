import csv
import logging

from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class ReportExporter(ABC):
    """
    Abstract class for basing file exporters from, class currently exports supports:

    -   CSV (CSVExporter)

    """
    @abstractmethod
    def export(self, filename, data):
        pass

class CSVExporter(ReportExporter):
    """
    Class responsible for exporting processed operators and calls data into a CSV file
    """
    def __init__(self) -> None:
        pass

    def export(self, output_file:str, data:dict) -> None:
        """
        Export data to csv
        """
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logger.info('CSV report %s created successfully', output_file)