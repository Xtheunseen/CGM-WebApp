from typing import List
from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Reading:
    glucoseLevel : float
    timeTaken : datetime

@dataclass
class GlucoseSeries:
    series : List[Reading]

@dataclass(frozen=True)
class Event:
    event_type : str
    timeTaken : datetime


