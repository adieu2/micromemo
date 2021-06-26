from tkinter import *

from script.model import *
from script.controller import *
from script.view import *

root = Tk()

# Size configuration
root.geometry("800x300")
root.maxsize(1200, 400)
root.minsize(400, 200)

view = Application(master=root)
Controller(MicroMemo(), view)
view.mainloop()
