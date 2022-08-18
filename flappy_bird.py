# Welcome to a small game called Flappy Bird #
# Created by Team Dot members #
# Press SPACE button to fly bird #

import turtle
import time
import winsound

windows = turtle.Screen()
windows.title("Flappy Bird")
windows.bgpic("wallpaper.png")
windows.setup(500, 600)
windows.register_shape("bird1.gif")
windows.tracer(0)

point = turtle.Turtle()
point.speed(0)
point.hideturtle()
point.penup()
point.color("white")
point.goto(0, 250)
point.write("0", move=False, align="left", font=("Arial", 32, "normal"))

bird = turtle.Turtle()
bird.speed(0)
bird.penup()
bird.shape("bird1.gif")
bird.goto(-200, 0)
bird.dx = 0
bird.dy = 1

tube1_top = turtle.Turtle()
tube1_top.speed(0)
tube1_top.penup()
tube1_top.color("green")
tube1_top.shape("square")
tube1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
tube1_top.goto(300, 250)
tube1_top.dx = -2
tube1_top.dy = 0
tube1_top.value = 1

tube1_bottom = turtle.Turtle()
tube1_bottom.speed(0)
tube1_bottom.penup()
tube1_bottom.color("green")
tube1_bottom.shape("square")
tube1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
tube1_bottom.goto(300, -250)
tube1_bottom.dx = -2
tube1_bottom.dy = 0

tube2_top = turtle.Turtle()
tube2_top.speed(0)
tube2_top.penup()
tube2_top.color("green")
tube2_top.shape("square")
tube2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
tube2_top.goto(600, 300)
tube2_top.dx = -2
tube2_top.dy = 0
tube2_top.value = 1

tube2_bottom = turtle.Turtle()
tube2_bottom.speed(0)
tube2_bottom.penup()
tube2_bottom.color("green")
tube2_bottom.shape("square")
tube2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
tube2_bottom.goto(600, -200)
tube2_bottom.dx = -2
tube2_bottom.dy = 0

gravity = -0.3


# Define function / method
def button():
    bird.dy += 8
    winsound.PlaySound('wing.wav', winsound.SND_ASYNC)

    if bird.dy > 8:
        bird.dy = 8


# Keyboard binding
windows.listen()
windows.onkeypress(button, "space")

# Initialize game variables
bird.score = 0

# Main Game Loop
while True:
    # Pause
    time.sleep(0.02)
    # Update the screen
    windows.update()

    # Add gravity
    bird.dy += gravity

    # Move bird
    y = bird.ycor()
    y += bird.dy
    bird.sety(y)

    # Bottom Border
    if bird.ycor() < -390:
        bird.dy = 0
        bird.sety(-390)

    # Move Tube 1
    x = tube1_top.xcor()
    x += tube1_top.dx
    tube1_top.setx(x)

    x = tube1_bottom.xcor()
    x += tube1_bottom.dx
    tube1_bottom.setx(x)

    # Return tubes to start
    if tube1_top.xcor() < -350:
        tube1_top.setx(350)
        tube1_bottom.setx(350)
        tube1_top.value = 1

    # Move tube 2
    x = tube2_top.xcor()
    x += tube2_top.dx
    tube2_top.setx(x)

    x = tube2_bottom.xcor()
    x += tube2_bottom.dx
    tube2_bottom.setx(x)

    # Return tubes to start
    if tube2_top.xcor() < -350:
        tube2_top.setx(350)
        tube2_bottom.setx(350)
        tube2_top.value = 1

    # Check for collisions with tubes
    # tube 1
    if (bird.xcor() + 10 > tube1_top.xcor() - 30) and (bird.xcor() - 10 < tube1_top.xcor() + 30):
        if (bird.ycor() + 10 > tube1_top.ycor() - 180) or (bird.ycor() - 10 < tube1_bottom.ycor() + 180):
            point.clear()
            winsound.PlaySound('die.wav', winsound.SND_ASYNC)
            point.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
            windows.update()
            time.sleep(3)
            # Reset score
            bird.score = 0
            # Move tubes Back
            tube1_top.setx(300)
            tube1_bottom.setx(300)
            tube1_top.setx(600)
            tube1_bottom.setx(600)
            # Move bird back
            bird.goto(-200, 0)
            bird.dy = 0

    # Check for point
    if tube1_top.xcor() + 30 < bird.xcor() - 10:
        bird.score += tube1_top.value
        tube1_top.value = 0
        point.clear()
        point.write(bird.score, move=False, align="center", font=("Arial", 32, "normal"))

    # Check for collisions with tubes
    # Tube 2
    if (bird.xcor() + 10 > tube2_top.xcor() - 30) and (bird.xcor() - 10 < tube2_top.xcor() + 30):
        if (bird.ycor() + 10 > tube2_top.ycor() - 180) or (bird.ycor() - 30 < tube2_bottom.ycor() + 180):
            point.clear()
            winsound.PlaySound('die.wav', winsound.SND_ASYNC)
            point.write("Game Over", move=False, align="left", font=("Arial", 16, "normal"))
            windows.update()
            time.sleep(3)
            # Reset score
            bird.score = 0
            # Move Pipes Back
            tube2_top.setx(300)
            tube2_bottom.setx(300)
            tube2_top.setx(600)
            tube2_bottom.setx(600)
            # Move bird back
            bird.goto(-200, 0)
            bird.dy = 0
            # Clear the point
            point.clear()

    # Check for point
    if tube2_top.xcor() + 30 < bird.xcor() - 10:
        bird.score += tube2_top.value
        tube2_top.value = 0
        point.clear()
        point.write(bird.score, move=False, align="left", font=("Arial", 32, "normal"))

windows.mainloop()