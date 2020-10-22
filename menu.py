import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import filedialog
from tkinter import ttk
import os
from booksearch import *
from bookcheckout import *
from bookreturn import *
from booklist import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

form = tk.Tk()
form.title("Library Management System")

form.geometry("800x580")

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Populate Database")
tab_parent.add(tab2, text="Search for book")
tab_parent.add(tab3, text="Checkout Book")
tab_parent.add(tab4, text="Return Book")
tab_parent.add(tab5, text="Show book popularity")

def searchBooks():
    searchScrollBox.delete('1.0',tk.END)
    bookTitle = firstEntryTabTwo.get()
    if bookTitle:
        result = bookSearch(bookTitle)
        if result:
            for i in result:
                searchScrollBox.insert(tk.END, i)
        else:
            searchScrollBox.insert(tk.END, "No book with title '{}' found".format(bookTitle))
    else:
        searchScrollBox.insert(tk.END, "Please enter book title")

def checkOutBookAction():
    checkoutScrollBox.delete('1.0',tk.END)
    bookID = firstEntryTabThree.get()
    memberID = memberIDEntryTabThree.get()
    result = checkOutBook(bookID, memberID)
    checkoutScrollBox.insert(tk.END, result)

def returnBookAction():
    returnBookScrollBox.delete('1.0', tk.END)
    bookID = firstEntryTabFour.get()
    result = returnBook(bookID)
    returnBookScrollBox.insert(tk.END, result)



# === WIDGETS FOR TAB TWO
firstLabelTabTwo = tk.Label(tab2, text="Book Title:")
firstEntryTabTwo = tk.Entry(tab2)

searchButton = tk.Button(tab2, text="Search", command=searchBooks)

searchScrollBox = scrolledtext.ScrolledText(tab2,width=100,height=30)
searchScrollBox.grid(column=0, row=5,rowspan=6, columnspan=20, padx=5, pady=5)

# === ADD WIDGETS TO GRID ON TAB TWO
firstLabelTabTwo.grid(row=0, column=0, padx=5, pady=5)
firstEntryTabTwo.grid(row=0, column=1, padx=5, pady=5)

searchButton.grid(row=0, column=3)

# === WIDGETS FOR TAB THREE
firstLabelTabThree = tk.Label(tab3, text="Book ID:")
memberIDLabelTabThree = tk.Label(tab3, text="Member ID:")

firstEntryTabThree = tk.Entry(tab3)
memberIDEntryTabThree = tk.Entry(tab3)


withdrawBook = tk.Button(tab3, text="Withdraw Book", command=checkOutBookAction)

checkoutScrollBox = scrolledtext.ScrolledText(tab3,width=100,height=30)
checkoutScrollBox.grid(column=0, row=5,rowspan=6, columnspan=20, padx=5, pady=5)

# === ADD WIDGETS TO GRID ON TAB THREE
firstLabelTabThree.grid(row=0, column=0, padx=5, pady=5)
firstEntryTabThree.grid(row=0, column=1, padx=5, pady=5)

memberIDLabelTabThree.grid(row=1, column=0, padx=5, pady=5)
memberIDEntryTabThree.grid(row=1, column=1, padx=5, pady=5)

withdrawBook.grid(row=3, column=1)


# === WIDGETS FOR TAB FOUR
firstLabelTabFour = tk.Label(tab4, text="Book ID:")
firstEntryTabFour = tk.Entry(tab4)

returnBookScrollBox = scrolledtext.ScrolledText(tab4,width=100,height=30)
returnBookScrollBox.grid(column=0, row=5,rowspan=6, columnspan=20, padx=5, pady=5)

returnBookBtn = tk.Button(tab4, text="Return Book", command=returnBookAction)

# === ADD WIDGETS TO GRID ON TAB FOUR
firstLabelTabFour.grid(row=0, column=0, padx=5, pady=5)
firstEntryTabFour.grid(row=0, column=1, padx=5, pady=5)
returnBookBtn.grid(row=1, column=1)


# === Plot GUI
# def createGraph():
#     table_names,record_count=showplot()
#     print(table_names, record_count)
#     fig = plt.figure(num=None, figsize=(4,4), dpi=50, facecolor='w', edgecolor='k')
#     plt.title("Book Popularity - Top 5 Books")
#     plt.xlabel("Books")
#     plt.ylabel("Number of Books Borrowed")
#     plt.xticks(rotation=90)

#     plt.bar(table_names, record_count)
#     plt.ylim(bottom=0)
#     return fig

def createPieChart():
    table_names,record_count=showplot()
    fig = plt.figure()
    plt.title("Book Popularity - Top 5 Books")
    # ax = fig.add_axes([0,0,1,1])
    # ax.axis('equal')
    # ax.pie(record_count, labels = table_names,autopct='%1.1f%%')
    # # plt.show(block=False)
    # return fig
    
    labels = table_names
    sizes = record_count
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.tight_layout()
    return fig
    # plt.show()

pieFig = createPieChart()

pieCanvas = FigureCanvasTkAgg(pieFig, master=tab5)
pieCanvas.draw()
pieCanvas.get_tk_widget().grid(column=0, row=5)

# fig = createGraph()

# canvas = FigureCanvasTkAgg(fig, master=tab5)
# canvas.draw()
# canvas.get_tk_widget().grid(column=0, row=0)

tab_parent.pack(expand=1, fill='both')
form.mainloop()