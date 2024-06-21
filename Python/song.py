class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        current = self
        _next = self.next
        while _next is not None and _next.next is not None:
            current = current.next
            _next = _next.next.next
            if current == _next:
                return True
        return False


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_in_repeating_playlist())