from example.vacation_request.locations.castle.castle_insides import (
    CastleInside,
)
from rpg.location import Location


class Castle(Location):
    INCORRECT_INPUT_MESSAGE = (
        "You are frightened by an owl crying nearby and "
        "frozen by the cold chill of the night. You didn't moved."
    )
    CHOICES = ["go_north", "go_west"]

    def welcome_message(self):
        return "You arrive in front of the castle. There is a huge door right in front of you"

    def go_north(self):
        from example.vacation_request.keys import Keys

        if Keys.CASTLE_ENTRY in self.game.bag.keys:
            if not Keys.CASTLE_ENTRY.value.door_opened:
                print(
                    "You look at the old and rusty lock. "
                    "It looks a lot like the key you got at the entry of the forest."
                )
                return CastleDoor
            else:
                print("The door is opened and you can step inside.")
                return CastleInside
        else:
            print(
                "You try to open the door. It's closed. "
                "You observe the door for a minute and notice an old and rusty lock."
            )
            return CastleDoor

    def go_west(self):
        from example.vacation_request.locations.forest import (
            ForestDepthBackwards,
        )

        print("You choose to go back. Coward...")
        return ForestDepthBackwards


class CastleDoor(Castle):
    def welcome_message(self):
        return "You still are in front of the castle."


class CastleDoorReturned(Castle):
    def welcome_message(self):
        return "You step out of the castle frightened by what you have seen inside."
