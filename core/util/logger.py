import logging
import allure
logger = logging.getLogger(__name__)


def step(msg:str):
    with step(msg):
        pass