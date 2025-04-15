"""
Description: Unit tests for the Book class.
Author: Zizhang He
Date: 30 August 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py
"""

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class Test_LibraryItem(unittest.TestCase):
    """Test for the Library_Item class.
    """
    
    def setUp(self):
        """Setup runs AUTOMATICALLY before each test method and
        provides initial values for the class attributes.
        """
        self.library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", Genre.FICTION, True)
        
    def test_init_initializes_object(self):
        
        # Assert
        self.assertEqual(101, self.library_item._LibraryItem__item_id)
        self.assertEqual("3 Body Problem", self.library_item._LibraryItem__title)
        self.assertEqual("Cixin Liu", self.library_item._LibraryItem__author)
        self.assertEqual(Genre.FICTION, self.library_item._LibraryItem__genre)
        self.assertEqual(True, self.library_item._LibraryItem__is_borrowed)
        
    def test_init_invalid_item_id_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_item = LibraryItem("101", "3 Body Problem", "Cixin Liu", Genre.FICTION, True)
            
        self.assertEqual("Item Id must be numeric.", str(context.exception))
    
    
    def test_init_blank_title_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_item = LibraryItem(101, "", "Cixin Liu", Genre.FICTION, True)
            
        self.assertEqual("Title cannot be blank.", str(context.exception))
                       
    def test_init_blank_author_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_item = LibraryItem(101, "3 Body Problem", "", Genre.FICTION, True)
            
        self.assertEqual("Author cannot be blank.", str(context.exception))

    def test_init_invalid_genre_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", "fiction", True)
            
        self.assertEqual("Invalid Genre.", str(context.exception))
        
    def test_init_invalid_is_borrowed_raises_exception(self):
        # Assert
        with self.assertRaises(ValueError) as context:
            library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", Genre.FICTION, "True")
            
        self.assertEqual("Is Borrowed must be a boolean value.", str(context.exception))
        
    def test_item_id_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(101, self.library_item.item_id)
            
    def test_title_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("3 Body Problem", self.library_item.title)
        
    def test_author_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual("Cixin Liu", self.library_item.author)
        
    def test_genre_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(Genre.FICTION, self.library_item.genre)
        
    def test_is_borrowed_accessor_returns_correct_state(self):
        # Assert
        self.assertEqual(True, self.library_item.is_borrowed)
                    
