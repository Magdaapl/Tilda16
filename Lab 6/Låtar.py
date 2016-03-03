class Låtar:
    def __init__(self, trackid, låttid, artistnamn, låttitel):
        self.trackid = trackid
        self.låttid = låttid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        if self.artistnamn < other.artistnamn:
            return True
        else:
            return False
