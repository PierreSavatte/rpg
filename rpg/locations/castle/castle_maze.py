from rpg.locations import Location
from rpg.objects.potion import Potion
from rpg.objects.key import Keys


class CastleMaze(Location):
    def welcome_message(self):
        return "You encounter a carrefour. There are 3 new directions."

    def go_east(self):
        print("You go east and you think the corridor goes a bit north.")
        return CastleMaze2

    def go_west(self):
        print("You go west and you have the feeling it goes a bit north.")
        return CastleMaze4

    def go_north(self):
        return CastleMaze5

    def go_south(self):
        from rpg.locations.castle.castle_insides import (
            BackAtCastleInsideFromMaze,
        )

        return BackAtCastleInsideFromMaze


class CastleMaze2(CastleMaze):
    def welcome_message(self):
        return "You encounter a carrefour. There are 3 new directions."

    def go_east(self):
        print(
            "You go east. It's a really long hallway and you have a strange feeling. As if you have turned around."
        )
        return CastleMaze2

    def go_west(self):
        return CastleMaze5

    def go_north(self):
        print(
            "You go north. And you can clearly see a hook after few minutes. It goes west."
        )
        return CastleMaze3

    def go_south(self):
        print("You go south, but you can feel it goes a bit west too.")
        return CastleMaze


class CastleMaze3(CastleMaze):
    def welcome_message(self):
        return "You encounter a carrefour. There are 3 new directions."

    def go_east(self):
        print("You go east, but it clearly turns south at some point.")
        return CastleMaze2

    def go_west(self):
        print(
            "You go west. It's a really long hallway. You have the feeling it also goes a bit south."
        )
        return CastleMaze4

    def go_north(self):
        return CastleMazeChest

    def go_south(self):
        print("You go south. It's yet another long hallway.")
        return CastleMaze5


class CastleMaze4(CastleMaze):
    def welcome_message(self):
        return "You encounter a carrefour. There are 3 new directions."

    def go_east(self):
        return CastleMaze5

    def go_west(self):
        from rpg.locations.castle.castle_insides import (
            BackAtCastleInsideFromMaze,
        )

        return BackAtCastleInsideFromMaze

    def go_north(self):
        print(
            "You go north. It's a really long hallway. "
            "You think at some point, it's not straight and you go a bit east."
        )
        return CastleMaze3

    def go_south(self):
        print(
            "You go south. And you can clearly see a hook after few minutes. It goes east."
        )
        return CastleMaze


class CastleMaze5(CastleMaze):
    def welcome_message(self):
        return "You encounter a carrefour. There are 3 new directions."

    def go_east(self):
        print("You go east.")
        return CastleMaze2

    def go_west(self):
        return CastleMaze4

    def go_north(self):
        print("You go east. It's another long hallway.")
        return CastleMaze3

    def go_south(self):
        return CastleMaze


class CastleMazeChest(CastleMaze):
    CHOICES = ["go_south", "open_chest"]

    def welcome_message(self):
        return "You enter a small room. There is a chest. You can try to open the chest."

    def open_chest(self):
        print("You approaches the chest. You find a potion!")
        self.game.object_received(Potion(power=40))
        print("You find an ancient key that seems to open a large door.")
        self.game.object_received(Keys.CASTLE_BOSS)
        print("You go back into the maze.")
        return CastleMaze3

    def go_south(self):
        print("You decide not to touch the chest. And go back into the maze.")
        return CastleMaze3
