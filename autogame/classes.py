class Config:
    import json
    def __init__(self):
        with open ("config.json") as file:
            self.path = self.json.loads(file.read())

class Db:
    import sqlite3
    def __init__(self, path):
        self.conn = self.sqlite3.connect(path)
        self.conn.text_factory = str
        self.c = self.conn.cursor()

class ScoreDb:
    import sqlite3
    def __init__(self):
        self.conn = self.sqlite3.connect("score.db")
        self.conn.text_factory = str
        self.c = self.conn.cursor()

        self.c.execute("CREATE TABLE IF NOT EXISTS scores (block_start INTEGER, hash TEXT, seed TEXT, experience INT, inventory TEXT, league TEXT,bet TEXT, damage TEXT, defense TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS unfinished (block_start INTEGER, hash TEXT, seed TEXT, experience INT, inventory TEXT, league TEXT,bet TEXT, damage TEXT, defense TEXT)")

class Game:

    def __init__(self):
        self.potions = [HealthPotion]
        self.armors = [Armor]
        self.weapons = [Sword, Warhammer]
        self.enemies = [Troll, Goblin, Berserker, Dragon]  # order matters!

        self.properties = {}
        self.seed = None
        self.current_block = None
        self.hash = None
        self.finished = False
        self.story = {}
        self.step = 0
        self.quit = False
        self.filename_temp = None
        self.filename = None
        self.replay_exists = False
        self.cycle={}
        self.subcycle={}
        self.bet = 0
        self.league = None
        self.coordinator = None
        self.interaction_string = "autogame:add"

class Hero:
    def __init__(self):
        self.full_hp = 500
        self.health = self.full_hp
        self.power = 10
        self.alive = True
        self.in_combat = False
        self.experience = 0
        self.armor = 0

        self.weapon = None
        self.armor = None
        self.ring = None


class Troll:
    def __init__(self):
        self.trigger = "4f"
        self.name = "Troll"
        self.health = 20
        self.power = 20
        self.alive = True
        self.requirement = 0

class Goblin:
    def __init__(self):
        self.trigger = "df"
        self.name = "Goblin"
        self.health = 20
        self.power = 10
        self.alive = True
        self.requirement = 0

class Berserker:
    def __init__(self):
        self.trigger = "5a"
        self.name = "Berserker"
        self.health = 15
        self.power = 40
        self.alive = True
        self.requirement = 0

class Dragon:
    def __init__(self):
        self.trigger = "61a"
        self.name = "Dragon"
        self.health = 300
        self.power = 75
        self.alive = True
        self.requirement = 0

class Fenrir:
    def __init__(self):
        self.trigger = "53b"
        self.name = "Fenrir"
        self.health = 500
        self.power = 100
        self.alive = True
        self.requirement = 0

class Dwarf:
    def __init__(self):
        self.trigger = "4c"
        self.name = "Dwarf"
        self.health = 20
        self.power = 5
        self.alive = True
        self.requirement = 0



class Sword:
    def __init__(self):
        self.trigger = "70b"
        self.name = "Sword"
        self.power = 10

class Warhammer:
    def __init__(self):
        self.trigger = "64c"
        self.name = "Warhammer"
        self.power = 15

class Armor:
    def __init__(self):
        self.trigger = "69a"
        self.name = "Armor"
        self.defense = 5


class ChaosRing:
    def __init__(self):
        self.trigger = "item:chaos_ring"

    def roll_good(self):
        self.health_modifier = +150
        self.name = "Perseverance Ring"
        self.string = "You slide the ring on your finger and immediately feel stronger"
        return self

    def roll_bad(self):
        self.health_modifier = -150
        self.name = "Blight Ring"
        self.string = "You slide the ring on your finger and your hands start to tremble"
        return self


class HealthPotion:
    def __init__(self):
        self.trigger = "3d"

class Ragnarok:
    def __init__(self):
        self.trigger = "event:ragnarok"

#the following lists are static, changes to these are persistent across object instances
items_interactive = [ChaosRing]
events_interactive_global = [Ragnarok]
enemies_ragnarok = [Fenrir, Dwarf]  # order matters!