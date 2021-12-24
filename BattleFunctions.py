# Main Calculations
import pickle
import matplotlib.pyplot as plt

# Globals
Civilizations = []
Space = []

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

class Civilization():
    name = "Default Civilization"
    hero_count = 1
    builder_count = 20
    mothership = []
    def __init__(self, param, name, hero_count):
        self.param = param
        self.name = name
        self.hero_count = hero_count

class Mothership():
    name = ""
    coord_x = 0.0
    coord_y = 0.0
    coord_size = 50
    def __init__(self, name, coord_x, coord_y):
        self.name = name
        self.coord_x = coord_x
        self.coord_y = coord_y

class Planet():
    name = "Default Planet"
    coord_x = 0.0
    coord_y = 0.0
    coord_size = 200
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
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class CopperOrePoint():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class LimestoneOrePoint():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Grassland():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Forest():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Desert():
    coord_x = 0.0
    coord_y = 0.0
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

def battle(red, blue):
    # unit calculation

    # battle attributes calculation
    if (red.param > blue.param):
        winner = red
    else:
        winner = blue
    print(winner.name)

# default civ passthrough

red = Civilization(10, "Sa", 1)
blue = Civilization(12, "Sda", 1)
Civilizations.append(red)
Civilizations.append(blue)

battle(red,blue)
save_object(Civilizations)

fire = load_object("data.pickle")

print(fire[0].param)

# Map Generation

orange = Mothership("Stasis", 300.0, 500.0)
red.mothership.append(orange)
yellow = Mothership("Prime", 350.0, 550.0)
blue.mothership.append(yellow)
green = Planet("Gumbpa", 320, 520)


x = []
y = []
s = []
n = []

print(Civilizations)
for i, a in Civilizations.items():
    a = a.mothership[0]
    print(a)
    x.append(a.coord_x)
    y.append(a.coord_y)
    s.append(a.coord_size)
    n.append(a.name)

print(x)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.scatter(x, y, s)


for i, a in enumerate(n):
    plt.annotate(a, (x[i], y[i]))

plt.show()