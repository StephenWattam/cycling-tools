




import feature

class TrackData(feature.Feature):
    '''Track-specific technical features.

    Not intended for useful sporting-related things like distance, time, duration.'''

    def __init__(self, gpx, track):
        super(TrackData, self).__init__(gpx, track)

    @staticmethod
    def names():
        return ["Name", "Points in Track", "Track Comment", "Track Description"]

    def get(self):
        return [self.track.name, self.track.get_points_no(), self.track.comment, self.track.description]




