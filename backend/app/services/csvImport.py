import csv
from datetime import datetime
from app.models.cgm import Reading

def csvImport(path: str) -> list[Reading]:
    readings = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamp = datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S")
            glucose = float(row["glucoseMmolL"])
            readings.append(
                Reading(
                    glucoseLevel=glucose,
                    timeTaken=timestamp
                )
            )
    return readings