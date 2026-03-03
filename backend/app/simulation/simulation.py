import numpy
import pandas

# --- Simulation parameters ---
numReadings = 24 * 12          # 288 readings (5 min intervals)
trendInfluence = 0.2
noiseStdDev = 0.2

# Event schedule (in 5‑min indices)
mealTimes = [9*12, 16*12]      # 08:00, 13:00, 17:00
exerciseTimes = [10*12, 12*12]               # 10:00, 12:00 

# Incremental effect parameters
mealAmplitude = 0.50
mealTau = 2
exerciseAmplitude = 0.07
exerciseTau = 18

# Precompute decay factors
mealDecay = numpy.exp(-1 / mealTau)
exerciseDecay = numpy.exp(-1 / exerciseTau)

# --- Initialise readings ---
glucoseValues = numpy.zeros(numReadings)
glucoseValues[0] = 5.5

# State variables for incremental effects
mealState = 0.0
exerciseState = 0.0

# --- Generate readings ---
for t in range(1, numReadings):

    # Trend from last 5 readings
    recentWindow = glucoseValues[max(0, t-5):t]
    if len(recentWindow) >= 2:
        slope = (recentWindow[-1] - recentWindow[0]) / len(recentWindow)
    else:
        slope = 0

    trendTerm = trendInfluence * slope

    baseline = 5.5
    homeostasisK = 0.03
    homeostasisTerm = homeostasisK * (baseline - glucoseValues[t-1])


    # Update incremental meal state
    mealState *= mealDecay
    if t in mealTimes:
        mealState += mealAmplitude

    # Update incremental exercise state
    exerciseState *= exerciseDecay
    if t in exerciseTimes:
        exerciseState -= exerciseAmplitude

    # Noise
    noiseTerm = numpy.random.normal(0, noiseStdDev)

    # Update reading
    glucoseValues[t] = (
        glucoseValues[t-1]
        + trendTerm
        + mealState
        + exerciseState
        + noiseTerm
        + homeostasisTerm
    )

# Clip to plausible physiological range
glucoseValues = numpy.clip(glucoseValues, 3.0, 15.0)

# Build dataframe
timestamps = pandas.date_range("2026-03-03", periods=numReadings, freq="5min")
df = pandas.DataFrame({
    "timestamp": timestamps,
    "glucoseMmolL": glucoseValues.round(1)
})

df.to_csv("cgmReadings.csv", index=False)