import main


def test_my1():
    assert main.myFun(8, 4) == 2


def test_my2():
    assert main.myFun(1, 2) == 0.5


def test_my3():
    assert main.myFun(5, 0 ) is None