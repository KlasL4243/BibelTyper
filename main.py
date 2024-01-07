from bibleParser import parse_bible, load_book

if __name__ == "__main__":
    # parse_bible()
    gen = load_book("Gen")
    print(gen[1-1][1-1])