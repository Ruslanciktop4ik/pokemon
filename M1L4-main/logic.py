from random import randint
import requests
from datetime import datetime, timedelta

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

    def feed(self, feed_interval = 60, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > feed_interval:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time + delta_time}"
            
        
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
    def feed(self):
        return super().feed(feed_interval=10)

 
class Wizzard(Pokemon):
    def info():
        return "У тебя покемон волшебник n\n" + super().info()
    def feed(self):
        return super().feed(hp_increase=20)