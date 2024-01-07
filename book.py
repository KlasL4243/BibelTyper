
class Book(list):
    def __init__(self, rows: list):
        super().__init__()

        self.chapter_count = int(rows[-1][0])
        self.verse_count = len(rows)

        self.extend([[] for _ in range(self.chapter_count)])

        for row in rows:
            self[int(row[0])-1].append(row[2])
