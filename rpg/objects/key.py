from enum import Enum

from rpg.objects import Object
from rpg.locations.castle.castle_entrance import Castle
from rpg.locations.castle.castle_insides import CastleBoss


class Key(Object):
    def __init__(self, success_message, correct_place):
        self.success_message = success_message
        self.door_opened = False
        self.correct_place = correct_place

    def use(self, game):
        if isinstance(game.current_location, self.correct_place):
            if not self.door_opened:
                print(self.success_message)
                self.door_opened = True
            else:
                print(
                    "You found the correct key, but the door is already open."
                )
            return True
        return False


class Keys(Enum):
    CASTLE_ENTRY = Key(
        success_message="You used the key to open the castle door.",
        correct_place=Castle,
    )
    CASTLE_BOSS = Key(
        success_message="You used the key to open the door of the archduke.",
        correct_place=CastleBoss,
    )
