#Memoria.py
#Carla Perez, Aranza Garcia
#Juego de memoria 

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None,"count":0}
hide = [True] * 64
writer = Turtle(visible=False)
taps=0 #Contador para el número de Taps
CounterParejas=0 #Contador para el numero de Parejas

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
    spot = index(x, y)
    mark = state['mark']
    global taps
    taps +=1 #Se llama a la variable taps y se le suma uno
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global CounterParejas
        CounterParejas+=1# Se llama a la variable CounterParejas y se le suma uno
    

def draw():
    "Draw image and tiles."
    
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
        if tiles[mark]<=8:
            up()
            goto(x + 26, y+5)
            color(tiles[mark]*7, 255-tiles[mark]*3, 200-tiles[mark]*5) #Cambia los colores de los números en un rango de 0-255 de rgb
            write(tiles[mark], align="center",font=('Arial', 30, 'normal'))#Si el número esta dentro del rango de 1 a 8 será de color amarillo
      
           
    color('red')
    up()
    goto(-190, 180)
    write(taps,  align="center", font=("Arial", 20, "bold")) # Cuenta el número de taps que realice el usuario

    if CounterParejas==32:
        up()
        goto(0, 0)
        color('white')
        write("Has Acabado",  align="center", font=("Arial", 20, "bold"))# Muestra que el usuario ha acabado de juntar las 32 parejas



    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
colormode(255)
addshape(car)
hideturtle()
tracer(False)
addshape(car)
onscreenclick(tap)
draw()
done()
