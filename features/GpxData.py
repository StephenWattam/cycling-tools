


import feature

class GpxData(feature.Feature):
    '''GPX-specific technical features.
    
    Not intended for useful sporting-related things like distance, time, duration.'''

    def __init__(self, gpx, track):
        super(GpxData, self).__init__(gpx, track)

    @staticmethod
    def names():
        return ["Tracks in File", "Author"]

    def get(self):
        return [len(self.gpx.tracks), self.gpx.author_name]



