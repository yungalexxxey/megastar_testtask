from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_HOST = os.getenv('SERVICE_HOST')
SERVICE_PORT = os.getenv('SERVICE_PORT')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

