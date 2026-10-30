from App import User

def test_greet():
    u = User()
    assert u.greet() == "Hello"