from typing import List
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Reading(frozen = True):
    glucoseLevel : float
    timeTaken : datetime

@dataclass
class GlucoseSeries:
    series : List[Reading]

@dataclass
class Event(frozen = True):
    event_type : str
    timeTaken : datetime


