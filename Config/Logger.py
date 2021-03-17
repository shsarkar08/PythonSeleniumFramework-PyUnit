import logging
import logging.config
import yaml
from Resources.TestData import TestData


class pyLog:

    @staticmethod
    def logr(__name__):

        with open(TestData.LOG_CONFIG_PATH, 'r') as f:
            log_cfg = yaml.safe_load(f.read())

        logging.config.dictConfig(log_cfg)

        lgr = logging.getLogger('dev')

        lgr.setLevel(logging.DEBUG)
        return lgr