from app.models.cgm import * 
from app.services import * 
from datetime import datetime

readings = csvImport("/mnt/c/Users/chazd/programmingStuff/CGM-WebApp/backend/app/simulation/cgmReadings.csv")
datestr = "2026-03-03 11:00"
values = calculateFromTime(readings, datetime.strptime(datestr, "%Y-%m-%d %H:%M"))
print(values)