import os

from main.common.logger import Logger
from main.common.configuration import Configuration

# setup env
PROJ_HOME = os.path.join(os.getcwd())
os.environ['PROJ_HOME'] = PROJ_HOME

__logger__ = Logger('main/conf/logging.yml')

# config
config = Configuration('main/conf/application.yml')

def get_conf():
    return config
