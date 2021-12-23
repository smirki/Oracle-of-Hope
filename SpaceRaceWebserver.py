from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'



# Battle Calculatorrr

def battle_stat(winner):
    print(winner +  "won by")

def battle(red, blue):
    # unit calculation

    # battle attributes calculation
    winner = red
    print(winner['name'])



v = 2
b = 2
z = 5
l = 5
h = 7

red = {"name" : "badshah", "hero" : 1}
blue = red
battle(red, blue)


if __name__ == '__main__':
   app.run()

