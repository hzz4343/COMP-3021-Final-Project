""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Zizhang He
Date: 30 August 2024
"""

from genre.genre import Genre
from borrower_status.borrower_status import BorrowerStatus
from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem and LibraryUser class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", Genre.FICTION, True)
    except Exception as error:
        print(error)
        
    try:
        library_user = LibraryUser(101, "Patrick", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
    except Exception as error:
        print(error)    

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem and LibraryUser instance.
    print(library_item.item_id)
    print(library_item.title)    
    print(library_item.author)
    print(library_item.genre)
    print(library_item.is_borrowed)
    
    print(library_user.user_id)
    print(library_user.name)
    print(library_user.email)
    print(library_user.borrower_status)

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        # Quick check item_id
        library_item = LibraryItem("101", "3 Body Problem", "Cixin Liu", Genre.FICTION, True)
    except Exception as error:
        print(error)
    
    try:
        # Quick check title
        library_item = LibraryItem(101, "", "Cixin Liu", Genre.FICTION, True)
    except Exception as error:
        print(error)
        
    try:
        # Quick check author
        library_item = LibraryItem(101, "3 Body Problem", "", Genre.FICTION, True)
    except Exception as error:
        print(error)

    try:
        # Quick check genre
        library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", "fiction", True)
    except Exception as error:
        print(error)
    
    try:
        # Quick check is_borrowed
        library_item = LibraryItem(101, "3 Body Problem", "Cixin Liu", Genre.FICTION, "True") 
    except Exception as error:
        print(error)
          
    #   Using the instance defined above, invoke the borrow_item method and print the result.
    print(library_user.borrow_item())
    
    #   Using the instance defined above, invoke the return_item method and print the result.
    print(library_user.return_item())
    
    #   Code a statement which creates an instance of the LibraryUser class with one or more invalid inputs. Use your own unique valid values for the inputs to the class.
    try:
        # Quick check user id
        library_user = LibraryUser(98, "Patrick", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
    except Exception as error:
        print(error)    
    
    try:
        # Quick check name
        library_user = LibraryUser(101, " ", "hzz1996@qq.com", BorrowerStatus.ACTIVE)
    except Exception as error:
        print(error)    
        
if __name__ == "__main__":
    main()