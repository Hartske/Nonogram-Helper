from tkinter import Tk, Frame, Entry, Grid, ttk, StringVar, Canvas
from remainder import find_remainder, check_overlap

class Window():
    def __init__(self):
        self._root = Tk()
        self._root.title("Nonogram Helper")
        self._root.grid()
        self.length = StringVar(value=0)
        self.remainder = StringVar(value=0)
        self.lst = StringVar(value=0)
        self.overlap = StringVar(value='False')

        self._entry_frame = ttk.Frame(
            self._root, borderwidth=2, relief='solid'
        )
        self._entry_frame.grid(column=0, row=0, padx=5, pady=5)
        self._build_entry_frame()

        self._result_frame = ttk.Frame(
            self._root, borderwidth=2, relief='solid'
        )
        self._result_frame.grid(column=1, row=0)
        self._build_result_frame()

        self._display_frame = ttk.Frame(self._root,).grid(column=0, row=1, columnspan=2, sticky='we')
        self._build_display_frame()

        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(1, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
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

        # Entry window for length of column or row
        length_entry = ttk.Entry(
            self._entry_frame, width=7, textvariable=self.length, font=('Arial', 20)
        )
        length_entry.grid(column=1, row=0, sticky='w')

        # Text label for list entry window
        ttk.Label(
            self._entry_frame,
            text='List numbers in column or row. ex: 2,10,1,2', font=('Arial', 20)
        ).grid(
            column=0, row=1, columnspan=2, sticky='we'
        )

        # Entry window for list of numbers
        lst_entry = ttk.Entry(
            self._entry_frame, width=24, textvariable=self.lst, font=('Arial', 20)
        )
        lst_entry.grid(column=0, row=2, columnspan=2, sticky='we', padx=10)

        ttk.Button(
            self._entry_frame,
            text='Find Remainder', command=self._find_remainder
        ).grid(column=0, row=3, columnspan=2)

        length_entry.focus()

    def _build_result_frame(self):
        rem = self.remainder.get()
        ttk.Label(
            self._result_frame, text='Remaining squares in row/column: ', font=('Arial', 20)
        ).grid(column=0, row=0, sticky='e')

        label_remainder = ttk.Label(
            self._result_frame, textvariable=self.remainder, font=('Arial', 20)
        ).grid(column=1, row=0, sticky='w')

        ttk.Label(
            self._result_frame, text='Overlap?: ', font=('Arial', 20)
        ).grid(column=0,row=1, sticky='e')

        label_overlap = ttk.Label(
            self._result_frame, textvariable=self.overlap, font=('Arial', 20)
        ).grid(column=1, row=1, sticky='w')

    def _build_display_frame(self):
        self.horizontal = Canvas(self._display_frame, width=200, height=100)
        self.horizontal.grid(column=0, row=1, columnspan=2, sticky='we')
    
    def _find_remainder(self, *args):
        _lst = self.lst.get()
        int_list = [int(num.strip()) for num in _lst.split(',')]
        rem = find_remainder(int(self.length.get()), int_list)
        self.remainder.set(str(rem))
        overlap = check_overlap(int_list, rem)
        self.overlap.set(overlap)
        self.draw_grid()

    def draw_grid(self):
        count = int(self.length.get())
        
        self.horizontal.delete('all')

        canvas_width = self.horizontal.winfo_width()
        canvas_height = self.horizontal.winfo_height()

        square_size = 52

        start = (canvas_width - count * square_size) // 2

        for i in range(count):
            x1 = start + i * square_size
            y1 = 0
            x2 = x1 + square_size
            y2 = square_size
            self.horizontal.create_rectangle(
                x1, y1, x2, y2, fill='white', outline='black', width=2
            )