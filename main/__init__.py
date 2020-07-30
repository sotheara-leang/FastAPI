import logging

import os
import sys

from main.common.logger import Logger
from main.common.configuration import Configuration

# setup env
PROJ_HOME = os.path.join(os.getcwd())
sys.path.append(PROJ_HOME)
os.environ['PROJ_HOME'] = PROJ_HOME

logger = Logger('main/conf/logging.yml')
