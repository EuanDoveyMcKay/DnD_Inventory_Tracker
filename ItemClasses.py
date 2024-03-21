# Reference being used is: https://www.dndbeyond.com/sources/basic-rules/equipment

class Item:

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: str="-", description: str="-"):
        self.name = name
        self.type = type
        self.cost = cost
        self.weight = weight
        self.tags = tags
        self.description = description

    def info(self):
        return(f"\nName: {self.name} \nType: {self.type} \nCost: {self.cost} GP \nWeight: {self.weight} lbs \ntags: {self.tags} \ndescription: {self.description}")
    
    def Rename(self, name: str):
        self.name = name

    def Cost(self, cost: int):
        self.cost = cost

    def Weight(self, weight: float):
        self.weight = weight

    def Tags(self, tags: str):
        self.tags = tags
    
    def Desc(self, description: str):
        self.description = description

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Armour(Item):

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: str="-", description: str="-", AC: str="0", strength: int="-", stealth: str="-"):
        super().__init__(name, type, cost, weight, tags, description)
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
    
    def info(self):
        return(f"{super().info()} \nAC: {self.AC} \nstrength: {self.strength} \nstealth: {self.stealth}\n")
    
    def ChangeAC(self, AC: str):
        self.AC = AC

    def Strength(self, strength: int):
        self.strength = strength

    def Stealth(self, stealth: str):
        self.stealth = stealth

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Weapon(Item):

    def __init__(self, name: str, type: str = "-", cost: int = 0, weight: float = 0, tags: str = "-", description: str = "-", damage: str = "-", properties: str = "-"):
        super().__init__(name, type, cost, weight, tags, description)
        self.damage = damage
        self.properties = properties

    def info(self):
        return(f"{super().info()} \nDamage: {self.dmg} \nProperties: {self.properties}\n")
    
    def Damage(self, damage: str):
        self.damage = damage

    def Properties(self, properties: str):
        self.properties = properties
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Container:
    
    def __init__(self, name: str, capacity: str):
        self.name = name
        self.capacity = capacity

    def info(self):
        return(f"\nName: {self.name} \nCapacity: {self.capacity}\n")
    
    def Rename(self, name: str):
        self.name = name

    def Capacity(self, capacity: str):
        self.capacity = capacity

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#