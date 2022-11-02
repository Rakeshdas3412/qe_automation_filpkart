import inspect
import logging
from pathlib import Path
import pytest
import configparser
from utils.common_utils import CommonUtils


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

    ROOT_PATH = str(Path(__file__).parent.parent)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(self.ROOT_PATH+"/logs/"+'logfile.log')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger