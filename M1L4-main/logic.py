from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, name,):

        self.pokemon_trainer = pokemon_trainer   
        self.hp = randint(4,12)
        self.power = randint()
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.name = name

    def get_img(self):
        pass
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/1.gif"
        
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    def info(self):
        return f"Имя твоего покеомона: {self.name}"
    
    
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


    def attack(self, enemy):
        if isinstance(enemy, Wizzard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
            
        
class Fighter(Pokemon):
    def attack(self, enemy):
        return super().attack(enemy)
    def attack(self, enemy):
        super_attack = randint(5,15)
        self.power += super_attack
        result = super().attack(enemy)
        self.power -= super_attack
        return result + f"\nБоец применил супер-атаку силой:{super_attack} "
    def info():
        return "У тебя покемон боец n\n" + super().info()

 
class Wizzard(Pokemon):
    def info():
        return "У тебя покемон волшебник n\n" + super().info()