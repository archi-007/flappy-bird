import turtle
import time



sc = turtle.Screen()
sc.title("Bird")
sc.bgcolor("green")
sc.setup(width=650, height=800)
sc.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))


bird = turtle.Turtle()
bird.speed(0)
bird.color('yellow')
bird.shape('turtle')
bird.penup()
bird.goto(-200,0)
bird.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=None)
bird.dx = 0
bird.dy = 1


pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.color('red')
pipe1_top.shape('square')
pipe1_top.penup()
pipe1_top.goto(300,250)
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1



pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.color('red')
pipe1_bottom.shape('square')
pipe1_bottom.penup()
pipe1_bottom.goto(300,-250)
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0




pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("red")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 280)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1




pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("red")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -220)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0




pipe3_top = turtle.Turtle()
pipe3_top.speed(0)
pipe3_top.penup()
pipe3_top.color("red")
pipe3_top.shape("square")
pipe3_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_top.goto(900, 320)
pipe3_top.dx = -2
pipe3_top.dy = 0
pipe3_top.value = 1





pipe3_bottom = turtle.Turtle()
pipe3_bottom.speed(0)
pipe3_bottom.penup()
pipe3_bottom.color("red")
pipe3_bottom.shape("square")
pipe3_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_bottom.goto(900, -180)
pipe3_bottom.dx = -2
pipe3_bottom.dy = 0




gravity = -0.3


def jump():
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8
sc.listen()
sc.onkeypress(jump, "space")

bird.score = 0

pipes = [(pipe1_top,pipe1_bottom),(pipe2_top,pipe2_bottom),(pipe3_top,pipe3_bottom)]

while True:

    time.sleep(0.02)

    sc.update()

    bird.dy = bird.dy + gravity

    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)


    if bird.ycor() < -390:
        bird.dy = 0
        bird.sety(-390)

    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]


        x = pipe_top.xcor()
        x += pipe_top.dx
        pipe_top.setx(x)


        
        x = pipe_bottom.xcor()
        x += pipe_bottom.dx
        pipe_bottom.setx(x)


        if pipe_top.xcor() < -350:
            pipe_top.setx(600)
            pipe_bottom.setx(600)
            pipe_top.value = 1



        if (bird.xcor() + 10 > pipe_top.xcor() - 30) and (bird.xcor() - 10 < pipe_top.xcor() + 30):
            if (bird.ycor() + 10 > pipe_top.ycor() - 180) or (bird.ycor() - 10 < pipe_bottom.ycor() + 180):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
                sc.update()
                time.sleep(3)
                


                bird.score = 0
                


                pipe_top.setx(450)
                pipe_bottom.setx(450)
                



                bird.goto(-200, 0)
                bird.dy = 0
                


                pen.clear()
                pen.write("0", move=False, align="center", font=("Arial", 16, "normal"))



        if pipe_top.xcor() + 30 < bird.xcor() - 10:
            bird.score += pipe_top.value
            pipe_top.value = 0
            pen.clear()
            pen.write(bird.score, move=False, align="center", font=("Arial", 32, "normal"))




sc.mainloop()
