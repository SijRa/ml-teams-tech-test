import unittest

from unittest.mock import patch

from ExtractToCSV import utils

class TestUtils(unittest.TestCase):

    def test_get_phone_group(self):
        
        # Setup
        test_number = '447138423818'

        # Execute        
        group = utils.get_phone_group(test_number)

        # Check
        self.assertEqual(3842, group)

    def test_create_dict_from_lists(self):
        
        # Setup
        ids = ['a1', 'b2', 'c3']
        dates = ['1994-03-12', '1996-02-15', '1996-02-14']
        numbers = ['425', '534', '734']
        operators = ['Op1', 'Op2', 'Op3']
        riskScores = [0.5, 0.3, 0]

        expected_dict = [
            {'id':'a1','date':'1994-03-12','number':'425','operator':'Op1','riskScore':0.5},
            {'id':'b2','date':'1996-02-15','number':'534','operator':'Op2','riskScore':0.3},
            {'id':'c3','date':'1996-02-14','number':'734','operator':'Op3','riskScore':0}
        ]

        # Execute        
        dict = utils.create_dict_from_lists(ids, dates, numbers, operators, riskScores)

        # Check
        self.assertEqual(dict, expected_dict)

    def test_sort_by_ascending(self):
        
        # Setup
        ids = ['a1', 'b2', 'c3']
        dates = ['1994-03-12', '1996-02-15', '1996-02-14']
        numbers = ['425', '534', '734']
        operators = ['Op1', 'Op2', 'Op3']
        riskScores = [0.5, 0.3, 0]

        expected_dict = [
            {'id':'a1','date':'1994-03-12','number':'425','operator':'Op1','riskScore':0.5},
            {'id':'c3','date':'1996-02-14','number':'734','operator':'Op3','riskScore':0},
            {'id':'b2','date':'1996-02-15','number':'534','operator':'Op2','riskScore':0.3}
        ]

        # Execute        
        data = utils.create_dict_from_lists(ids, dates, numbers, operators, riskScores)
        sorted_data = utils.sort_by_ascending(data)

        # Check
        self.assertEqual(sorted_data, expected_dict)

    def test_extract_date(self):
        
        # Setup
        test_date = '2019-10-12T07:20:50.52Z'
        expected_date = '2019-10-12'

        # Execute        
        converted_date = utils.extract_date(test_date)

        # Check
        self.assertEqual(converted_date, expected_date)