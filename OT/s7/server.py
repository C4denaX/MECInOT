import logging
import sys
import snap7
from snap7.server import mainloop

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

port = 1102

if __name__ == '__main__':
    if len(sys.argv) > 1:
        snap7.common.load_library(sys.argv[1])
    mainloop(port)