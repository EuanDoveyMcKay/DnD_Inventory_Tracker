# Reference being used is: https://www.dndbeyond.com/sources/basic-rules/equipment

class Item:

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: list=[], description: str="-"):
        self.name = name
        self.type = type
        self.cost = cost
        self.weight = weight
        self.tags = tags
        self.description = description

    def info(self, PrintIt=True):
        StringOfTags = ", ".join(self.tags)
        if PrintIt == True:
            print(f"\nName: {self.name} \nType: {self.type} \nCost: {self.cost} GP \nWeight: {self.weight} lbs \ntags: {StringOfTags} \ndescription: {self.description}")
        else:
            return(f"\nName: {self.name} \nType: {self.type} \nCost: {self.cost} GP \nWeight: {self.weight} lbs \ntags: {self.tags} \ndescription: {self.description}")
    
    def Rename(self, NewName: str):
        self.name = NewName

    def Cost(self, NewCost: int):
        self.cost = NewCost

    def Weight(self, NewWeight: float):
        self.weight = NewWeight

    def AddTags(self, NewTags: list):
        self.tags.append(NewTags)

    def RemoveTags(self, TagsToRemove: list):
        if TagsToRemove.index("All") != -1 or TagsToRemove.index("all") != -1:
            self.tags = []
        else:
            for tag in TagsToRemove:
                self.tags.remove(tag)
    
    def NewDesc(self, NewDescription: str):
        self.description = NewDescription

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Armour(Item):

    def __init__(self, name: str, type: str="-", cost: int=0, weight: float=0.0, tags: str="-", description: str="-", AC: str="0", strength: int="-", stealth: str="-"):
        super().__init__(name, type, cost, weight, tags, description)
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
    
    def info(self, PrintIt = True):
        if PrintIt == True:
            print(f"{super().info()} \nAC: {self.AC} \nstrength: {self.strength} \nstealth: {self.stealth}\n")
        else:
            return(f"{super().info()} \nAC: {self.AC} \nstrength: {self.strength} \nstealth: {self.stealth}\n")
    
    def ChangeAC(self, NewAC: str):
        self.AC = NewAC

    def Strength(self, NewStrength: int):
        self.strength = NewStrength

    def Stealth(self, NewStealth: str):
        self.stealth = NewStealth

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Weapon(Item):

    def __init__(self, name: str, type: str = "-", cost: int = 0, weight: float = 0, tags: str = "-", description: str = "-", damage: str = "-", properties: list = []):
        super().__init__(name, type, cost, weight, tags, description)
        self.damage = damage
        self.properties = properties

    def info(self, PrintIt = True):
        StringOfProperties = ", ".join(self.properties)
        if PrintIt == True:
            print(f"{super().info()} \nDamage: {self.damage} \nProperties: {StringOfProperties}\n")
        else:
            return(f"{super().info()} \nDamage: {self.damage} \nProperties: {StringOfProperties}\n")
    
    def Damage(self, NewDamage: str):
        self.damage = NewDamage

    def AddProperties(self, NewProperties: list):
        self.properties.append(NewProperties)

    def RemoveProperties(self, PropertiesToRemove: list):
        if PropertiesToRemove.index("All") != -1 or PropertiesToRemove.index("all") != -1:
            self.properties = []
        else:
            for property in PropertiesToRemove:
                self.properties.remove(property)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Container:
    
    def __init__(self, name: str, capacity: str):
        self.name = name
        self.capacity = capacity

    def info(self, PrintIt = True):
        if PrintIt == True:
            print(f"\nName: {self.name} \nCapacity: {self.capacity}\n")
        else:
            return(f"\nName: {self.name} \nCapacity: {self.capacity}\n")
    
    def Rename(self, name: str):
        self.name = name

    def Capacity(self, capacity: str):
        self.capacity = capacity

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
