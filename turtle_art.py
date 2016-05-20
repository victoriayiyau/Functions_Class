import turtle
# def draw_star():
# 	turtle.reset()
# 	turtle.shape("triangle")
# 	turtle.shapesize(5,2)
# 	turtle.tilt(30)
# 	turtle.fd(50)
# 	turtle.tilt(30)
# 	turtle.fd(50)
window = turtle.Screen()
window.bgcolor("white")

# draw_star()

def draw_triangle(new_turtle):
	for x in range(0, 2):
		new_turtle.pendown()
		new_turtle.right(135)
		new_turtle.forward(100)

# create an instance of Turtle
# fred = turtle.Turtle()

# # set values on attributes in the Turtle module
# fred.shape("turtle")
# fred.color("green", "yellow")  # outline color, fill color
# fred.penup()
# fred.setx(150)
# create another instance of Turtle and set its values
ginger = turtle.Turtle()
ginger.shape("classic")
ginger.color("green")
ginger.penup()
ginger.setx(-150)
# draw one square filled with color with the fred instance
# fred.begin_fill()
# draw_triangle(fred)
# fred.end_fill()
# draw offset squares in a loop with the ginger instance
for x in range(0, 9):
	draw_triangle(ginger)
	ginger.right(50)

window.exitonclick()