from customtkinter import CTk, CTkFont, CTkLabel

from bibleParser import load_book
from utils import center_window


class App2(CTk):
    def __init__(self):
        super().__init__()

        self.font = CTkFont("Arial", 40)
        center_window(self, 1200, 800)

        self.title("Bible")
        self.resizable(False, False)
        self.geometry()

        self.from_user = []
        self.from_book = list(load_book("Gen")[0][0])

        self.labels = [CTkLabel(self, text=char, font=self.font) for char in self.from_book]
        for index, label in enumerate(self.labels):
            label.grid(row=0, column=index)

        self.bind("<Key>", self.callback)

    def callback(self, event):
        len_from_user = len(self.from_user)
        if event.keysym == "BackSpace" and len_from_user > 0:
            self.from_user.pop()
            self.labels[len_from_user].configure(bg_color="transparent")
        elif event.char:
            if len_from_user >= len(self.from_book):
                return
            self.from_user.append(event.char)
            chat_correct = self.from_user[-1] == self.from_book[len_from_user]
            self.labels[len_from_user].configure(bg_color=("darkgreen" if chat_correct else "darkred"))