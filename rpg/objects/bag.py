from collections import defaultdict

from rpg.objects.potion import Potion
from rpg.objects.key import RPGKeys


class Bag:
    def __init__(self):
        self.potions = []
        self.keys = []
        self.other_objects = defaultdict(list)

    def add(self, obj):
        if isinstance(obj, Potion):
            self.potions.append(obj)
        if isinstance(obj, RPGKeys):
            self.keys.append(obj)
        else:
            name = obj.__class__.__name__.lower()
            self.other_objects[name].append(obj)

    def use(self, game, object_name: str) -> bool:
        if object_name == "potion":
            if len(self.potions):
                potion = self.potions.pop()
                potion.use(game)
                return True

        elif object_name == "key":
            if len(self.keys):
                success = False
                for key in self.keys:
                    success = success or key.value.use(game)
                if success:
                    return True
                else:
                    print("You tried all your keys but none fits the lock.")
                    return False

        print(f"You don't have any {object_name}. You can not use one.")
        return False
