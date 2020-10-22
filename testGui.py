# # import tkinter as tk

# # class Example(tk.Frame):
# #     def __init__(self, parent):
# #         tk.Frame.__init__(self, parent)
# #         b = tk.Button(self, text="Done!", command=self.upload_cor)
# #         b.pack()
# #         table = tk.Frame(self)
# #         table.pack(side="top", fill="both", expand=True)

# #         data = (
# #             (45417, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45418, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45419, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45420, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45421, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45422, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #             (45423, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
# #         )

# #         self.widgets = {}
# #         row = 0
# #         for rowid, reviewer, task, num_seconds, start_time, end_time in (data):
# #             row += 1
# #             self.widgets[rowid] = {
# #                 "rowid": tk.Label(table, text=rowid),
# #                 "reviewer": tk.Label(table, text=reviewer),
# #                 "task": tk.Label(table, text=task),
# #                 "num_seconds_correction": tk.Entry(table),
# #                 "num_seconds": tk.Label(table, text=num_seconds),
# #                 "start_time": tk.Label(table, text=start_time),
# #                 "end_time": tk.Label(table, text=start_time)
# #             }

# #             self.widgets[rowid]["rowid"].grid(row=row, column=0, sticky="nsew")
# #             self.widgets[rowid]["reviewer"].grid(row=row, column=1, sticky="nsew")
# #             self.widgets[rowid]["task"].grid(row=row, column=2, sticky="nsew")
# #             self.widgets[rowid]["num_seconds_correction"].grid(row=row, column=3, sticky="nsew")
# #             self.widgets[rowid]["num_seconds"].grid(row=row, column=4, sticky="nsew")
# #             self.widgets[rowid]["start_time"].grid(row=row, column=5, sticky="nsew")
# #             self.widgets[rowid]["end_time"].grid(row=row, column=6, sticky="nsew")

# #         table.grid_columnconfigure(1, weight=1)
# #         table.grid_columnconfigure(2, weight=1)
# #         # invisible row after last row gets all extra space
# #         table.grid_rowconfigure(row+1, weight=1)

# #     def upload_cor(self):
# #         for rowid in sorted(self.widgets.keys()):
# #             entry_widget = self.widgets[rowid]["num_seconds_correction"]
# #             new_value = entry_widget.get()
# #             print("%s: %s" % (rowid, new_value))

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     Example(root).pack(fill="both", expand=True)
# #     root.mainloop()


# # Author: Miguel Martinez Lopez
# # Version: 0.20

# try:
#     from Tkinter import Frame, Label, Message, StringVar, Canvas
#     from ttk import Scrollbar
#     from Tkconstants import *
# except ImportError:
#     from tkinter import Frame, Label, Message, StringVar, Canvas
#     from tkinter.ttk import Scrollbar
#     from tkinter.constants import *

# import platform

# OS = platform.system()

# class Mousewheel_Support(object):    

#     # implemetation of singleton pattern
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = object.__new__(cls)
#         return cls._instance

#     def __init__(self, root, horizontal_factor = 2, vertical_factor=2):
        
#         self._active_area = None
        
#         if isinstance(horizontal_factor, int):
#             self.horizontal_factor = horizontal_factor
#         else:
#             raise Exception("Vertical factor must be an integer.")

#         if isinstance(vertical_factor, int):
#             self.vertical_factor = vertical_factor
#         else:
#             raise Exception("Horizontal factor must be an integer.")

#         if OS == "Linux" :
#             root.bind_all('<4>', self._on_mousewheel,  add='+')
#             root.bind_all('<5>', self._on_mousewheel,  add='+')
#         else:
#             # Windows and MacOS
#             root.bind_all("<MouseWheel>", self._on_mousewheel,  add='+')

#     def _on_mousewheel(self,event):
#         if self._active_area:
#             self._active_area.onMouseWheel(event)

#     def _mousewheel_bind(self, widget):
#         self._active_area = widget

#     def _mousewheel_unbind(self):
#         self._active_area = None

#     def add_support_to(self, widget=None, xscrollbar=None, yscrollbar=None, what="units", horizontal_factor=None, vertical_factor=None):
#         if xscrollbar is None and yscrollbar is None:
#             return

#         if xscrollbar is not None:
#             horizontal_factor = horizontal_factor or self.horizontal_factor

#             xscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget,'x', self.horizontal_factor, what)
#             xscrollbar.bind('<Enter>', lambda event, scrollbar=xscrollbar: self._mousewheel_bind(scrollbar) )
#             xscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

#         if yscrollbar is not None:
#             vertical_factor = vertical_factor or self.vertical_factor

#             yscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget,'y', self.vertical_factor, what)
#             yscrollbar.bind('<Enter>', lambda event, scrollbar=yscrollbar: self._mousewheel_bind(scrollbar) )
#             yscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

#         main_scrollbar = yscrollbar if yscrollbar is not None else xscrollbar
        
#         if widget is not None:
#             if isinstance(widget, list) or isinstance(widget, tuple):
#                 list_of_widgets = widget
#                 for widget in list_of_widgets:
#                     widget.bind('<Enter>',lambda event: self._mousewheel_bind(widget))
#                     widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

#                     widget.onMouseWheel = main_scrollbar.onMouseWheel
#             else:
#                 widget.bind('<Enter>',lambda event: self._mousewheel_bind(widget))
#                 widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

#                 widget.onMouseWheel = main_scrollbar.onMouseWheel

#     @staticmethod
#     def _make_mouse_wheel_handler(widget, orient, factor = 1, what="units"):
#         view_command = getattr(widget, orient+'view')
        
#         if OS == 'Linux':
#             def onMouseWheel(event):
#                 if event.num == 4:
#                     view_command("scroll",(-1)*factor, what)
#                 elif event.num == 5:
#                     view_command("scroll",factor, what) 
                
#         elif OS == 'Windows':
#             def onMouseWheel(event):        
#                 view_command("scroll",(-1)*int((event.delta/120)*factor), what) 
        
#         elif OS == 'Darwin':
#             def onMouseWheel(event):        
#                 view_command("scroll",event.delta, what)
        
#         return onMouseWheel

# class Scrolling_Area(Frame, object):

#     def __init__(self, master, width=None, anchor=N, height=None, mousewheel_speed = 2, scroll_horizontally=True, xscrollbar=None, scroll_vertically=True, yscrollbar=None, outer_background=None, inner_frame=Frame, **kw):
#         Frame.__init__(self, master, class_=self.__class__)

#         if outer_background:
#             self.configure(background=outer_background)

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
        
#         self._width = width
#         self._height = height

#         self.canvas = Canvas(self, background=outer_background, highlightthickness=0, width=width, height=height)
#         self.canvas.grid(row=0, column=0, sticky=N+E+W+S)

#         if scroll_vertically:
#             if yscrollbar is not None:
#                 self.yscrollbar = yscrollbar
#             else:
#                 self.yscrollbar = Scrollbar(self, orient=VERTICAL)
#                 self.yscrollbar.grid(row=0, column=1,sticky=N+S)
        
#             self.canvas.configure(yscrollcommand=self.yscrollbar.set)
#             self.yscrollbar['command']=self.canvas.yview
#         else:
#             self.yscrollbar = None

#         if scroll_horizontally:
#             if xscrollbar is not None:
#                 self.xscrollbar = xscrollbar
#             else:
#                 self.xscrollbar = Scrollbar(self, orient=HORIZONTAL)
#                 self.xscrollbar.grid(row=1, column=0, sticky=E+W)
            
#             self.canvas.configure(xscrollcommand=self.xscrollbar.set)
#             self.xscrollbar['command']=self.canvas.xview
#         else:
#             self.xscrollbar = None

#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
        
#         self.innerframe = inner_frame(self.canvas, **kw)
#         self.innerframe.pack(anchor=anchor)
        
#         self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")

#         self.canvas.bind('<Configure>', self._on_canvas_configure)

#         Mousewheel_Support(self).add_support_to(self.canvas, xscrollbar=self.xscrollbar, yscrollbar=self.yscrollbar)

#     @property
#     def width(self):
#         return self.canvas.winfo_width()

#     @width.setter
#     def width(self, width):
#         self.canvas.configure(width= width)

#     @property
#     def height(self):
#         return self.canvas.winfo_height()
        
#     @height.setter
#     def height(self, height):
#         self.canvas.configure(height = height)
        
#     def set_size(self, width, height):
#         self.canvas.configure(width=width, height = height)

#     def _on_canvas_configure(self, event):
#         width = max(self.innerframe.winfo_reqwidth(), event.width)
#         height = max(self.innerframe.winfo_reqheight(), event.height)

#         self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
#         self.canvas.itemconfigure("inner_frame", width=width, height=height)

#     def update_viewport(self):
#         self.update()

#         window_width = self.innerframe.winfo_reqwidth()
#         window_height = self.innerframe.winfo_reqheight()
        
#         if self._width is None:
#             canvas_width = window_width
#         else:
#             canvas_width = min(self._width, window_width)
            
#         if self._height is None:
#             canvas_height = window_height
#         else:
#             canvas_height = min(self._height, window_height)

#         self.canvas.configure(scrollregion="0 0 %s %s" % (window_width, window_height), width=canvas_width, height=canvas_height)
#         self.canvas.itemconfigure("inner_frame", width=window_width, height=window_height)

# class Cell(Frame):
#     """Base class for cells"""

# class Data_Cell(Cell):
#     def __init__(self, master, variable, anchor=W, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None, foreground=None, font=None):
#         Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=borderwidth, bd= 0)

#         self._message_widget = Message(self, textvariable=variable, font=font, background=background, foreground=foreground)
#         self._message_widget.pack(expand=True, padx=padx, pady=pady, anchor=anchor)

# class Header_Cell(Cell):
#     def __init__(self, master, text, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None, foreground=None, font=None, anchor=CENTER, separator=True):
#         Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=borderwidth, bd= 0)
#         self.pack_propagate(False)

#         self._header_label = Label(self, text=text, background=background, foreground=foreground, font=font)
#         self._header_label.pack(padx=padx, pady=pady, expand=True)

#         if separator and bordercolor is not None:
#             separator = Frame(self, height=2, background=bordercolor, bd=0, highlightthickness=0, class_="Separator")
#             separator.pack(fill=X, anchor=anchor)

#         self.update()
#         height = self._header_label.winfo_reqheight() + 2*padx
#         width = self._header_label.winfo_reqwidth() + 2*pady

#         self.configure(height=height, width=width)
        
# class Table(Frame):
#     def __init__(self, master, columns, column_weights=None, column_minwidths=None, height=500, minwidth=20, minheight=20, padx=5, pady=5, cell_font=None, cell_foreground="black", cell_background="white", cell_anchor=W, header_font=None, header_background="white", header_foreground="black", header_anchor=CENTER, bordercolor = "#999999", innerborder=True, outerborder=True, stripped_rows=("#EEEEEE", "white"), on_change_data=None, mousewheel_speed = 2, scroll_horizontally=False, scroll_vertically=True):
#         outerborder_width = 1 if outerborder else 0

#         Frame.__init__(self,master, bd= 0)

#         self._cell_background = cell_background
#         self._cell_foreground = cell_foreground
#         self._cell_font = cell_font
#         self._cell_anchor = cell_anchor
        
#         self._stripped_rows = stripped_rows

#         self._padx = padx
#         self._pady = pady
        
#         self._bordercolor = bordercolor
#         self._innerborder_width = 1 if innerborder else 0

#         self._data_vars = []

#         self._columns = columns
        
#         self._number_of_rows = 0
#         self._number_of_columns = len(columns)

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(1, weight=1)
        
#         self._head = Frame(self, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
#         self._head.grid(row=0, column=0, sticky=E+W)

#         header_separator = False if outerborder else True

#         for j in range(len(columns)):
#             column_name = columns[j]

#             header_cell = Header_Cell(self._head, text=column_name, borderwidth=self._innerborder_width, font=header_font, background=header_background, foreground=header_foreground, padx=padx, pady=pady, bordercolor=bordercolor, anchor=header_anchor, separator=header_separator)
#             header_cell.grid(row=0, column=j, sticky=N+E+W+S)

#         add_scrollbars = scroll_horizontally or scroll_vertically
#         if add_scrollbars:
#             if scroll_horizontally:
#                 xscrollbar = Scrollbar(self, orient=HORIZONTAL)
#                 xscrollbar.grid(row=2, column=0, sticky=E+W)
#             else:
#                 xscrollbar = None

#             if scroll_vertically:
#                 yscrollbar = Scrollbar(self, orient=VERTICAL)
#                 yscrollbar.grid(row=1, column=1, sticky=N+S)
#             else:
#                 yscrollbar = None

#             scrolling_area = Scrolling_Area(self, width=self._head.winfo_reqwidth(), height=height, scroll_horizontally=scroll_horizontally, xscrollbar=xscrollbar, scroll_vertically=scroll_vertically, yscrollbar=yscrollbar)
#             scrolling_area.grid(row=1, column=0, sticky=E+W)

#             self._body = Frame(scrolling_area.innerframe, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
#             self._body.pack()
            
#             def on_change_data():
#                 scrolling_area.update_viewport()

#         else:
#             self._body = Frame(self, height=height, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
#             self._body.grid(row=1, column=0, sticky=N+E+W+S)

#         if column_weights is None:
#             for j in range(len(columns)):
#                 self._body.grid_columnconfigure(j, weight=1)
#         else:
#             for j, weight in enumerate(column_weights):
#                 self._body.grid_columnconfigure(j, weight=weight)

#         if column_minwidths is not None:
#             for j, minwidth in enumerate(column_minwidths):
#                 if minwidth is None:
#                     header_cell = self._head.grid_slaves(row=0, column=j)[0]
#                     minwidth = header_cell.winfo_reqwidth()

#                 self._body.grid_columnconfigure(j, minsize=minwidth)
#         else:
#             for j in range(len(columns)):
#                 header_cell = self._head.grid_slaves(row=0, column=j)[0]
#                 minwidth = header_cell.winfo_reqwidth()

#                 self._body.grid_columnconfigure(j, minsize=minwidth)

#         self._on_change_data = on_change_data

#     def _append_n_rows(self, n):
#         number_of_rows = self._number_of_rows
#         number_of_columns = self._number_of_columns

#         for i in range(number_of_rows, number_of_rows+n):
#             list_of_vars = []
#             for j in range(number_of_columns):
#                 var = StringVar()
#                 list_of_vars.append(var)

#                 if self._stripped_rows:
#                     cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._stripped_rows[i%2], foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)
#                 else:
#                     cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._cell_background, foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)

#                 cell.grid(row=i, column=j, sticky=N+E+W+S)

#             self._data_vars.append(list_of_vars)
            
#         if number_of_rows == 0:
#             for j in range(self.number_of_columns):
#                 header_cell = self._head.grid_slaves(row=0, column=j)[0]
#                 data_cell = self._body.grid_slaves(row=0, column=j)[0]
#                 data_cell.bind("<Configure>", lambda event, header_cell=header_cell: header_cell.configure(width=event.width), add="+")

#         self._number_of_rows += n

#     def _pop_n_rows(self, n):
#         number_of_rows = self._number_of_rows
#         number_of_columns = self._number_of_columns
        
#         for i in range(number_of_rows-n, number_of_rows):
#             for j in range(number_of_columns):
#                 self._body.grid_slaves(row=i, column=j)[0].destroy()
            
#             self._data_vars.pop()
    
#         self._number_of_rows -= n

#     def set_data(self, data):
#         n = len(data)
#         m = len(data[0])

#         number_of_rows = self._number_of_rows

#         if number_of_rows > n:
#             self._pop_n_rows(number_of_rows-n)
#         elif number_of_rows < n:
#             self._append_n_rows(n-number_of_rows)

#         for i in range(n):
#             for j in range(m):
#                 self._data_vars[i][j].set(data[i][j])

#         if self._on_change_data is not None: self._on_change_data()

#     def get_data(self):
#         number_of_rows = self._number_of_rows
#         number_of_columns = self.number_of_columns
        
#         data = []
#         for i in range(number_of_rows):
#             row = []
#             row_of_vars = self._data_vars[i]
#             for j in range(number_of_columns):
#                 cell_data = row_of_vars[j].get()
#                 row.append(cell_data)
            
#             data.append(row)
#         return data

#     @property
#     def number_of_rows(self):
#         return self._number_of_rows

#     @property
#     def number_of_columns(self):
#         return self._number_of_columns

#     def row(self, index, data=None):
#         if data is None:
#             row = []
#             row_of_vars = self._data_vars[index]

#             for j in range(self.number_of_columns):
#                 row.append(row_of_vars[j].get())
                
#             return row
#         else:
#             number_of_columns = self.number_of_columns
            
#             if len(data) != number_of_columns:
#                 raise ValueError("data has no %d elements: %s"%(number_of_columns, data))

#             row_of_vars = self._data_vars[index]
#             for j in range(number_of_columns):
#                 row_of_vars[index][j].set(data[j])
                
#             if self._on_change_data is not None: self._on_change_data()

#     def column(self, index, data=None):
#         number_of_rows = self._number_of_rows

#         if data is None:
#             column= []

#             for i in range(number_of_rows):
#                 column.append(self._data_vars[i][index].get())
                
#             return column
#         else:            
#             if len(data) != number_of_rows:
#                 raise ValueError("data has no %d elements: %s"%(number_of_rows, data))

#             for i in range(number_of_columns):
#                 self._data_vars[i][index].set(data[i])

#             if self._on_change_data is not None: self._on_change_data()

#     def clear(self):
#         number_of_rows = self._number_of_rows
#         number_of_columns = self._number_of_columns

#         for i in range(number_of_rows):
#             for j in range(number_of_columns):
#                 self._data_vars[i][j].set("")

#         if self._on_change_data is not None: self._on_change_data()

#     def delete_row(self, index):
#         i = index
#         while i < self._number_of_rows:
#             row_of_vars_1 = self._data_vars[i]
#             row_of_vars_2 = self._data_vars[i+1]

#             j = 0
#             while j <self.number_of_columns:
#                 row_of_vars_1[j].set(row_of_vars_2[j])

#             i += 1

#         self._pop_n_rows(1)

#         if self._on_change_data is not None: self._on_change_data()

#     def insert_row(self, data, index=END):
#         self._append_n_rows(1)

#         if index == END:
#             index = self._number_of_rows - 1
        
#         i = self._number_of_rows-1
#         while i > index:
#             row_of_vars_1 = self._data_vars[i-1]
#             row_of_vars_2 = self._data_vars[i]

#             j = 0
#             while j < self.number_of_columns:
#                 row_of_vars_2[j].set(row_of_vars_1[j])
#                 j += 1
#             i -= 1

#         list_of_cell_vars = self._data_vars[index]
#         for cell_var, cell_data in zip(list_of_cell_vars, data):
#             cell_var.set(cell_data)

#         if self._on_change_data is not None: self._on_change_data()

#     def cell(self, row, column, data=None):
#         """Get the value of a table cell"""
#         if data is None:
#             return self._data_vars[row][column].get()
#         else:
#             self._data_vars[row][column].set(data)
#             if self._on_change_data is not None: self._on_change_data()

#     def __getitem__(self, index):
#         if isinstance(index, tuple):
#             row, column = index
#             return self.cell(row, column)
#         else:
#             raise Exception("Row and column indices are required")
        
#     def __setitem__(self, index, value):
#         if isinstance(index, tuple):
#             row, column = index
#             self.cell(row, column, value)
#         else:
#             raise Exception("Row and column indices are required")

#     def on_change_data(self, callback):
#         self._on_change_data = callback

# if __name__ == "__main__":
#     try:
#         from Tkinter import Tk
#     except ImportError:
#         from tkinter import Tk

#     root = Tk()

#     table = Table(root, ["column A", "column B", "column C"], column_minwidths=[None, None, None])
#     table.pack(padx=10,pady=10)

#     table.set_data([[1,2,3],[4,5,6], [7,8,9], [10,11,12], [13,14,15],[15,16,18], [19,20,21]])
#     table.cell(0,0, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")
    
#     table.insert_row([22,23,24])
#     table.insert_row([25,26,27])
    
#     root.update()
#     root.geometry("%sx%s"%(root.winfo_reqwidth(),250))

#     root.mainloop()

# from tkinter import *
  
  
# class Table: 
      
#     def __init__(self,root): 
          
#         # code for creating table 
#         for i in range(total_rows): 
#             for j in range(total_columns): 
                  
#                 self.e = Entry(root, width=20, fg='blue', 
#                                font=('Arial',16,'bold')) 
                  
#                 self.e.grid(row=i, column=j) 
#                 self.e.insert(END, lst[i][j]) 
  
# # take the data 
# lst = [(1,'Raj','Mumbai',19), 
#        (2,'Aaryan','Pune',18), 
#        (3,'Vaishnavi','Mumbai',20), 
#        (4,'Rachna','Mumbai',21), 
#        (5,'Shubham','Delhi',21)] 
   
# # find total number of rows and 
# # columns in list 
# total_rows = len(lst) 
# total_columns = len(lst[0]) 
   
# # create root window 
# root = Tk() 
# t = Table(root) 
# root.mainloop() 

# import tkinter as Tkinter
# import tkinter.font as tkFont
# import tkinter.ttk as ttk

# class Picker(ttk.Frame):

#     def __init__(self, master=None,activebackground='#b1dcfb',values=[],entry_wid=None,activeforeground='black', selectbackground='#003eff', selectforeground='white', command=None, borderwidth=1, relief="solid"):

#         self._selected_item = None

#         self._values = values

#         self._entry_wid = entry_wid

#         self._sel_bg = selectbackground 
#         self._sel_fg = selectforeground

#         self._act_bg = activebackground 
#         self._act_fg = activeforeground

#         self._command = command
#         ttk.Frame.__init__(self, master, borderwidth=borderwidth, relief=relief)

#         self.bind("<FocusIn>", lambda event:self.event_generate('<<PickerFocusIn>>'))
#         self.bind("<FocusOut>", lambda event:self.event_generate('<<PickerFocusOut>>'))

#         self._font = tkFont.Font()

#         self.dict_checkbutton = {}
#         self.dict_checkbutton_var = {}
#         self.dict_intvar_item = {}

#         for index,item in enumerate(self._values):

#             self.dict_intvar_item[item] = Tkinter.IntVar()
#             self.dict_checkbutton[item] = ttk.Checkbutton(self, text = item, variable=self.dict_intvar_item[item],command=lambda ITEM = item:self._command(ITEM))
#             self.dict_checkbutton[item].grid(row=index, column=0, sticky=Tkinter.NSEW)
#             self.dict_intvar_item[item].set(0)


# class Combopicker(ttk.Entry, Picker):
#     def __init__(self, master, values= [] ,entryvar=None, entrywidth=None, entrystyle=None, onselect=None,activebackground='#b1dcfb', activeforeground='black', selectbackground='#003eff', selectforeground='white', borderwidth=1, relief="solid"):

#         if entryvar is not None:
#             self.entry_var = entryvar
#         else:
#             self.entry_var = Tkinter.StringVar()

#         entry_config = {}
#         if entrywidth is not None:
#             entry_config["width"] = entrywidth

#         if entrystyle is not None:
#             entry_config["style"] = entrystyle

#         ttk.Entry.__init__(self, master, textvariable=self.entry_var, **entry_config, state = "readonly")

#         self._is_menuoptions_visible = False

#         self.picker_frame = Picker(self.winfo_toplevel(), values=values,entry_wid = self.entry_var,activebackground=activebackground, activeforeground=activeforeground, selectbackground=selectbackground, selectforeground=selectforeground, command=self._on_selected_check)

#         self.bind_all("<1>", self._on_click, "+")

#         self.bind("<Escape>", lambda event: self.hide_picker())

#     @property
#     def current_value(self):
#         try:
#             value = self.entry_var.get()
#             return value
#         except ValueError:
#             return None

#     @current_value.setter
#     def current_value(self, INDEX):
#         self.entry_var.set(values.index(INDEX))

#     def _on_selected_check(self, SELECTED):

#         value = []
#         if self.entry_var.get() != "" and self.entry_var.get() != None:
#             temp_value = self.entry_var.get()
#             value = temp_value.split(",")

#         if str(SELECTED) in value:
#             value.remove(str(SELECTED))

#         else:    
#             value.append(str(SELECTED))

#         value.sort()

#         temp_value = ""
#         for index,item in enumerate(value):
#             if item!= "":
#                 if index != 0:
#                     temp_value += ","
#                 temp_value += str(item)

#         self.entry_var.set(temp_value)

#     def _on_click(self, event):
#         str_widget = str(event.widget)

#         if str_widget == str(self):
#             if not self._is_menuoptions_visible:
#                 self.show_picker()
#         else:
#             if not str_widget.startswith(str(self.picker_frame)) and self._is_menuoptions_visible:
#                 self.hide_picker()

#     def show_picker(self):
#         if not self._is_menuoptions_visible:
#             self.picker_frame.place(in_=self, relx=0, rely=1, relwidth=1 )
#             self.picker_frame.lift()

#         self._is_menuoptions_visible = True

#     def hide_picker(self):
#         if self._is_menuoptions_visible:
#             self.picker_frame.place_forget()

#         self._is_menuoptions_visible = False

# if __name__ == "__main__":
#     import sys

#     try:
#         from Tkinter import Tk, Frame, Label
#     except ImportError:
#         from tkinter import Tk, Frame, Label

#     root = Tk()
#     root.geometry("500x600")

#     main =Frame(root, pady =15, padx=15)
#     main.pack(expand=True, fill="both")

#     Label(main, justify="left", text=__doc__).pack(anchor="w", pady=(0,15))

#     COMBOPICKER1 = Combopicker(main, values = [1, 2, 3, 4])
#     COMBOPICKER1.pack(anchor="w")


#     if 'win' not in sys.platform:
#         style = ttk.Style()
#         style.theme_use('clam')

#     root.mainloop()

# from tkinter import *
# from tkinter import ttk
import tkinter as tk

# main = Tk()
# main.title("Multiple Choice Listbox")
# main.geometry("+50+150")
# frame = ttk.Frame(main, padding=(3, 3, 12, 12))
# frame.grid(column=0, row=0, sticky=(N, S, E, W))

# valores = StringVar()
# valores.set("Carro Coche Moto Bici Triciclo Patineta Patin Patines Lancha Patrullas")

# lstbox = Listbox(frame, listvariable=valores, selectmode=MULTIPLE, width=20, height=10)
# lstbox.grid(column=0, row=0, columnspan=2)

# def select():
#     reslist = list()
#     seleccion = lstbox.curselection()
#     for i in seleccion:
#         entrada = lstbox.get(i)
#         reslist.append(entrada)
#     for val in reslist:
#         print(val)

# btn = ttk.Button(frame, text="Choices", command=select)
# btn.grid(column=1, row=1)

# main.mainloop()

# class CheckOut(tk.Frame): #check out page

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         #create and place base widgets
#         backGroundPicture = ImageTk.PhotoImage(Image.open("Background.jpg"))
#         backGroundLabel = tk.Label(self, image=backGroundPicture, borderwidth=0)
#         backGroundLabel.image = backGroundPicture
#         backGroundLabel.place(x=0, y=0, anchor=tk.NW)

#         checkOutLabel = tk.Label(self, text="Check Out", font=("Verdana", 48), bg="#001f33", fg="red")
#         checkOutLabel.place(relx=0.5, rely=0, anchor=tk.N)

#         returnButton = tk.Button(self, text="Return to Main Menu", bg="#4db8ff", fg="black",
#                         command=lambda: controller.show_frame(StartPage))
#         returnButton.place(relx=1, rely=1, anchor=tk.SE)

#     def update(): #add new widgets displaying items purchase
#         print("debug")
#         itemLists = []
#         for each in movieTitles:
#             i = movieTitles.index(each)
#             if(adultTickets[i] != 0):
#                 tempLabel = tk.Label(self, text="Adult Ticket: " + str(adultTickets[i]) + " " + each)
#                 itemLists.append(tempLabel)
#             if(childTickets[i] != 0):
#                 tempLabel = tk.Label(self, text="Child Ticket: " + str(childTickets[i]) + " " + each)
#                 itemLists.append(tempLabel)
#         for i in itemLists:
#             i.place(x=100, y=200, anchor=tk.CENTER)
#         print(itemLists)

# from tkinter import *
# from tkinter import ttk
# from sys import argv
# import glob
# import os

# search_input = argv
# #code in question
# def find_files():
#     for dirname, dirnames, filenames in os.walk('/home'):
#         for i in glob.glob('/*'+searchinput):
#             listbox.insert(END, search_input)

# #Code in question

# main = Tk()
# main.title("FSX")
# main.geometry('640x480')

# frame1 = ttk.Frame(main, height=200, width=400)
# frame1.pack()

# entry = Entry(frame1, width=30)
# entry.pack()

# button1 = ttk.Button(frame1, text="Search", command=find_files)
# button1.pack()
# button1.bind ('<ButtonPress>', lambda e: progressbar.start())

# button2 = ttk.Button(frame1, text="Quit")
# button2.pack()
# button2.bind ('<ButtonPress>', lambda e: exit())

# progressbar = ttk.Progressbar(frame1, orient = HORIZONTAL, length = 200,      mode = 'indeterminate')
# progressbar.pack()
# #progressbar.start()

# frame2 = ttk.Frame(main, height=200, width=400)
# frame2.pack()

# listbox = Listbox(frame2, height=200, width=400)
# listbox.pack(fill=BOTH, expand=YES)

# progressbar.stop()

# main.mainloop()

'''
Here the TreeView widget is configured as a multi-column listbox
with adjustable column width and column-header-click sorting.
'''
try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        s = """\click on header to sort by that column
to change width of column drag boundary
        """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=car_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in car_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

# the test data ...

car_header = ['car', 'repair']
car_list = [
('Hyundai', 'brakes') ,
('Honda', 'light') ,
('Lexus', 'battery') ,
('Benz', 'wiper') ,
('Ford', 'tire') ,
('Chevy', 'air') ,
('Chrysler', 'piston') ,
('Toyota', 'brake pedal') ,
('BMW', 'seat')
]


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox()
    root.mainloop()