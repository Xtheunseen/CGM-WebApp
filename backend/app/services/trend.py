from app.models.cgm import GlucoseSeries

def calculate_trend(series: GlucoseSeries):
    changesPerMinute = []
    avgChange = 0.0
    points = sorted(
    [(r.timeTaken, r.glucoseLevel) for r in series.series],
    key=lambda p: p[0])
    
    for i in range (0, len(points)-1):
        changeInGlucose = points[i+1][1] - points[i][1]
        changeInTime = points[i+1][0] - points[i][0]
        changeInSeconds = changeInTime.total_seconds()
        currentChangePerMinute = changeInGlucose / (changeInSeconds/60)
        changesPerMinute.append(currentChangePerMinute)

    avgChange = sum(changesPerMinute) / len(changesPerMinute)

    if avgChange >= 0.17:
        return "vqr"    #very quick rise
    elif avgChange >= 0.11 and avgChange < 0.17:
        return "qr"  #quick rise
    elif avgChange >= 0.06 and avgChange < 0.11:
        return "r" #rise
    elif avgChange >= 0.03 and avgChange <0.06:
        return "gr" #gentle rise 
    elif avgChange < 0.03 and avgChange > -0.03:
        return "n" #normal
    elif avgChange <-0.03 and avgChange >= -0.06:
        return "gf" #gentle fall
    elif avgChange < -0.06 and avgChange >= -0.11:
        return "f" #fall
    elif avgChange < -0.11 and avgChange >= -0.17:
        return "qf" #quick fall
    elif avgChange < -0.17:
        return "vqf" # very quick fall