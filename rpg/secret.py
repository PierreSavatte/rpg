import math


def konami_code(game):
    game.win()


def motherlode(game):
    print(
        'You mysteriously have received 50,000 units what is called "Simoleons". '
        "You don't really know what to do with this..."
    )
    game.bag.add("50,000 Simoleons")


def doom_god_mode(game):
    print("You are now a god.")
    self.player.is_a_god = True
    game.player.life_points = math.inf
    game.player.strength = math.inf


secrets = {
    "up_up_down_down_left_right_left_right_b_a": konami_code,
    "motherlode": motherlode,
    "iddqd": doom_god_mode,
}
