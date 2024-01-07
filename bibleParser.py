from pathlib import Path
from csv import writer, QUOTE_STRINGS

# paths to files and folders
paths = {
    "bible": {
        "txt": Path("bible.txt"),
        "folder": Path("bible/")
    }
}

def parse_bible():
    """
    If the bible folder doesn't exist, it will be created.
    If the bible folder is empty, bible.txt will be parsed into the bible folder.
    """

    if not _bible_folder_already_exists():
        print("Creating bible folder...")
        _create_bible_folder()
    if not _bible_already_parsed():
        print("Parsing bible.txt...")
        _parse_bible_file()
    else:
        print("Bible already parsed.")


def _bible_folder_already_exists():
    """Returns True if bible folder already exists."""
    return paths["bible"]["folder"].exists()

def _create_bible_folder():
    """Creates bible folder"""
    paths["bible"]["folder"].mkdir()

def _bible_already_parsed():
    """Returns True if bible folder contains any files."""
    return any(paths["bible"]["folder"].iterdir())

def _parse_bible_file():
    """Parses bible.txt into a folder of csv files, one for each book of the bible."""
    books = {}

    # read bible.txt into a list of lines
    with open(file=paths["bible"]["txt"], mode="r", encoding="utf-8") as file:
        file_bible = file.read().splitlines()

    # parse each line into a book, chapter, verse, and text
    for line in file_bible:
        book, chapter_and_verse, text = line.split(sep=" ", maxsplit=2)
        chapter, verse = chapter_and_verse.split(":")
        chapter, verse = int(chapter), int(verse)

        # add book to books if it doesn't exist
        if book not in books:
            books[book] = []

        # adds the verse to the book
        books[book].append((chapter, verse, text))

    # write each book to a csv file
    for book, rows in books.items():
        with open(file=f"bible/{book}.csv", mode="w+", encoding="utf-8", newline="") as file:
            # string are quoted to preserve "," a delimiter
            csv_writer = writer(file, quoting=QUOTE_STRINGS)
            csv_writer.writerow(["chapter", "verse", "text"])
            for row in rows:
                csv_writer.writerow(row)
