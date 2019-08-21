import  first
# from allure import severity,severity_level,scenario
from allure_commons.types import AttachmentType

import pytest

# def setup(self):
#     print("f")
# class TestClass(object):
# @severity(severity_level.CRITICAL)
# @scenario('test_user.feature', 'Check user list by page')
def setup_module(module):
    print("-----setup------")

# @pytest.mark.skip()
@pytest.mark.number
def test_add( ):
    print("add")
    assert first.add(7,3)==10
    assert first.add(7)==9
#
@pytest.mark.number
@pytest.mark.string
def test_pro():
    # print("2")
    print("pro")
    assert first.product(7,3)==21
    print("before")
    assert first.product(7)==14
    print("after")

@pytest.mark.string
def test_pro1():
    print("----2")
    assert first.product(7, 5) == 35
    assert first.product(7) == 14

def tear_down(module):
    print("-----teardown------")