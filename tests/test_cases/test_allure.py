import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


# @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
# def test_xfail_expected_failure():
#     """this test is an xfail that will be marked as expected failure"""
#     assert False
#
#
# @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
# def test_xfail_unexpected_pass():
#     """this test is an xfail that will be marked as unexpected success"""
#     assert True