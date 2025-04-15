"""
Description: Unit tests for the LibraryUser class.
Author: Zizhang He
Date: 31 August
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

from library_user.library_user import LibraryUser
from borrower_status.borrower_status import BorrowerStatus
import unittest

class Test_LibraryUser(unittest.TestCase):
    """Test for the Library_User class.
    """
    
    def setUp(self):
        """Setup runs AUTOMATICALLY before each test method and
        provides initial values for the class attributes.
        """
        self.library_user = LibraryUser(101, "Patrick", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
        self.delinquent_library_user = LibraryUser(101, "Patrick", "hzz1996@qq.com", BorrowerStatus.DELINQUENT)

    def test_init_initializes_object(self):
        # Assert
        self.assertEqual(101, self.library_user._LibraryUser__user_id)
        self.assertEqual("Patrick", self.library_user._LibraryUser__name)
        self.assertEqual("hzz1996@qq.com", self.library_user._LibraryUser__email)
        self.assertEqual(BorrowerStatus.ACTIVE, self.library_user._LibraryUser__borrower_status)

    def test_init_non_numeric_user_id_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser("101", "Patrick", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
            
        self.assertEqual("User Id must be numeric.", str(context.exception))
    
    def test_init_invalid_user_id_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser(98, "Patrick", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
            
        self.assertEqual("Invalid User Id.", str(context.exception))
            
    def test_init_blank_name_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser(101, "", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
            
        self.assertEqual("Name cannot be blank.", str(context.exception))            
            
    def test_init_blank_name_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser(101, "", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
            
        self.assertEqual("Name cannot be blank.", str(context.exception))  
        
    def test_init_invalid_email_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser(101, "Patrick", "hzz1996qq.com", BorrowerStatus.ACTIVE)
            
        self.assertEqual("Invalid email address.", str(context.exception))         
        
    def test_init_invalid_borrower_status_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_user = LibraryUser(101, "Patrick", "hzz1996@qq.com", "active")
            
        self.assertEqual("Invalid Borrower Status.", str(context.exception))      
                 
    def test_user_id_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(101, self.library_user.user_id)
        
    def test_name_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("Patrick", self.library_user.name)
        
    def test_email_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("hzz1996@qq.com", self.library_user.email)
        
    def test_borrower_status_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(BorrowerStatus.ACTIVE, self.library_user.borrower_status)
            
    def test_borrow_item_raise_exception(self):

        # Assert
        with self.assertRaises(Exception) as context:
            self.delinquent_library_user.borrow_item()
            
        self.assertEqual("Patrick cannot borrow an item due to their delinquent status.", str(context.exception))
    
    def test_borrow_item_return_message(self):
        # Assert
        self.assertEqual("Patrick is eligible to borrow the item.", self.library_user.borrow_item())

    def test_return_item_modify_status(self):
        # Assert
        self.assertEqual("Item successfully returned. Patrick has returned the item, status now changed to: active.", self.delinquent_library_user.return_item())

    def test_return_item_return_message(self):
        # Assert
        self.assertEqual("Item successfully returned.", self.library_user.return_item())
    