import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
pitt = turtle.Turtle()
angelina = turtle.Turtle()
brad.speed(0)
brad.color("yellow")
size = 300

def ustaw(zolw):
	zolw.up()
	zolw.backward(100)
	zolw.right(90)
	zolw.forward(100)
	zolw.left(90)
	zolw.down()

ustaw(brad)
ustaw(pitt)
ustaw(angelina)

def trojkat(size,zolw):

	zolw.forward(size)
	zolw.left(120)
	zolw.forward(size)
	zolw.left(120)
	zolw.forward(size)
	zolw.left(120)
	zolw.forward(size/2)

trojkat(size,brad)
trojkat(size,pitt)
trojkat(size,angelina)

def trojkat2(size2,zolw):
	zolw.left(60)
	zolw.forward(size2)
	zolw.left(120)
	zolw.forward(size2)
	zolw.left(120)
	zolw.forward(size2)
	zolw.left(60)
	zolw.forward(size2/2)

i=50 
a=2
while i > 0:
	trojkat2(size/a)
	i -= 1
	a *= 2



window.exitonclick()