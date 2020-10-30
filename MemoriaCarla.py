from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None,"count":0}
hide = [True] * 64
writer = Turtle(visible=False)
taps=0
CounterParejas=0

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
    taps +=1
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global CounterParejas
        CounterParejas+=1
    

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
            color('yellow')
            write(tiles[mark], align="center",font=('Arial', 30, 'normal'))
        elif tiles[mark]>=9 and tiles[mark]<=16:
            up()
            goto(x + 26, y+5)
            color('blue')
            write(tiles[mark], align="center",font=('Arial', 30, 'normal'))
        elif tiles[mark]>=17 and tiles[mark]<=24:
            up()
            goto(x + 26, y+5)
            color('purple')
            write(tiles[mark], align="center",font=('Arial', 30, 'normal'))
        elif tiles[mark]>=25 and tiles[mark]<=32:
            up()
            goto(x + 26, y+5)
            color('pink')
            write(tiles[mark], align="center",font=('Arial', 30, 'normal'))

    color('red')
    up()
    goto(-190, 180)
    write(taps,  align="center", font=("Arial", 20, "bold"))

    if CounterParejas==32:
        up()
        goto(0, 0)
        color('white')
        write("Has Acabado",  align="center", font=("Arial", 20, "bold"))



    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
addshape(car)
onscreenclick(tap)
draw()
done()