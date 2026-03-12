from app.models.cgm import GlucoseSeries
from datetime import datetime, timedelta

HIGH = 10.0


def timeAboveRange(series: GlucoseSeries):
    points = sorted(
        [(r.timeTaken, r.glucoseLevel) for r in series.series],
        key=lambda p: p[0],
    )

    above_range = timedelta(0)
    for i in range(0, len(points) - 1):
        t1, g1 = points[i]
        t2, g2 = points[i + 1]

        if g1 >= HIGH and g2 >= HIGH:
            above_range += (t2 - t1)

    return above_range


    