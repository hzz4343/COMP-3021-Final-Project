import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when creating DataProcessor class objects in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.INPUT_DATA
    e.g.:  data_procesor = DataProcessor(self.INPUT_DATA)
    """
    INPUT_DATA = [{"Transaction ID":"1" ,"Account number":"1001" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1000,"Currency":"CAD","Description":"Salary"}, 
                {"Transaction ID":"2" ,"Account number":"1002" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1500,"Currency":"CAD","Description":"Salary"},
                {"Transaction ID":"3" ,"Account number":"1002" ,
                "Date":"2023-03-01" ,"Transaction type": "withdrawal",
                "Amount":500,"Currency":"CAD","Description":"Fine"},
                {"Transaction ID":"4" ,"Account number":"1003" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":50000,"Currency":"CAD","Description":"Lottery"},
                {"Transaction ID":"5" ,"Account number":"1004" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1000,"Currency":"XRP","Description":"Remote job salary"}]

    def test_update_account_summary_deposit(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        account_number = "1001"
        expected_balance = 1000
        
        # Act
        account_summary = data_processor.account_summaries
        actual_balance = account_summary[account_number]["balance"]
        
        # Assert
        self.assertEqual(expected_balance, actual_balance)

    def test_update_account_summary_withdrawal(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        account_number = "1002"
        expected_balance = 1000
        
        # Act
        account_summary = data_processor.account_summaries
        actual_balance = account_summary[account_number]["balance"]
        
        # Assert
        self.assertEqual(expected_balance, actual_balance)
        
    def test_check_suspicious_transactions_large_amount(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        expected_output = {"Transaction ID":"4" ,"Account number":"1003" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":50000,"Currency":"CAD","Description":"Lottery"}
        
        # Act
        actual_output = data_processor.suspicious_transactions[0]

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        expected_output = {"Transaction ID":"5" ,"Account number":"1004" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1000,"Currency":"XRP","Description":"Remote job salary"}
        
        # Act
        actual_output = data_processor.suspicious_transactions[1]

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_update_transaction_statistics(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        expected_deposit_output = 53500.0
        expected_withdrawal_output = 500.0
        
        # Act
        actual_deposit_output = data_processor.transaction_statistics["deposit"]["total_amount"]
        actual_withdrawal_output = data_processor.transaction_statistics["withdrawal"]["total_amount"]
        

        # Assert
        self.assertEqual(expected_deposit_output, actual_deposit_output)
        self.assertEqual(expected_withdrawal_output, actual_withdrawal_output)

    def test_get_average_transaction_amount(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()
        
        expected_deposit_output = 13375.0
        expected_withdrawal_output = 500.0
        
        # Act
        actual_deposit_output = data_processor.get_average_transaction_amount("deposit")
        actual_withdrawal_output = data_processor.get_average_transaction_amount("withdrawal")
        
        # Assert
        self.assertEqual(expected_deposit_output, actual_deposit_output)
        self.assertEqual(expected_withdrawal_output, actual_withdrawal_output)


if __name__ == "__main__":
    unittest.main()
