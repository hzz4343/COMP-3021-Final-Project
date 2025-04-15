""""
Description: A class to manage User objects.
Author: Zizhang He
Date: 31 August 2024
"""

from borrower_status.borrower_status import BorrowerStatus
from email_validator import validate_email, EmailNotValidError
 
class LibraryUser:
    """Represents a library user in the library.
    """
    
    def __init__(self, user_id: int, name: str, email: str, borrower_status: BorrowerStatus):
        """Initializes a new instance of the LibraryUser class.

        Args:
            user_id: The unique user id value of the library user.
            name: The name of the library user.
            email: The email address of the library user.
            borrower_status: The current status of the library user.

        Raises:
            ValueError: Raised when the user id is not an integer or lower than 99, or the user name
                        contains no non-whitespace characters. It is also raised when email is 
                        invalid, or borrower status is invalid.
        """        
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        
        if user_id <= 99:
            raise ValueError("Invalid User Id.")

        if len(name.strip()) == 0:
            raise ValueError("Name cannot be blank.")
        
        try:
            validate_email(email)
        except EmailNotValidError:
            raise ValueError("Invalid email address.")
        
        if not isinstance(borrower_status, BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")
        
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__borrower_status = borrower_status
        
    @property
    def user_id(self) -> int:
        """Gets the id of the user.
        
        Returns:
            The id of the user.
        """
        return self.__user_id
    
    @property
    def name(self) -> str:
        """Gets the name of the user.
        
        Returns:
            The name of the user.
        """
        return self.__name   
    
    @property
    def email(self) -> str:
        """Gets the email of the user.
        
        Returns:
            The email of the user.
        """
        return self.__email
    
    @property
    def borrower_status(self) -> BorrowerStatus:
        """Gets the borrower's status.
        
        Returns:
            The status of the borrower.
        """
        return self.__borrower_status
    
    def borrow_item(self) -> str:
        """Raises error when borrower status is delinquent. Otherwise, returns a string
        indicating the borrower is eligble to borrow the item.

        Returns:
            The "informal" or nicely printable string representation of eligibility."""
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception(f"{self.__name} cannot borrow an item due to their "
                            f"{self.__borrower_status.name.lower()} status.")
            
        return (f"{self.__name} is eligible to borrow the item.")
    
    def return_item(self) -> str:
        """Returns a string indicating the item is reutrned. If the borrower's status is
        delinquent, changes to active.

        Returns:
            The "informal" or nicely printable string indicating return."""
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            self.__borrower_status = BorrowerStatus.ACTIVE
            return (f"Item successfully returned. {self.__name} has returned the item, "
                    f"status now changed to: {self.__borrower_status.name.lower()}.")
            
        return ("Item successfully returned.")
    