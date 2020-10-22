from database import *

def bookSearch(bookTitle):
    try:
        result = findBookByTitle(bookTitle)
        return result
    except Exception as err:
        return "An error occured {}".format(err)


if __name__ == "__main__":
    print(bookSearch("The Ultimate Hitchhiker's Guide"))
    