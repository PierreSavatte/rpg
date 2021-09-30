from rpg.character import Character
from rpg.fight import Fight
from rpg.game_over import GameOver
from rpg.locations import Location
from rpg.locations.castle.castle_entrance import Castle
from rpg.locations.guardian_cabin import GuardianCabin
from rpg.objects.key import Keys

_SPIDER_DEAFEATED = False
_BOAR_DEAFEATED = False


def fight_spider(location: Location):
    global _SPIDER_DEAFEATED

    if not _SPIDER_DEAFEATED:
        print(
            "You approach the weird looking chest. The lock is broken. You open it. You find a big ass spider."
        )
        fight = Fight(
            game=location.game,
            foe=Character(
                name="Spider",
                life_points=30,
                level=1,
                strength=10,
            ),
            player_started_the_fight=False,
        )
        player_won = fight.fight()

        if player_won:
            print(
                "You have defeated the spider. Congratulations. "
                "There is nothing left here, you go back at the entry of the forest."
            )
            _SPIDER_DEAFEATED = True
            return ForestEntry
        else:
            print("You have been defeated by the spider (loser...).")
            return GameOver
    else:
        print(
            "You already have defeated the spider. "
            "There is nothing left here, you go back at the entry of the forest."
        )
        return ForestEntry


class Forest(Location):
    CHOICES = ["go_north", "go_south", "go_east", "go_west", "go_up", "search"]

    def welcome_message(self):
        print(
            "You have entered a deep and dark forest. "
            "You are holding your magnificent sword that "
            "you managed to obtain in a previous quest in which you almost lost your life. "
            "You feel ready to face any danger."
        )
        print(
            "In the distance you can see an old abandoned castle. "
            "On your left, what seems to be the cabin of the guardian of the castle. "
            "On your right an old rusty chest is on the ground. "
        )
        print(
            "There is a small sign at the entrance of the forest saying: "
            '"To go to the castle, enter the forest and go east at the carrefour inside the forest"'
        )
        print(
            "You already heard about this castle in a nearby tavern "
            "when this maid asked you to get a mysterious scroll. "
            "She told you the scroll content could affect the whole region. "
            "You believe it is a powerful charm or some ancient spell."
        )

        return "Which direction do you want to take? (go north, go south, go east or go west?)"

    def go_north(self):
        return ForestDepth

    def go_west(self):
        return GuardianCabin

    def go_up(self):
        if not self.game.player.is_a_god:
            print("Who do you think you are, to try and defy gravity?")
            return ForestEntry

        from rpg.locations.castle.castle_insides import CastleBoss

        print("You are a real Chad and don't follow orders.")
        print(
            "You can see the castle in the distance, you fly there. "
            "You punch the first wall in your way to get into the castle and you find yourself in front of a large door."
        )
        return CastleBoss

    def go_east(self):
        return fight_spider(self)

    def go_south(self):
        print(
            "You come from there. There is no reason to go back now. You must find what you seek."
        )
        return ForestEntry

    def search(self):
        print(
            "You are looking at the ground. "
            "You find all kinds of skeletons rests. "
            "You become really afraid suddenly. "
            "To you it's a a bad omen, you believe a lot of adventurers already visited this forest."
            "You're starting to wonder if maybe this wasn't such a good idea."
        )
        return ForestEntry


class ForestEntry(Forest):
    def welcome_message(self):
        return "You are now back at the entry of the forest."


class ForestDepth(Location):
    def welcome_message(self):
        return (
            "You decide to continue ahead. You enter the depths of the forest. "
            "There is a strange shop on your right. "
            "You believe it's a wizard's shop since it generates a lot of light. "
            "You can see a strange diamond-shaped sign on the shopfront. You decide to ignore it"
        )

    def go_north(self):
        return ForestWrongDirection

    def go_west(self):
        return ForestWrongDirection

    def go_east(self):
        return Castle

    def go_south(self):
        return ForestEntry


class ForestDepthBackwards(ForestDepth):
    def welcome_message(self):
        return (
            "You returned to the depths of the forest. "
            "The night is dark and full of terrors. You barely can see in front of you."
        )


class ForestWrongDirection(ForestDepth):
    def welcome_message(self):
        direction = "to that direction"
        if self.choice_adventurer_made == "go_west":
            direction = "west"
        elif self.choice_adventurer_made == "go_north":
            direction = "north"
        return f"You wanted to go {direction} but the road is blocked."
