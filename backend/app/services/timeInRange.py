from app.models.cgm import GlucoseSeries
from datetime import datetime, timedelta

LOW = 3.9
HIGH = 10.00


def timeInRange(series: GlucoseSeries):
    points = sorted(
        [(r.timeTaken, r.glucoseLevel) for r in series.series],
        key=lambda p: p[0],
    )

    in_range = timedelta(0)
    for i in range(0, len(points) - 1):
        t1, g1 = points[i]
        t2, g2 = points[i + 1]

        if LOW <= g1 <= HIGH and LOW <= g2 <= HIGH:
            in_range += (t2 - t1)

    return in_range


    