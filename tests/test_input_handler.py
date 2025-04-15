import os
import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler

class InputHandlerTests(TestCase):
    
    def setUp(self):
        """Set up resources before test."""
        self.test_csv_file = 'test_data.csv'
        
        with open(self.test_csv_file, 'w') as csv_file:
            csv_file.write("Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n")
            csv_file.write("1,1001,2023-03-01,deposit,1000,CAD,Salary\n")
            csv_file.write("2,1002,2023-03-01,deposit,1500,CAD,Salary\n")

    def tearDown(self):
        """Clear resources after test."""
        try:
            os.remove(self.test_csv_file)
        except FileNotFoundError:
            pass

    def test_get_file_format_with_proper_extension(self):
        """Test to verify that the extension is returned when the file has a proper extension."""
        # Arrange
        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.get_file_format()
        # Assert
        self.assertEqual(data, 'csv', 'Riases proper extenstion error')

    def test_get_file_format_with_no_extension(self):
        """Test to verify that an empty string is returned when the file does not have an extension."""
        # Arrange
        handler = InputHandler('example.')
        # Act
        data = handler.get_file_format()
        # Assert
        self.assertEqual(data, '', 'Raises no extension error')

    def test_read_csv_data_with_populated_file(self):
        """Test to verify that a populated list is returned when the .csv file exists and contains data."""
        # Arrange
        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.read_csv_data()
        # Assert
        expected_data = [
            {'Transaction ID': '1', 'Account number': '1001', 'Date': '2023-03-01', 
             'Transaction type': 'deposit', 'Amount': '1000', 'Currency': 'CAD', 'Description': 'Salary'},
            {'Transaction ID': '2', 'Account number': '1002', 'Date': '2023-03-01', 
             'Transaction type': 'deposit', 'Amount': '1500', 'Currency': 'CAD', 'Description': 'Salary'}
        ]
        self.assertEqual(data, expected_data, 'Raises populated file error')

    def test_read_csv_data_with_empty_file(self):
        """Test to verify that an empty list is returned when the .csv file exists, but is empty."""
        # Arrange
        with open(self.test_csv_file, 'w') as csv_file:
            csv_file.write('')
        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.read_csv_data()
        # Assert
        self.assertEqual(data, [], 'Raises empty file error')

    def test_read_csv_data_with_no_existent_file(self):
        """Test to verify that a FileNotFoundError exception is raised when the .csv file does not exist."""
        # Arrange
        handler = InputHandler('nonexistent.csv')
        # Act and Assert
        with self.assertRaises(FileNotFoundError):
            handler.read_csv_data()

    def test_read_input_data_with_valid_csv_file(self):
        """Test to verify that a populated list is returned when a valid .csv file is used."""
        # Arrange
        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.read_input_data()
        
        # Assert
        expected_data = [
            {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "1000", "Currency": "CAD", "Description": "Salary"},
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"}
        ]
        self.assertEqual(data, expected_data, 'Raises valid file error')

    def test_read_input_data_with_invalid_extension(self):
        """Test to verify that an empty list is returned when a file with an invalid extension is used."""
        # Arrange
        handler = InputHandler('invalid.txt')
        # Act
        data = handler.read_input_data()
        # Assert
        self.assertEqual(data, [], 'Raises invalid extension error')

    #Milestone 2

    def test_data_validation_with_non_numeric_amount(self):
        """Test to verify that the returned list excludes records with a non-numeric amount."""
        # Arrange
        # Adjust the CSV file for this test
        with open(self.test_csv_file, 'w') as csv_file:
            csv_file.write("Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n")
            csv_file.write("1,1001,2023-03-01,deposit,text,CAD,Salary\n") # non-numeric amount
            csv_file.write("2,1002,2023-03-01,deposit,1500,CAD,Salary\n")

        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.data_validation()
        # Assert
        # Filtered non-numeric amount transaction
        expected_data = [
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"}
        ]
        self.assertEqual(data, expected_data, 'Raises non-numeric amount error')
    
    def test_data_validation_with_negative_amount(self):
        """Test to verify that the returned list excludes records with a negative amount."""
        # Arrange
        # Adjust the CSV file for this test
        with open(self.test_csv_file, 'w') as csv_file:
            csv_file.write("Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n")
            csv_file.write("1,1001,2023-03-01,deposit,-1000,CAD,Salary\n") # negative amount
            csv_file.write("2,1002,2023-03-01,deposit,1500,CAD,Salary\n")

        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.data_validation()
        # Assert
        # Filtered the transaction with negative amount
        expected_data = [
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"}
        ]
        self.assertEqual(data, expected_data, 'Raises negative amount error')

    def test_data_validation_with_invalid_transaction_type(self):
        """Test to verify that the returned list excludes records with an invalid transaction_type."""
        # Arrange
        # Adjust the CSV file for this test
        with open(self.test_csv_file, 'w') as csv_file:
            csv_file.write("Transaction ID,Account number,Date,Transaction type,Amount,Currency,Description\n")
            csv_file.write("1,1001,2023-03-01,invalid_type,1000,CAD,Salary\n") # invalid transaction type
            csv_file.write("2,1002,2023-03-01,deposit,1500,CAD,Salary\n")

        handler = InputHandler(self.test_csv_file)
        # Act
        data = handler.data_validation()
        # Assert
        # Filtered the transaction with invalid transaction type
        expected_data = [
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"}
        ]
        self.assertEqual(data, expected_data, 'Raises invalid transaction type error')

if __name__ == "__main__":
    unittest.main()