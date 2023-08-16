import logging
import allure

logger = logging.getLogger(__name__)



def step(msg: str):
    with allure.step(msg):
        pass
