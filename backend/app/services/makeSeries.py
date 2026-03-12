from app.models.cgm import Reading, GlucoseSeries


def makeSeries(readings: list[Reading]) -> GlucoseSeries:
    # Construct a GlucoseSeries from a list of Reading objects
    return GlucoseSeries(series=readings)
