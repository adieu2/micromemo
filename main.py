from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()
        self.init_menu()

    def init_window(self):
        self.master.title("Micromemo")
        self.pack(fill=BOTH, expand=1)

        self.card_frame = Frame(self, bg="#111", highlightbackground="black", highlightthickness=1)
        self.card_frame.pack(fill=BOTH, expand=True, side=TOP, padx=5, pady=5)

        self.buttons_frame = Frame(self)
        self.buttons_frame.pack(fill=X, side=BOTTOM, padx=5, pady=5)

        self.question_label = Label(self.card_frame, text="Device", borderwidth=2, relief="groove")
        self.question_label.config(font=("Verdana", 36))
        self.question_label.pack(expand=True)

        self.answer_label = Label(self.card_frame, text="Appareil", borderwidth=2, relief="groove")
        self.answer_label.config(font=("Verdana", 36))
        self.answer_label.pack(expand=True)

        self.load_button = Button(self.buttons_frame, text="Charger...")
        self.load_button.pack(side=LEFT)

        self.next_button = Button(self.buttons_frame, text="Carte suivante")
        self.next_button.pack(side=RIGHT)

    def init_menu(self):
        menu = Menu(self.master)
        self.master.configure(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Charger un fichier csv...")
        file_menu.add_command(label="Rafraichir le fichier")
        file_menu.add_separator()
        file_menu.add_command(label="Quitter")

        card_menu = Menu(menu)
        card_menu.add_command(label="Apprendre dans l'autre sens")
        
        menu.add_cascade(label="Fichier", menu=file_menu)
        menu.add_cascade(label="Cartes", menu=card_menu)

    def client_exit(self):
        exit()

root = Tk()

# Size configuration
root.geometry("600x200")
root.maxsize(1200, 200)
root.minsize(400, 200)

app = Application(master=root)
app.mainloop()
