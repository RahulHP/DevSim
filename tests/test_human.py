from humans.Human import Human


def test_default_init_age():
    h = Human()
    assert h.age == 20


def test_init_age():
    h = Human(None, 30)
    assert h.age == 30


def test_update():
    h = Human()
    init_age = h.get_age()
    h.update()
    assert h.age == init_age+1


def test_is_alive():
    h = Human()
    assert h.is_alive()


def test_is_dead():
    h = Human(None, 50)
    h.update()
    assert not h.is_alive()
