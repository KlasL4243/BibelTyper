from app2 import App2
from bibleParser import parse_bible, load_book


if __name__ == "__main__":
    parse_bible()
    gen = load_book("Gen")

    app = App2()
    app.mainloop()

