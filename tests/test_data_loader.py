import json

import unittest
from unittest.mock import patch, mock_open

from ExtractToCSV import DataLoader

class TestDataLoader(unittest.TestCase):

    def test_extract_json(self):

        # Setup
        filename = 'mock_calls.json'
        test_json = '{"data":[{"test":"data"}, {"test":"data"}]}'
        
        # Execute
        with patch('builtins.open', mock_open(read_data=test_json)) as open_mock:
            with open("test_json.json") as open_mock:
                data_loader = DataLoader()
                extracted_json = data_loader.extract_json_from_file(filename)

        # Check
        self.assertEqual(extracted_json, json.loads(test_json)['data'])


        
