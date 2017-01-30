
import feature

class Time(feature.Feature):

    def __init__(self, gpx, track):
        super(Time, self).__init__(gpx, track)

    @staticmethod
    def names():
        return ["Time", "Unix Time", "Year", "Month", "Day", "Hour", "Minute", "Second"]

    def get(self):

        d = self.gpx.time
        return [str(d), d.strftime("%s"), d.year, d.month, d.day, d.hour, d.minute, d.second]


