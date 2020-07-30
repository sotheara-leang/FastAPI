import os

from main.common.logger import Logger
from main.common.configuration import Configuration

# setup env
PROJ_HOME = os.path.join(os.getcwd())
os.environ['PROJ_HOME'] = PROJ_HOME

logger = Logger('main/conf/logging.yml')
