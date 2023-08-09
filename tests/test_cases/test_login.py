from tests.test_cases.test_base import TestBase
from time import sleep

from threading import local

import logging

logger = logging.getLogger(__name__)

class TestLogin(TestBase):

    def test_login(self):
        logger.info('asdffffffffffffffffffffffffffffffffffffffff')
        sleep(3)
        print('test_login')

    def test_login2(self):
        print('test_login2')
        sleep(15)
        logger.info("done")

    # def test_login3(self):
    #     print('test_login3')
    #
    # def test_login4(self):
    #     sleep(5)
    #     print('test_login4')
