from customtkinter import CTk, CTkFont, CTkTextbox

from utils import center_window


class App(CTk):
    def __init__(self):
        super().__init__()

        self.font = CTkFont("Arial", 20)
        center_window(self, 1200, 800)

        self.title("Bible")
        self.resizable(False, False)
        self.geometry()

        self.book_textbox = CTkTextbox(self, width=800, height=300, font=self.font, wrap="word")
        self.book_textbox.bind("<KeyRelease>", self.callback)

        self.book_textbox.pack(fill="both", expand=True)
        self.from_user = ""
        self.from_book = ""

    def set_text(self, text: str):
        self.book_textbox.delete("1.0", "end")
        self.book_textbox.insert("1.0", text)

    def callback(self, event):
        if event.keysym == "BackSpace" and len(self.from_user) > 0:
            self.from_user = self.from_user[:-1]
            self.book_textbox.delete(f"1.{len(self.from_user)-1}")
        else:
            self.from_user += event.char
            self.book_textbox.insert(f"1.{len(self.from_user)-1}", event.char)
