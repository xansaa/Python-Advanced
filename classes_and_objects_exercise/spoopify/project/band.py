from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: Album):
        try:
            album = next(filter(lambda p: p.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_name)

        return f"Album {album_name} is not found."

    def details(self) -> str:
        albums_details = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n" \
               f"{albums_details}"



