# Battle Calculator
import pickle

class Civilization():
    name = "Default Civilization"
    hero_count = 1
    builder_count = 20
    def __init__(self, param, name, hero_count):
        self.param = param
        self.name = name
        self.hero_count = hero_count
    
class Planet():
    name = "Default Planet"
    coord_x = 0.0
    coord_y = 0.0
    colonies = []
    ores = []
    copper = []
    limestone = []
    grasslands = []
    forests = []
    deserts = []
    def __init__(self, name, coord_x, coord_y):
        self.name = name
        self.coord_x = coord_x
        self.coord_y = coord_y

class Colony():
    name = "Fault Colony"

class IronOrePoint():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class CopperOrePoint():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class LimestoneOrePoint():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Grassland():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Forest():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Desert():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, name, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


# Save and Load Handler functions

def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def battle(red, blue):
    # unit calculation

    # battle attributes calculation
    if (red.param > blue.param):
        winner = red
    else:
        winner = blue
    print(winner.name)

# default civ passthrough

list = []

red = Civilization(10, "Sa", 1)
blue = Civilization(12, "Sda", 1)
list.append(red)
list.append(blue)

battle(red,blue)
save_object(list)

fire = load_object("data.pickle")

print(fire[0].param)