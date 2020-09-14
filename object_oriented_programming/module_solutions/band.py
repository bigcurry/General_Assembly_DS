class Band:
    def __init__(self, name, genre, albums):
        self.name = name
        self.genre = genre
        self.albums = albums

    def add_album(self, album_name):
        self.albums.append(album_name)

    def remove_album(self, album_name):
        self.albums.remove(album_name)

    def count_albums(self):
        return len(self.albums)
