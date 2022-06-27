import sys
import uvicorn

from service.app import app
from service.db.init.init_sql import init_sql

from tools.config_parser import SERVICE_PORT, SERVICE_HOST

if __name__ == '__main__':
    if len(sys.argv) == 1:
        uvicorn.run(app, host=SERVICE_HOST, port=SERVICE_PORT)
    else:
        if len(sys.argv) > 2:
            print("python3 main.py or python3 main.py init")
            sys.exit()
        if sys.argv[1] == 'init':
            init_sql()
            uvicorn.run(app, host="0.0.0.0", port=8080)
