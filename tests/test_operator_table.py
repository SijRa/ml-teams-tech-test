import json
import unittest

from ExtractToCSV import OperatorsTable

class TestOperatorTable(unittest.TestCase):

    def test_find_operator_valid(self):

        # Setup
        test_numbergroup = 3235
        operators = json.loads(
            '[{"type":"operator","id":"12d9b951-c125-4da0-a70f-609b7ac558d8","attributes":{"prefix":"3000","operator":"EE"}},{"type":"operator","id":"6f8f0022-0e5b-4018-9e2a-0703481758e6","attributes":{"prefix":"4000","operator":"O2"}},{"type":"operator","id":"2eca5a6c-c9f1-42b8-980a-b91b7ac25c06","attributes":{"prefix":"5000","operator":"Three"}},{"type":"operator","id":"e4fa86dd-b8e2-496f-aac4-a1acd8c4e6db","attributes":{"prefix":"1000","operator":"Vodafone"}},{"type":"operator","id":"4207272a-75ae-4cd1-b91c-dd2c34179a82","attributes":{"prefix":"9000","operator":"Monaco Telecom"}},{"type":"operator","id":"d0e76f09-4678-4b79-a6ec-7e0c30a4d0eb","attributes":{"prefix":"8000","operator":"Orange"}},{"type":"operator","id":"079c1ac1-babd-4fe7-b399-262ab79d4181","attributes":{"prefix":"7000","operator":"Swisscom"}},{"type":"operator","id":"a319f299-cd13-41c7-a473-56a2aea8c0f9","attributes":{"prefix":"2000","operator":"Bouygues Telecom"}}]'
            )
        operator_table = OperatorsTable(operators)

        # Execute
        op = operator_table.find_operator(test_numbergroup)

        # Check
        self.assertEqual(op, 'EE')
        

    def test_find_operator_unknown(self):
        
        # Setup
        test_numbergroup = 6446
        operators = json.loads(
            '[{"type":"operator","id":"12d9b951-c125-4da0-a70f-609b7ac558d8","attributes":{"prefix":"3000","operator":"EE"}},{"type":"operator","id":"6f8f0022-0e5b-4018-9e2a-0703481758e6","attributes":{"prefix":"4000","operator":"O2"}},{"type":"operator","id":"2eca5a6c-c9f1-42b8-980a-b91b7ac25c06","attributes":{"prefix":"5000","operator":"Three"}},{"type":"operator","id":"e4fa86dd-b8e2-496f-aac4-a1acd8c4e6db","attributes":{"prefix":"1000","operator":"Vodafone"}},{"type":"operator","id":"4207272a-75ae-4cd1-b91c-dd2c34179a82","attributes":{"prefix":"9000","operator":"Monaco Telecom"}},{"type":"operator","id":"d0e76f09-4678-4b79-a6ec-7e0c30a4d0eb","attributes":{"prefix":"8000","operator":"Orange"}},{"type":"operator","id":"079c1ac1-babd-4fe7-b399-262ab79d4181","attributes":{"prefix":"7000","operator":"Swisscom"}},{"type":"operator","id":"a319f299-cd13-41c7-a473-56a2aea8c0f9","attributes":{"prefix":"2000","operator":"Bouygues Telecom"}}]'
            )
        operator_table = OperatorsTable(operators)
        
        # Execute
        op = operator_table.find_operator(test_numbergroup)

        # Check
        self.assertEqual(op, 'Unknown')


    def test_find_operator_invalid(self):

        # Setup
        test_numbergroup = int('0536')
        operators = json.loads(
            '[{"type":"operator","id":"12d9b951-c125-4da0-a70f-609b7ac558d8","attributes":{"prefix":"3000","operator":"EE"}},{"type":"operator","id":"6f8f0022-0e5b-4018-9e2a-0703481758e6","attributes":{"prefix":"4000","operator":"O2"}},{"type":"operator","id":"2eca5a6c-c9f1-42b8-980a-b91b7ac25c06","attributes":{"prefix":"5000","operator":"Three"}},{"type":"operator","id":"e4fa86dd-b8e2-496f-aac4-a1acd8c4e6db","attributes":{"prefix":"1000","operator":"Vodafone"}},{"type":"operator","id":"4207272a-75ae-4cd1-b91c-dd2c34179a82","attributes":{"prefix":"9000","operator":"Monaco Telecom"}},{"type":"operator","id":"d0e76f09-4678-4b79-a6ec-7e0c30a4d0eb","attributes":{"prefix":"8000","operator":"Orange"}},{"type":"operator","id":"079c1ac1-babd-4fe7-b399-262ab79d4181","attributes":{"prefix":"7000","operator":"Swisscom"}},{"type":"operator","id":"a319f299-cd13-41c7-a473-56a2aea8c0f9","attributes":{"prefix":"2000","operator":"Bouygues Telecom"}}]'
            )
        operator_table = OperatorsTable(operators)

        # Execute
        op = operator_table.find_operator(test_numbergroup)

        # Check
        self.assertEqual(op, 'Unknown')


    def test_operator_table_build(self):

        # Setup
        operators = json.loads(
            '[{"type":"operator","id":"12d9b951-c125-4da0-a70f-609b7ac558d8","attributes":{"prefix":"3000","operator":"EE"}},{"type":"operator","id":"6f8f0022-0e5b-4018-9e2a-0703481758e6","attributes":{"prefix":"4000","operator":"O2"}},{"type":"operator","id":"2eca5a6c-c9f1-42b8-980a-b91b7ac25c06","attributes":{"prefix":"5000","operator":"Three"}}]'
            )

        # Execute
        operator_table = OperatorsTable(operators)

        # Check
        expected = "{3000: 'EE', 4000: 'O2', 5000: 'Three'}"
        self.assertEqual(str(operator_table), expected)
        
