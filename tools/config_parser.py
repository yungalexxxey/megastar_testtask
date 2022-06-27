import os

from dotenv import load_dotenv

# from tools.logger import logger

load_dotenv()

SERVICE_HOST = os.getenv('SERVICE_HOST')
SERVICE_PORT = os.getenv('SERVICE_PORT')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

# logger.debug(f"big config time\n"
#              f"dbname is {DB_NAME}\n"
#              f"dbuser is {DB_USER}\n"
#              f"dbpass is {DB_PASS}\n"
#              f"dbhost is {DB_HOST}\n"
#              f"dbport is {DB_PORT}\n"
#              f"service_host is {SERVICE_HOST}\n"
#              f"service_port is {SERVICE_PORT}\n")
