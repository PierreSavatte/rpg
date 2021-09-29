from rpg.game_over import GameOver

DEFAULT_MESSAGE = (
    "A tear in reality appeared and without you realizing it, you entered it. "
    "Unfortunately it closes just after you entered it, leaving you in a deep void. "
    "You don't hear any sound. You noticed that don't feel anything anymore actually. Might you just be dead?"
)


class Location:

    CHOICES = ["go_north", "go_south", "go_east", "go_west"]
    INCORRECT_INPUT_MESSAGE = "This is not a correct choice. Please try again"

    def __init__(self, game, choice_adventurer_made):
        self.choice_adventurer_made = choice_adventurer_made
        self.game = game

    def get_action(self) -> str:
        decision = self.game.take_a_decision()
        while decision.count_as_action or decision.value not in self.CHOICES:
            if not decision.already_processed:
                if decision.value not in self.CHOICES:
                    print(self.INCORRECT_INPUT_MESSAGE)
            decision = self.game.take_a_decision()
        return decision.value

    def unfold_scenario(self):
        self.game.current_location = self
        print(self.welcome_message())

        action = self.get_action()
        do_action = getattr(self, action)
        next_location = do_action()

        if next_location is GameOver:
            self.game.game_over()
            return

        location = next_location(self.game, action)
        location.unfold_scenario()

    def welcome_message(self):
        return "Welcome to this location"

    def go_north(self):
        # from rpg.game import GameOver

        print(DEFAULT_MESSAGE)
        return GameOver

    def go_south(self):
        # from rpg.game import GameOver

        print(DEFAULT_MESSAGE)
        return GameOver

    def go_east(self):
        # from rpg.game import GameOver

        print(DEFAULT_MESSAGE)
        return GameOver

    def go_west(self):
        # from rpg.game import GameOver

        print(DEFAULT_MESSAGE)
        return GameOver
