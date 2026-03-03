from app.models.cgm import GlucoseSeries
from datetime import datetime
import math

def coefficientOfVariation(series : GlucoseSeries):
    values = [r.glucoseLevel for r in series.series]

    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    stdDev = math.sqrt(variance)
    cv = stdDev/mean
    return cv
