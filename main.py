from tkinter import *

from script.model import *
from script.controller import *
from script.view import *

root = Tk()

# Size configuration
root.geometry("600x200")
root.maxsize(1200, 400)
root.minsize(400, 200)

view = Application(master=root)
Controller(MicroMemo(), view)
view.mainloop()
