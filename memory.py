"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.


EQUIPO 12
Klaus Manuel Cedillo Arredondo A01653257 
Isaac Jacinto Ruiz A01658578
"""

#Librerias
from random import *
from turtle import *
from freegames import path

#Variables
car = path('car.gif')
#Cambiando la siguiente lista podemos cambiar los simbolos que aparecen, 
#en mi opinion seria mucho más fácil ya que las personas somos seres 
#más visuales
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
numeroDeEncontradas = 0

#diccionario donde se almacena el numero de clics y el mensaje de victoria
counter = {'clicks': 0,'ganador':"Felicidaes, encontraste todas"}
writer = Turtle(visible=False)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    #Contador de clics que se hacen
    counter['clicks'] = counter['clicks']+1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global numeroDeEncontradas
        #Detecta el numero de parejas encontradas
        numeroDeEncontradas = numeroDeEncontradas + 1

def draw():
    "Draw image and tiles."
    #Mensaje que aparece si encuentras todas las parejas
    if numeroDeEncontradas == 32:
        writer.undo()
        writer.goto(0, 160)
        writer.write(counter['ganador'])
    else:
        writer.undo()
        writer.write(counter['clicks'])
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('black')
writer.write(counter['clicks'])
onscreenclick(tap)
draw()
done()
