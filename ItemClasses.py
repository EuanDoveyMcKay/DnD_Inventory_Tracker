class Item:

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: str="-", description: str="-"):
        self.name = name
        self.type = type
        self.cost = cost
        self.weight = weight
        self.tags = tags
        self.description = description

    def info(self):
        return(f"\nName: {self.name} \nType: {self.type} \nCost: {self.cost}GP \nWeight: {self.weight} lbs \ntags: {self.tags} \ndescription: {self.description}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Armour(Item):

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: str="-", description: str="-", AC: str="0", strength: int="-", stealth: str="-"):
        super().__init__(name, type, cost, weight, tags, description)
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
    
    def info(self):
        return(f"{super().info()} \nAC: {self.AC} \nstrength: {self.strength} \nstealth: {self.stealth}\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Weapon(Item):

    def __init__(self, name: str, type: str = "-", cost: int = 0, weight: float = 0, tags: str = "-", description: str = "-", damage: str = "-", properties: str = "-"):
        super().__init__(name, type, cost, weight, tags, description)
        self.dmg = damage
        self.properties = properties

    def info(self):
        return(f"{super().info()} \nDamage: {self.dmg} \nProperties: {self.properties}\n")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#