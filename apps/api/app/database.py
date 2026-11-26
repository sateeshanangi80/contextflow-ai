import os
import psycopg # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DATABASE_URL)
