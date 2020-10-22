from database import *

def checkOutBook(bookID, memberID):
    try:
        record = findBookById(bookID)
        if record[0]['member_id'] != '0':
            return "{} is not available".format(record[0]['title'])
        else:
            result = updateBookStatus(bookID, memberID)
            createLoanHistoryRecord(bookID, memberID)
            return "{} withdrawn successfully".format(record[0]['title'])
    except Exception as err:
        return "An error occured : {}. Please try again".format(err)


if __name__=='__main__':
    pass
