""""
Description: A class to manage LibraryItem objects.
Author: Zizhang He
Date: 30 August 2024
"""
from genre.genre import Genre

class LibraryItem:
    """Represents a library item in the library.
    """
    
    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """Initializes a new instance of the LibraryItem class.

        Args:
            item_id: An id number to uniquely identify the library item.
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The Genre of the library item.
            is_borrowed: Identifies whether the library item is borrowed (True) or available (False).

        Raises:
            ValueError: Raised when the title or author contains no non-whitespace characters,
                        or the genre is not one of the valid genres included in the Genre
                        enumeration. It is also raised when item_id is not numeric or is_borrowed
                        is not a boolean value.
        """        
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")

        if len(title.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        
        if len(author.strip()) == 0:
            raise ValueError("Author cannot be blank.")
        
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")

        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed
    
    @property
    def item_id(self) -> int:
        """Gets the id of the item.
        
        Returns:
            The id of the item.
        """
        return self.__item_id
    
    @property
    def title(self) -> str:
        """Gets the title of the item.
        
        Returns:
            The title of the item.
        """
        return self.__title
    
    @property
    def author(self) -> str:
        """Gets the author of the item.
        
        Returns:
            The author of the item.
        """
        return self.__author
    
    @property
    def genre(self) -> Genre:
        """Gets the genre of the item.
        
        Returns:
            The genre of the item.
        """
        return self.__genre
    
    @property
    def is_borrowed(self) -> bool:
        """Gets the information whether the item is borrowed.
        
        Returns:
            The information whether the item is borrowed.
        """
        return self.__is_borrowed
