
class Feature:
    '''Arbitrary feature as extracted from a GPX file or track.'''

    def __init__(self, gpx, track):
        self.gpx    = gpx
        self.track  = track

    @staticmethod
    def names():
        return "Name"

    def get(self):
        return self.track.name


