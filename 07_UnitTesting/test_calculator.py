from calculator import *
import pytest

@pytest.mark.skip
def test_add():
    assert add(2,3) == 5

def test_multiply():
    assert multiply(2,3) == 6