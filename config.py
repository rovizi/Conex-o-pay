import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Conexão Pay"
    MP_ACCESS_TOKEN: str = os.getenv("MP_ACCESS_TOKEN", "APP_USR-3649430665700411-091312-048c4f61a1272de84c1eb010d6498481-1317503478")

settings = Settings()