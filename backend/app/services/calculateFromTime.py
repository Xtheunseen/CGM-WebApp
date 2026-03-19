from app.models.cgm import Reading
from app.services.makeSeries import makeSeries
from app.services.coefficientOfVariation import coefficientOfVariation
from app.services.trend import calculate_trend
from app.services.timeAboveRange import timeAboveRange
from app.services.timeBelowRange import timeBelowRange
from app.services.timeInRange import timeInRange
from datetime import datetime
import bisect


def calculateFromTime(readings: list[Reading], time: datetime) -> list[str] | None:
    i = findIndexByTimestamp(readings, time)
    if i is None:
        return None

    # Use the 4 most recent readings including the target timestamp
    selected_readings = readings[max(0, i - 4) : i + 1]

    series = makeSeries(selected_readings)

    values = []
    values.append(calculate_trend(series))
    values.append(str(timeInRange(series)))
    values.append(str(timeBelowRange(series)))
    values.append(str(timeAboveRange(series)))
    values.append(str(coefficientOfVariation(series)))
    return values



def findIndexByTimestamp(readings: list[Reading], time: datetime) -> int | None:
    timestamps = [r.timeTaken for r in readings]
    i = bisect.bisect_left(timestamps, time)
    if i < len(readings) and readings[i].timeTaken == time:
        return i
    return None


