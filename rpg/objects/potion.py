from rpg.objects import Object


class Potion(Object):
    def __init__(self, power=10):
        self.power = power

    def use(self, game):
        print(f"You use a potion and get {self.power} health points.")
        game.player.life_points += self.power
        return True
