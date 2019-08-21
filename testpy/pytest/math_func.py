import  first
import pytest

# def setup(self):
#     print("f")
# class TestClass(object):
def setup_module(module):
    print("-----setup------")

# @pytest.mark.skip(reason="no way of currently testing this")
# @pytest.mark.number
def test_add( ):
    assert first.add(7,4)==10
    assert first.add(7)==9
#
# @pytest.mark.number
def test_pro():
    # print("2")
    assert first.product(7,4)==21
    assert first.product(7)==14

# @pytest.mark.string
def test_pro1():
    print("----2")
    assert first.product(7, 5) == 35
    assert first.product(7) == 14

def teardown_module(module):
    print("-----teardown------")