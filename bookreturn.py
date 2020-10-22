from database import *

def returnBook(bookID):
    try:
        record = findBookById(bookID)
        if record and record[0]['member_id'] != '0':
            result = updateBookStatus(bookID)
            return "Book successfully returned"
        else:
            return "Book not found. Please enter valid Book ID"
    except Exception as err:
        return "An error occured : {}".format(err)
