import random

class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.inventory = []
        self.experience = 0
        self.level = 1

    def heal(self):
        if "аптечка" in self.inventory:
            self.health = min(self.health + 50, 100)
            self.inventory.remove("аптечка")
            print("Здоровье восстановлено до", self.health)
        else:
            print("Нет аптечек в инвентаре!")

    def attack(self, enemy):
        damage = random.randint(10, 30)
        enemy.health -= damage
        print(f"Вы атаковали {enemy.name} и нанесли {damage} урона!")

    def level_up(self):
        if self.experience >= 100:
            self.level += 1
            self.experience -= 100
            print(f"Поздравляем! Вы достигли уровня {self.level}!")

    def check_health(self):
        print(f"Ваше текущее здоровье: {self.health}")

    def show_inventory(self):
        if self.inventory:
            print("Ваш инвентарь:", ", ".join(self.inventory))
        else:
            print("Ваш инвентарь пуст.")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(30, 100)
        self.damage = random.randint(5, 15)

class Planet:
    def __init__(self, name):
        self.name = name
        self.resources = ["аптечка", "оружие", "бронированный жилет", "кристалл энергии", "припасы"]

class NPC:
    def __init__(self, name):
        self.name = name
        self.dialogue = [
            "Привет, странник! Удачи в твоих приключениях!",
            "Здесь опасно, будь осторожен!",
            "Эта планета всеми забыта.",
            "Слышал, что на соседней планете обитают монстры.",
            "Здесь ничего нет"
        ]

    def speak(self):
        print(random.choice(self.dialogue))

def create_player():
    name = input("Введите ваше имя: ")
    return Player()

def explore_planet(player, planet):
    found_item = random.choice(planet.resources + ["ничего"])

    if found_item != "ничего":
        player.inventory.append(found_item)
        print(f"Вы исследовали {planet.name} и нашли: {found_item}")
    else:
        print(f"Вы исследовали {planet.name}, но ничего не нашли.")


def battle(player, enemy):
    while enemy.health > 0 and player.health > 0:
        choice = input(f"Вы хотите сразиться с {enemy.name} или сбежать? (сражаться/сбежать): ").strip().lower()

        if choice == "сражаться":
            player.attack(enemy)
            if enemy.health > 0:
                damage = max(0, enemy.damage)
                player.health -= damage
                print(f"{enemy.name} атаковал вас и нанес {damage} урона!")
                print(f"Ваше здоровье: {player.health}")

                if player.health <= 0:
                    print("Вы погибли! Игра окончена.")
                    return False
            else:
                print(f"Вы победили {enemy.name}!")
                player.experience += 50
                player.level_up()
                return True

        elif choice == "сбежать":
            print("Вы сбежали от врага!")
            return True

        else:
            print("Неизвестный выбор!")

def main():
    player = create_player()
    planets = [Planet("Земля"), Planet("Марс"), Planet("Юпитер"), Planet("Венера"), Planet("Сатурн")]
    enemies = ["Инопланетянин", "Робот", "Монстр", "Космический пират", "Дракон"]
    npcs = [NPC("Тор"), NPC("Лиан"), NPC("Зара"), NPC("Кир"), NPC("Мира")]

    while True:
        action = input("\nВведите команду (исследовать, лечиться, инвентарь, здоровье, выход): ").strip().lower()

        if action == "исследовать":
            planet = random.choice(planets)
            explore_planet(player, planet)

            if planet.name != "Земля" and random.random() < 0.3:
                enemy_name = random.choice(enemies)
                enemy = Enemy(enemy_name)
                print(f"Вы встретили врага: {enemy.name} с {enemy.health} здоровья.")
                if not battle(player, enemy):
                    break

            if random.random() < 0.2:
                npc = random.choice(npcs)
                print(f"Вы встретили NPC: {npc.name}.")
                npc.speak()

        elif action == "лечиться":
            player.heal()

        elif action == "инвентарь":
            player.show_inventory()

        elif action == "здоровье":
            player.check_health()

        elif action == "выход":
            print("Спасибо за игру! До свидания!")
            break

        else:
            print("Неизвестная команда!")

if __name__ == "__main__":
    main()
