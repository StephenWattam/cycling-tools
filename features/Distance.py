

import feature

class Distance(feature.Feature):
    '''Distance-related features'''

    def __init__(self, gpx, track):
        super(Distance, self).__init__(gpx, track)

    @staticmethod
    def names():
        return ["Distance 2D", "Distance 3D"]

    def get(self):
        return [self.track.length_2d(), self.track.length_3d()]


