from rpg.location import Location
from example.vacation_request.keys import Keys


class GuardianCabin(Location):
    CHOICES = ["go_east", "search"]

    INCORRECT_INPUT_MESSAGE = (
        "You cannot do that action. This is a very small place."
    )

    def welcome_message(self):
        return (
            "You are now in the guardian's cabin. "
            "It's a small house with just a bed, a toilet, and a small fireplace."
        )

    def go_east(self):
        from example.vacation_request.locations.forest import ForestEntry

        return ForestEntry

    def search(self):
        if Keys.CASTLE_ENTRY not in self.game.bag.keys:
            print(
                "You are looking through the guard's things. "
                "You find all kinds of trinkets."
            )
            print(
                "Finally you find a rather complex rusty key. "
                "It seems to open something important."
            )
            self.game.object_received(Keys.CASTLE_ENTRY)
        else:
            print(
                "You are continuing searching for useful things but nothing appears to be of any use."
            )
        return StillInGuardianCabin


class StillInGuardianCabin(GuardianCabin):
    def welcome_message(self):
        return "You are looking at the fireplace. It seems the guardian left few years ago already."
