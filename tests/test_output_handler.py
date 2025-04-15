import unittest
from unittest import TestCase
from output_handler.output_handler import OutputHandler
from unittest.mock import patch, mock_open

class TestOutputHandler(TestCase):
    """The following constants have been provided to reduce the amount of
    code needed when creating OutputHandler class objects in the tests that
    follow.  To use the constants, prefix them with self.  Examples:
    self.ACCOUNT_SUMMARIES
    self.SUSPICIOUS_TRANSACTIONS
    self.TRANSACTION_STATISTICS
    e.g.:  output_handler = OutputHandler(self.ACCOUNT_SUMMARIES,
                            self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
    """

    ACCOUNT_SUMMARIES = {
        "1001": {
            "account_number": "1001",
            "balance": 50,
            "total_deposits": 100,
            "total_withdrawals": 50,
        },
        "1002": {
            "account_number": "2",
            "balance": 200,
            "total_deposits": 200,
            "total_withdrawals": 0,
        },"1003": {
            "account_number": "3",
            "balance": 300,
            "total_deposits": 300,
            "total_withdrawals": 0,
        }
    }

    SUSPICIOUS_TRANSACTIONS = [
        {
            "Transaction ID": "1",
            "Account number": "1001",
            "Date": "2023-03-14",
            "Transaction type": "deposit",
            "Amount": 250,
            "Currency": "XRP",
            "Description": "crypto investment",
        }
    ]

    TRANSACTION_STATISTICS = {
        "deposit": {"total_amount": 300, "transaction_count": 2},
        "withdrawal": {"total_amount": 50, "transaction_count": 1},
    }
    
    def test_write_account_summaries_to_csv(self):
        # Arrange
        output_handler = OutputHandler(
            self.ACCOUNT_SUMMARIES,
            self.SUSPICIOUS_TRANSACTIONS,
            self.TRANSACTION_STATISTICS,
        )
        filename = "account_summaries_to_csv_temp.csv"
        expected_row_count = len(self.ACCOUNT_SUMMARIES) + 1  # Accounts + header

        # Act + Assert
        with patch("builtins.open", mock_open()) as mocked_open:
            output_handler.write_account_summaries_to_csv(filename)
            
        mocked_open.assert_called_once_with(filename, 'w', newline='')
        
        mock_file = mocked_open()
        self.assertEqual(mock_file.write.call_count, expected_row_count)

    def test_write_suspicious_transactions_to_csv(self):
        # Arrange
        output_handler = OutputHandler(
            self.ACCOUNT_SUMMARIES,
            self.SUSPICIOUS_TRANSACTIONS,
            self.TRANSACTION_STATISTICS,
        )
        filename = "suspicious_transactions_temp.csv"
        expected_row_count = len(self.SUSPICIOUS_TRANSACTIONS) + 1  # Accounts + header

        # Act + Assert
        with patch("builtins.open", mock_open()) as mocked_open:
            output_handler.write_suspicious_transactions_to_csv(filename)

        mocked_open.assert_called_once_with(filename, 'w', newline='')
        
        mock_file = mocked_open()
        self.assertEqual(mock_file.write.call_count, expected_row_count)

    def test_write_transaction_statistics_to_csv(self): 
        # Arrange
        output_handler = OutputHandler(
            self.ACCOUNT_SUMMARIES,
            self.SUSPICIOUS_TRANSACTIONS,
            self.TRANSACTION_STATISTICS,
        )
        filename = "transaction_statistics_temp.csv"
        expected_row_count = len(self.TRANSACTION_STATISTICS) + 1  # Transactions + header

        # Act + Assert
        with patch("builtins.open", mock_open()) as mocked_open:
            output_handler.write_transaction_statistics_to_csv(filename)

        mocked_open.assert_called_once_with(filename, 'w', newline='')
        
        mock_file = mocked_open()
        self.assertEqual(mock_file.write.call_count, expected_row_count)  


if __name__ == "__main__":
    unittest.main()