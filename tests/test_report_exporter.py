import unittest

from unittest.mock import patch
from ExtractToCSV import CSVExporter

class TestReportExporter(unittest.TestCase):

    @patch('csv.DictWriter')
    def test_extract_json(self, mock_writer):
        
        # Setup
        test_data = [{"test":"data"}, {"test":"data"}]
        report_exporter = CSVExporter()

        # Execute        
        report_exporter.export('test_output.csv', test_data)

        # Check
        self.assertTrue(mock_writer.called)
