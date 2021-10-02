from example.vacation_request.locations.forest import Forest
from rpg.game import Game


def main():
    game = Game(starting_location=Forest)
    game.start()


if __name__ == "__main__":
    main()
