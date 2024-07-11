import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_COLL = os.environ.get("DB_COLL")

TELEGA_TOKEN = os.environ.get("TELEGA_TOKEN")
