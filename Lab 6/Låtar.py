class Låtar:
    def __init__(self, trackid, låttid, artistnamn, låttitel):
        self.trackid = trackid
        self.låttid = låttid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def get_trackid(self):
        return self.trackid

    def get_låttid(self):
        return self.låttid

    def get_artistnamn(self):
        return self.artistnamn

    def get_låttitel(self):
        return self.låttitel

    def __It__(self, other):
        return self.artistnamn < other.artistnamn
