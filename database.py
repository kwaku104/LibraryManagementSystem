import subprocess  as sp
import os
import io
import datetime

CurrentDB="Library.db" #default value

def RunSQLStatement(SQLStatement):
    
    prelude = """
.mode list
.header off
    """
    postlude="""
.quit
    """
    
    code_to_run = '\n'.join([prelude, SQLStatement, postlude])
        
    try:
        result=sp.check_output(["sqlite3",CurrentDB],  stderr=sp.STDOUT,
                       input=code_to_run,universal_newlines=True)
        flag=True
    except sp.CalledProcessError as e:
        flag=False
        result=e.output
    return (flag, result)

def returnBookInfoData(SQLStatement):
    flag, result = RunSQLStatement(SQLStatement)
    if flag:
        buf = io.StringIO(result)
        data = []
        while True:
            line = buf.readline().rstrip("\n").split("|")
            if line == [''] or line == []:
                break
            else:
                line = {"id":line[0], "isbn":line[1], "title":line[2], "author":line[3], "date":line[4], "member_id":line[5]}
                data.append(line)
        return data
    else:
        return "error: {}".format(result)

def returnLoanHistoryData(SQLStatement):
    flag, result = RunSQLStatement(SQLStatement)
    if flag:
        buf = io.StringIO(result)
        data = []
        while True:
            line = buf.readline().rstrip("\n").split("|")
            if line == [''] or line == []:
                break
            else:
                line = {"transaction_id":line[0], "book_id":line[1], "checkout_date":line[2], "return_date":line[3], "member_id":line[4]}
                data.append(line)
        return data
    else:
        return "error: {}".format(result) 

def findBookByTitle(bookTitle):
    sqlStatement = "SELECT * FROM Book_Info WHERE title LIKE \"%{}%\";".format(bookTitle)
    if sqlStatement:
        result=returnBookInfoData(sqlStatement)
        return result
    else:
        return "An error occured. Try again"

def findAvailableBooksByTitle(bookTitle):
    sqlStatement = "SELECT * FROM Book_Info WHERE title LIKE \"%{}%\" AND member_id=0;".format(bookTitle)
    if sqlStatement:
        result=returnBookInfoData(sqlStatement)
        return result
    else:
        return "An error occured. Try again"

def findBookById(bookID):
    sqlStatement = "SELECT * FROM Book_Info WHERE id={};".format(bookID)
    if sqlStatement:
        result=returnBookInfoData(sqlStatement)
        return result
    else:
        return "No book with ID {} found".format(bookID)

def returnListOfBooks():
    sqlStatement = "SELECT * FROM Book_Info;"
    if sqlStatement:
        result=returnBookInfoData(sqlStatement)
        return result
    else:
        return "An error occured. Try again"

def showLoanHistory():
    sqlStatement = "SELECT * FROM Loan_History;"
    if sqlStatement:
        result=returnLoanHistoryData(sqlStatement)
        return result
    else:
        return "An error occured"

def updateBookStatus(bookID, memberID=None):
    if memberID:
        sqlStatement = "UPDATE Book_Info SET member_id = {} WHERE id = {};".format(memberID, bookID)
    else:
        sqlStatement = "UPDATE Book_Info SET member_id=0 WHERE id = {};".format(bookID)
    if sqlStatement:
        flag, result=RunSQLStatement(sqlStatement)
        if flag:
            return "DB updated accordingly"
        else:
            return "An error occured. Try again"
    else:
        return "An error occured. Try again"

def createLoanHistoryRecord(bookID, memberID):
    checkoutDate = str(datetime.date.today())
    returnDate = str(datetime.date.today())
    sqlStatement = "INSERT INTO Loan_History (book_id, checkout_date, return_date, member_id) VALUES ({},'{}','{}',{});".format(bookID, checkoutDate, returnDate, memberID)
    if sqlStatement:
        flag, result=RunSQLStatement(sqlStatement)
        if flag:
            return "Record Added to Loan History" 
        else:
            return "An error occured {}".format(result)
    else:
        return "An error occured. Try again."

def updateLoanHistoryReturnDate(bookID, memberID):
    returnDate = str(datetime.date.today())
    sqlStatement = "UPDATE Loan_History SET return_date='{}' WHERE book_id = {} AND member_id = {};".format(returnDate, bookID, memberID)
    if sqlStatement:
        flag, result = RunSQLStatement(sqlStatement)
        if flag:
            return "Update Successful"
        else:
            return "An error occured {}".format(result)
    else:
        return "An error occured. Try again."

def fetchPlotData():
    SQLText="""
            SELECT title, count(*) AS Number
            FROM Book_Info inner join Loan_History
            where Book_Info.id=Loan_History.book_id
            GROUP BY title
            ORDER BY Number desc;
            """

    flag,result=RunSQLStatement(SQLText)
    return flag, result
   
def PopulateDB():
    try:
        p = sp.Popen(["sqlite3", CurrentDB], stdout=sp.PIPE, stdin=sp.PIPE)
    except Exception as e:
        print("err "+e)

    try:
        stre = "CREATE TABLE IF NOT EXISTS Book_Info"\
        "(id INTEGER PRIMARY KEY,"\
        "isbn VARCHAR(10) NOT NULL,"\
        "title VARCHAR(30) NOT NULL,"\
        "author TEXT(30) NOT NULL,"\
        "purchase_date TEXT NOT NULL,"\
        "member_id INT);"\
        "\n.separator ','"\
        "\n.import Book_Info.txt Book_Info"
        print(stre)
        
        p.communicate(str.encode(stre))
    except Exception as e:
        print("err "+e)

def PopulateLoanDB():
    try:
        p = sp.Popen(["sqlite3", CurrentDB], stdout=sp.PIPE, stdin=sp.PIPE)
    except Exception as e:
        print("err "+e)

    try:
        stre = "CREATE TABLE IF NOT EXISTS Loan_History"\
        "(transaction_id INTEGER PRIMARY KEY,"\
        "book_id VARCHAR(10) NOT NULL,"\
        "checkout_date TEXT NOT NULL,"\
        "return_date TEXT,"\
        "member_id INT NOT NULL);"\
        "\n.separator ','"\
        "\n.import Loan_History.txt Loan_History"
        print(stre)
        
        p.communicate(str.encode(stre))
    except Exception as e:
        print("err "+e)
        
if __name__=='__main__':
    #######testing###############
    # print(findBookById(13))
    # print(showLoanHistory())
    # print(findBookByTitle("The Ultimate Hitchhiker's Guide"))
    # print(returnListOfBooks())
    # print(createLoanHistoryRecord(10,5238))
    # PopulateLoanDB()
    # PopulateDB()
    flag, result=RunSQLStatement("""SELECT title, count(*) AS Number
FROM Book_Info inner join Loan_History
where Book_Info.id=Loan_History.book_id
GROUP BY title
ORDER BY Number desc ;""")
    print(result)
 
            

