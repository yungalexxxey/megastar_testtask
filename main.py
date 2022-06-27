import sys
import uvicorn

from service.app import app
from service.db.init.init_sql import init_sql

from tools.config_parser import SERVICE_PORT, SERVICE_HOST

if __name__ == '__main__':
    if len(sys.argv) == 1:
        uvicorn.run(app, host=SERVICE_HOST, port=SERVICE_PORT, log_level="critical")
    else:
        if len(sys.argv) > 2:
            sys.exit("Usage: python3 main.py or python3 main.py init")
        if sys.argv[1] == 'init':
            init_sql()
            uvicorn.run(app, host=SERVICE_HOST, port=SERVICE_PORT, log_level="critical")
        else:
            sys.exit("unexpected argument.\nUsage: python3 main.py or python3 main.py init")
