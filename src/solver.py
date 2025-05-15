from tkinter import Tk, Frame, Entry, Grid, ttk, StringVar, Canvas
from tkinter.ttk import Style

class Solver_Config():
    def __init__(self):
        self._root = Tk()
        self._root.title('Nonogram Solver')
        self._col_row = StringVar()
        self.lst = StringVar()
        self._col_row_lst = [[], []]

        self.label_font = ('Arial', 12)
        self.header_font = ('Arial', 14, 'bold')
        self.button_font = ('Arial', 12)
        self.entry_font = ('Arial', 12)
        self.frame_width = 400
        
        self._display_frame = ttk.Frame(self._root)
        self._display_frame.grid(column=0, row=0)
        self._build_display_frame()
        
        self._entry_frame = ttk.Frame(self._root)
        self._entry_frame.grid(column=0, row=1)
        self._build_entry_frame()
        
        self.run()

    def run(self):
        self._root.mainloop()
        

    def _build_display_frame(self):
        # Define frame style
        style = ttk.Style()
        style.configure('TLabelframe.Label', font=self.header_font)

        # Column Frame Set up
        self.col_display = ttk.Labelframe(
            self._display_frame, text='Columns', width=self.frame_width
        )
        self.col_display.grid(column=0, row=0, sticky='we', padx=10, pady=5)
        #self.col_display.grid_propagate(False)
        self.col_display.config(width=self.frame_width, height=100)
        # Row Frame Set up
        self.row_display = ttk.Labelframe(
            self._display_frame, text='Rows', width=self.frame_width
        )
        self.row_display.grid(column=0, row=1, sticky='we', padx=10, pady=5)
        #self.row_display.grid_propagate(False)
        self.row_display.config(width=self.frame_width, height=100)

        # Add empty space
        ttk.Label(
            self.col_display, text='', font=self.label_font, width=20
        ).grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(
            self.row_display, text='', font=self.label_font, width=20
        ).grid(column=0, row=0, padx=5, pady=5)
    
    def _fill_display_frame(self):
        # Clean Up Window
        for widget in self.col_display.winfo_children():
            widget.destroy()
        for widget in self.row_display.winfo_children():
            widget.destroy()

        # Display column data
        for e, col_list in enumerate(self._col_row_lst[0]):
            ttk.Label(
                self.col_display, text=col_list, font=self.label_font
            ).grid(column=0, row=e, padx=5, pady=2)

        # Display row data
        for e, col_list in enumerate(self._col_row_lst[1]):
            ttk.Label(
                self.row_display, text=col_list, font=self.label_font
            ).grid(column=0,row=e, padx=5, pady=2)
            

    def _build_entry_frame(self):
        radio_frame = ttk.Frame(self._entry_frame)
        radio_frame.grid(column=0, row=0, columnspan=3, pady=5)

        ttk.Radiobutton(
            radio_frame, text='Column', variable=self._col_row, value='1',
            style='TRadiobutton', padding=5
        ).grid(column=0, row=0, padx=10)
        ttk.Radiobutton(
            radio_frame, text='Row', variable=self._col_row, value='2',
            style='TRadiobutton', padding=5
        ).grid(column=1, row=0, padx=10)

        self._col_row.set('1')

        style = ttk.Style()
        style.configure('TRadiobutton', font=self.label_font)
        style.configure('TButton', font=self.button_font, padding=5)

        ttk.Label(
            self._entry_frame,
            text='List numbers in column or row. ex: 2,10,1,2',
            font=self.label_font
        ).grid(
            column=0, row=1, columnspan=3, padx=10, pady=5
        )

        lst_entry = ttk.Entry(
            self._entry_frame, width=30, textvariable=self.lst, font=self.entry_font
        )
        lst_entry.grid(column=0, row=2, columnspan=3, sticky='we', padx=10, pady=5)

        #lst_entry.bind("<KeyRelease>", self.print_entry_text)

        button_frame = ttk.Frame(self._entry_frame)
        button_frame.grid(column=0, row=3, columnspan=3, pady=5)
        ttk.Button(
            button_frame, text='Confirm Row/Column',
            command=self._set_list, style='TButton'
        ).grid(column=1, row=3, padx=5)

        ttk.Button(
            button_frame, text='Solve!',
            command=self._solve, style='TButton'
        ).grid(column=2, row=3, padx=5)


    def _set_list(self):
        _lst = self.lst.get()
        print(f'Sent list: {_lst}')
        try:
            int_list = [int(num.strip()) for num in _lst.split(',')]
            print(f'Converted list: {int_list}')
            print(f'Button value: {self._col_row.get()}')
            button_val = self._col_row.get()
            if button_val == '1':
                self._col_row_lst[0].append(int_list)
            elif button_val == '2':
                self._col_row_lst[1].append(int_list)
            else:
                print('Check fail')
            self._fill_display_frame()
            self.lst.set('')
            print(f'Col/Row list: {self._col_row_lst}')
        except ValueError:
            print("Invalid input format.")

    def print_entry_text(self, *kwargs):
        text = self.lst.get()
        print(text)

    def _solve(self):
        pass

class Solver_Window():
    pass