from pydantic import BaseSettings
from dotenv import load_dotenv

load_env = load_dotenv()
load_env = True 

class Settings(BaseSettings):
    database_hostname: str 
    database_port: str 
    database_password: str
    database_name: str 
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class config:
        env_file = ".env"    

settings = Settings()