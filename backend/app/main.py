from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services import csvImport
from dataclasses import asdict

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (fine for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/readings")
def getReadings():
    readings = csvImport("app/simulation/cgmReadings.csv")
    return [asdict(r) for r in readings]
