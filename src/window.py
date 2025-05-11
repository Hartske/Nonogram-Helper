from tkinter import Tk, Frame, Entry, Grid, ttk, StringVar, Canvas
from tkinter.ttk import Style
from remainder import find_remainder, check_overlap, mark
from square import Square

class Window():
    def __init__(self):
        self._root = Tk()
        self._root.title("Nonogram Helper")
        self._root.grid()
        self.length = StringVar(value=0)
        self.remainder = StringVar(value=0)
        self.lst = StringVar(value=0)
        self.overlap = StringVar(value='False')
        self.error = StringVar()

        # Make entry frame container and call build method
        self._entry_frame = ttk.Frame(
            self._root, borderwidth=2, relief='solid'
        )
        self._entry_frame.grid(column=0, row=0, ipadx=15, ipady=15, padx=25, sticky='e')
        self._build_entry_frame()

        # Make result frame container and call build method
        self._result_frame = ttk.Frame(
            self._root, borderwidth=2, relief='solid'
        )
        self._result_frame.grid(column=1, row=0, ipadx=15, ipady=15, padx=25, sticky='w')
        self._build_result_frame()

        # Make display frame and call build method
        self._display_frame = ttk.Frame(
            self._root,).grid(column=0, row=1, columnspan=2, sticky='we'
        )
        self._build_display_frame()

        # Configure layout
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(1, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=2)
        # Focus and run
        self.run()

    def run(self):
        self._root.mainloop()
    
    def _build_entry_frame(self):
        # Text label for length entry window
        ttk.Label(
            self._entry_frame, text='Length of the column or row: ', font=('Arial', 20)
        ).grid(
            column=0, row=0, sticky='e'
        )

        # Entry field for length of column or row
        self.length_entry = ttk.Entry(
            self._entry_frame, width=8, textvariable=self.length, font=('Arial', 20)
        )
        self.length_entry.grid(column=1, row=0, sticky='w')

        # Text label for list entry window
        ttk.Label(
            self._entry_frame,
            text='List numbers in column or row. ex: 2,10,1,2', font=('Arial', 20)
        ).grid(
            column=0, row=1, columnspan=2, padx=20
        )

        # Entry field for list of numbers
        lst_entry = ttk.Entry(
            self._entry_frame, width=24, textvariable=self.lst, font=('Arial', 20)
        )
        lst_entry.grid(column=0, row=2, columnspan=2, sticky='we', padx=20)

        # Create button
        ttk.Button(
            self._entry_frame,
            text='Find Remainder', command=self._find_remainder
        ).grid(column=0, row=3, columnspan=2)

        self.length_entry.focus()
        # Configure entry frame
        self._entry_frame.columnconfigure(0, weight=1)
        self._entry_frame.columnconfigure(1, weight=1)
        self._entry_frame.rowconfigure(0, weight=1)
        self._entry_frame.rowconfigure(1, weight=1)
        self._entry_frame.rowconfigure(2, weight=1)
        self._entry_frame.rowconfigure(3, weight=1)

    def _build_result_frame(self):
        rem = self.remainder.get()

        # Remaining label and value
        ttk.Label(
            self._result_frame, text='Remaining squares: ', font=('Arial', 20)
        ).grid(column=0, row=0, sticky='e')

        label_remainder = ttk.Label(
            self._result_frame, textvariable=self.remainder, font=('Arial', 20)
        ).grid(column=1, row=0, sticky='w')

        # Overlapping squares and value
        ttk.Label(
            self._result_frame, text='Overlapping squares?: ', font=('Arial', 20, )
        ).grid(column=0,row=1, sticky='e')

        label_overlap = ttk.Label(
            self._result_frame, textvariable=self.overlap, font=('Arial', 20)
        ).grid(column=1, row=1, sticky='w')

        # Set error style and make label
        error_style = Style()
        error_style.configure('Error.TLabel', foreground='red')
        self.error_label = ttk.Label(
            self._result_frame,
            textvariable=self.error, font=('Arial', 20), style='Error.TLabel'
        ).grid(column=0, row=2, columnspan=2)

        # Configure result frame
        self._result_frame.columnconfigure(0, weight=1)
        self._result_frame.columnconfigure(1, weight=1)
        self._result_frame.rowconfigure(0, weight=1)
        self._result_frame.rowconfigure(1, weight=1)
        self._result_frame.rowconfigure(2, weight=1)

    def _build_display_frame(self):
        # Make canvas
        self.horizontal = Canvas(self._display_frame, width=200, height=200)
        self.horizontal.grid(column=0, row=1, columnspan=2, sticky='nwe')
    
    def _find_remainder(self, *args):
        # Try/Except check for inputs are integers
        try:
            # Get list, split string at ',' remove white space and convert to integers
            _lst = self.lst.get()
            self.int_list = [int(num.strip()) for num in _lst.split(',')]
            # Chek if remainder is less than 0
            rem = find_remainder(int(self.length.get()), self.int_list)
            if  rem < 0:
                self.error.set('Sum of numbers is greater than the length')
            else:
                # Run calculations and draw grid
                self.error.set('')
                self.remainder.set(str(rem))
                overlap = check_overlap(self.int_list, rem)
                self.overlap.set(overlap)
                self.draw_grid()
        except ValueError:
            self.error.set('Only input numbers')

    def draw_grid(self):
        count = int(self.length.get())
        
        self.horizontal.delete('all')

        canvas_width = self.horizontal.winfo_width()
        canvas_height = self.horizontal.winfo_height()

        square_size = 1040 // count

        start = (canvas_width - count * square_size) // 2
        sqrs = []

        for i in range(count):
            x1 = start + i * square_size
            y1 = 2
            x2 = x1 + square_size
            y2 = 2 + square_size
            sq = Square(x1,y1,x2,y2)
            sqrs.append(sq)

        marked = mark(sqrs, self.int_list, int(self.remainder.get()))

        i = 1
        for e in marked:
            if e.is_marked == False:
                self.horizontal.create_rectangle(
                    e.x1, e.y1, e.x2, e.y2, fill='white', outline='black', width=2
                )
                self.horizontal.create_text(
                    (e.x1 + e.x2) // 2, (e.y1 + e.y2) // 2.5 + square_size,
                    text=str(i), font=('Arial', 20, 'bold')
                )
                i += 1
            else:
                self.horizontal.create_rectangle(
                    e.x1, e.y1, e.x2, e.y2, fill='black', outline='white', width=2
                )
                self.horizontal.create_text(
                    (e.x1 + e.x2) // 2, (e.y1 + e.y2) // 2.5 + square_size,
                    text=str(i), font=('Arial', 20, 'bold')
                )
                i += 1