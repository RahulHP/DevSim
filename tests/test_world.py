from World import World


def test_default_init_pop():
    a = World()
    assert a.get_pop() == 10


def test_init_pop():
    a = World(15)
    assert a.get_pop() == 15


def test_init_year():
    a = World()
    assert a.year == 0


def test_increment_year():
    a = World()
    a.increment_year()
    assert a.year == 1


def test_run():
    a = World()
    a.run()
    assert a.get_pop() == 0

