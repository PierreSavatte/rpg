from example.vacation_request.locations.castle.castle_entrance import Castle
from example.vacation_request.locations.castle.castle_insides import (
    CastleBossDoor,
)
from rpg.objects.key import RPGKeys, Key


class Keys(RPGKeys):
    CASTLE_ENTRY = Key(
        success_message="You used the key to open the castle door.",
        correct_place=Castle,
    )
    CASTLE_BOSS = Key(
        success_message="You used the key to open the large door.",
        correct_place=CastleBossDoor,
    )
