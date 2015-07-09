__author__ = 'echiu'

from security_monkey.auditor import Auditor
from security_monkey.watchers.s3 import S3
from security_monkey import app

class S3LoggingAuditor(Auditor):
    index = S3.index
    i_am_singular = S3.i_am_singular
    i_am_plural = S3.i_am_plural

    def __init__(self, accounts=None, debug=False):
        super(S3LoggingAuditor, self).__init__(accounts=accounts, debug=debug)

    def check_logging(self, s3_item):
        app.logger.info("check S3 logging for: {}".format(s3_item))
        app.logger.debug(" - logging config: {}".format(s3_item.config.get('logging', {})))

    def post_logging(self, s3_items):
        app.logger.debug("post_logging {}".format(s3_items))
