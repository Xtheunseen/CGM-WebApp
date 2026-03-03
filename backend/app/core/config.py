from pydantic import BaseSettings

class Settings(BaseSettings):

    # Server settings
    APP_NAME: str = "CGM_WEBAPP"
    DEBUG: bool = true
    HOST: str = "0.0.0.0"
    PORT: int = 8080

    # Simulation settings
    CGM_UPDATE_INTERVAL: float = 5.0
    CGM_NOISE_STD: float = 2.0
    CGM_BASELINE: float = 120.0
    CGM_HISTORY_MINUTES: int = 60

    

settings = Settings()