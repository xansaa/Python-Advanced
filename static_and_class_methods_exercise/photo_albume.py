from math import ceil


class PhotoAlbum:
    PAGE_PHOTOS = 4
    DASHES_COUNT: int = 11
    SYMBOL_FOR_LINE: str = '-'

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGE_PHOTOS))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PAGE_PHOTOS:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:
        result = [
            self.DASHES_COUNT * self.SYMBOL_FOR_LINE,
        ]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASHES_COUNT * self.SYMBOL_FOR_LINE)

        return "\n".join(result)

