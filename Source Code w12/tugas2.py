from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = None  # Awalnya None, artinya belum ada operasi
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(0)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiply_button = Button(master, text="x", command=lambda: self.update("multiply"))
        self.divide_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.multiply_button.grid(row=3, column=0)
        self.divide_button.grid(row=3, column=1)

    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if self.total is None:  # Kasus pertama kali operasi
            self.total = self.entered_number
        else:
            if method == "add":
                self.total += self.entered_number
            elif method == "subtract":
                self.total -= self.entered_number
            elif method == "multiply":
                self.total *= self.entered_number
            elif method == "divide":
                if self.entered_number != 0:
                    self.total /= self.entered_number
                else:
                    self.total = 0  # atau tampilkan pesan error

        if method == "reset":
            self.total = None
            self.total_label_text.set(0)
        else:
            self.total_label_text.set(int(self.total))

        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()
