import attr


@attr.s
class Character:
    name = attr.ib()
    life_points = attr.ib(default=100)
    level = attr.ib(default=1)
    strength = attr.ib(default=10)
    is_a_god = attr.ib(default=False)
