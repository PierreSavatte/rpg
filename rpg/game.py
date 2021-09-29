import sys
import attr

from rpg.character import Character
from rpg.input import ask
from rpg.objects.bag import Bag
from rpg.secret import secrets


@attr.s
class Decision:
    value = attr.ib()
    count_as_action = attr.ib()
    already_processed = attr.ib()


class Game:
    def __init__(self):
        name = ask("What is your name?", do_validate=False)
        self.player = Character(name=name)
        self.bag = Bag()
        self.powers = []
        self.current_location = None

    def start(self):
        from rpg.locations.forest import Forest

        forest = Forest(game=self, choice_adventurer_made=None)

        forest.unfold_scenario()

    def take_a_decision(self) -> Decision:
        decision = ask("What do you want to do now?")
        count_as_action = False
        already_processed = False

        if decision in secrets.keys():
            secrets[decision](self)
            already_processed = True

        elif decision.startswith("use_"):
            decision = decision.lstrip("use_")
            count_as_action = True
            already_processed = True
            self.bag.use(game=self, object_name=decision)

        elif decision == "quit":
            print("You quitter...")
            self.game_over()

        return Decision(
            value=decision,
            count_as_action=count_as_action,
            already_processed=already_processed,
        )

    def object_received(self, obj):
        self.bag.add(obj)

    def secret_revealed(self, secret):
        pass

    def game_over(self):
        print("Game Over.")
        print(
            "You suck. Except if you're Eric, at least you knew where to go at the carrefour."
        )
        print(
            "@eric: I would like to have 18/10/21 - 22/10/21 as vacations please. :)"
        )
        sys.exit()

    def win(self):
        print(f"Congratulations {self.player.name}, you have won!")
        print("Thank you for playing this game.")
        print(
            "@eric: I would like to have 18/10/21 - 22/10/21 as vacations please. :)"
        )
        sys.exit()
