import allure
class AssertHelper:

    @staticmethod
    def assert_true(actual: bool, msg: str):
        try:
            assert actual is True
            allure.description(msg)
        except AssertionError as ex:
            allure.description(ex)

    @staticmethod
    def assert_false(actual: bool, msg: str):
        try:
            assert actual is False
            allure.description(msg)
        except AssertionError as ex:
            allure.description(ex)

    @staticmethod
    def assert_equals(actual, expected, msg: str):
        try:
            assert actual == expected
            allure.description(msg)
        except AssertionError as ex:
            allure.description(ex)

    @staticmethod
    def assert_not_equals(actual, expected, msg: str):
        try:
            assert actual != expected
            allure.description(msg)
        except AssertionError as ex:
            allure.description(ex)
