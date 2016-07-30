import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
brad.speed(0)
brad.color("yellow")
def draw_square():
	i = 4
	while i > 0:
		brad.forward(100)
		brad.right(90)
		i -= 1

a = 36
while a > 0:
	draw_square()
	brad.left(10)
	a -= 1

window.exitonclick()