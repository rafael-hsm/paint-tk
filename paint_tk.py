from tkinter import *  # this is a base for us project, tkinter is native python GUI.
from tkinter import colorchooser  # For chooser all parameters of colors.

import pyscreenshot  # library for a screenshot


class PaintTk:
    """In this class we have the entire project. I will enter comments by step"""

    def __init__(self):
        # Start the tkinter in the variable window. Define a title, and
        # the size window.
        self.window = Tk()
        self.window.title('PaintTk by Rafa')
        self.window.geometry("1200x600")
        self.window.minsize(width=680, height=480)
        self.window.resizable(0, 0)  # This blocks screen scaling.

        # The applications start with oval brush selected.
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

        # Set icons
        self.img_line = PhotoImage(file='assets/icons/line.png')
        self.img_oval = PhotoImage(file='assets/icons/oval.png')
        self.img_eraser = PhotoImage(file='assets/icons/eraser.png')
        self.img_save = PhotoImage(file='assets/icons/save.png')
        self.img_square = PhotoImage(file='assets/icons/rainbow.png')
        self.img_new = PhotoImage(file='assets/icons/new.png')

        self.list_colors = ('black', 'gray', 'red', 'green', 'blue',
                            'yellow', 'magenta', 'cyan')
        self.pick_colors = 'black'

        self.bar_menu = Frame(self.window, bg='#3b3b3b', padx=10, pady=10)
        self.bar_menu.pack(fill='x')  # "fill='x' fills the entire x-axis

        self.text_color = Label(self.bar_menu, text='  Colors:  ', fg='white', bg='#3b3b3b')
        self.text_color.pack(side='left')

        for cor in self.list_colors:
            self.button_color = Button(self.bar_menu, bg=cor, width=3, height=2, bd=1,
                                       command=lambda col=cor: self.select_colors(col)).pack(side='left')

        self.label_colors_choose = Label(self.bar_menu, text=' Color Choose:  ', fg='white', bg='#3b3b3b')
        self.label_colors_choose.pack(side='left')

        self.color_choose = Button(self.bar_menu, image=self.img_square, bd=1, command=self.selected_color)
        self.color_choose.pack(side='left')

        self.text_pen_size = Label(self.bar_menu, text='  Size:  ', fg='white', bg='#3b3b3b')
        self.text_pen_size.pack(side='left')

        self.pen_size = Spinbox(self.bar_menu, justify='center', from_=1, to=50, width=4)
        self.pen_size.pack(side='left')

        self.text_brushs = Label(self.bar_menu, text='  Brushs:  ', fg='white', bg='#3b3b3b').pack(side='left')

        self.button_line = Button(self.bar_menu, image=self.img_line, bd=1, command=self.brush_line)
        self.button_line.pack(side='left')
        self.button_oval = Button(self.bar_menu, image=self.img_oval, bd=1, command=self.brush_oval)
        self.button_oval.pack(side='left')
        self.button_eraser = Button(self.bar_menu, image=self.img_eraser, bd=1, command=self.brush_eraser)
        self.button_eraser.pack(side='left')

        self.text_options = Label(self.bar_menu, text='  Options:  ', fg='white', bg='#3b3b3b').pack(side='left')
        self.button_save = Button(self.bar_menu, image=self.img_save, bd=3, command=self.save).pack(side='left')
        self.button_new = Button(self.bar_menu, image=self.img_new, bd=3, command=self.clean).pack(side='left')

        self.area_draw = Canvas(self.window, height=720, bg='gainsboro')
        self.area_draw.pack(fill='both')
        self.area_draw.bind('<B1-Motion>', self.draw)

        self.window.bind("<F1>", self.save)
        self.window.bind("<F2>", self.clean)

        self.window.mainloop()

    def draw(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y

        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors,
                                       outline=self.pick_colors, width=self.pen_size.get())
        elif self.line_brush:
            self.area_draw.create_line(x1 - 10, y1 - 10, x2, y2, fill=self.pick_colors,
                                       width=self.pen_size.get())
        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill='gainsboro',
                                       outline='gainsboro', width=self.pen_size.get())

    def select_colors(self, col):
        self.pick_colors = col

    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = True

    def clean(self, event):
        self.area_draw.delete("all")

    def save(self, event):
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
        y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()

        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save('image.png', 'png')

    def selected_color(self):
        color = colorchooser.askcolor()
        self.pick_colors = color[1]


PaintTk()
