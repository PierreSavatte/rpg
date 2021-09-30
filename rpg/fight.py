from rpg.game import Character, Game


class Fight:
    def __init__(self, game: Game, foe: Character, player_started_the_fight: bool):
        self.game = game
        self.foe = foe
        self.player_started_the_fight = player_started_the_fight

        self.display_start_of_fight()

    def display_start_of_fight(self):
        enemy_name = self.foe.name
        if self.player_started_the_fight:
            message = f"You attack {enemy_name} (health={self.foe.life_points})."
        else:
            message = f"{enemy_name} (health={self.foe.life_points}) is attacking you."
        print(message)

    def deal_damage(self, attacker, defender, damage):
        attacker.life_points -= damage

        if defender.life_points <= damage:
            print(f"{defender.name} seems really weak now...")

    def foe_attack(self):
        damage = self.foe.strength
        print(f"{self.foe.name} is now hitting you. Dealing {damage} points of damage.")

        self.deal_damage(attacker=self.foe, defender=self.game.player, damage=damage)

    def you_attack(self):
        damage = self.game.player.strength
        print(f"You are hitting {self.foe.name} dealing {damage} points of damage.")
        self.deal_damage(attacker=self.game.player, defender=self.foe, damage=damage)

    def fight(self) -> bool:
        while self.foe.life_points > 0 and self.game.player.life_points > 0:
            decision = self.game.take_a_decision()
            if not decision.count_as_action:
                action = decision.value
                if action == "hit":
                    self.you_attack()
                else:
                    print("It's not effective...")

            self.foe_attack()

        return self.game.player.life_points != 0
