
import feature

class Elevation(feature.Feature):
    '''Elevation-related features'''

    def __init__(self, gpx, track):
        super(Elevation, self).__init__(gpx, track)

    @staticmethod
    def names():
        return ["Uphill", "Downhill", "High", "Low"]

    def get(self):

        mm = self.track.get_elevation_extremes()
        ud = self.track.get_uphill_downhill()
        return [ud.uphill, ud.downhill, mm.maximum, mm.minimum]


