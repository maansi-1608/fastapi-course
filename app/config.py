from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

class Settings(BaseSettings):
  database_hostname : str = os.getenv("DATABASE_HOST")
  database_port : str = os.getenv("DATABASE_PORT")
  database_password : str = os.getenv("DATABASE_PASSWORD")
  database_name : str = os.getenv("DATABASE_NAME ")
  database_username : str = os.getenv("DATABASE_USERNAME")
  secret_key : str = os.getenv("SECRET_KEY")
  algorithm : str = os.getenv("ALGORITHM")
  access_token_expire_minutes : int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

  class config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

settings = Settings()