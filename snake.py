import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

# snake bodies
bodies = []

# main screen
main_Screen = turtle.Screen()
main_Screen.title("Snake Game")

main_Screen.bgcolor('#a18740')
main_Screen.setup(width=600, height=600)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('white')
head.fillcolor('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# item
food = turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color('yellow')
food.fillcolor('red')
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# score board
sb = turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()
sb.ht()
food.goto(-280, 250)
sb.write('Score:0 | HighestScore: 0', font=('arial', 15, 'bold'))


# function declaration
def moveup():
    if head.direction != 'down':
        head.direction = 'up'


def movedown():
    if head.direction != 'up':
        head.direction = 'down'


def moveleft():
    if head.direction != 'right':
        head.direction = 'left'


def moveright():
    if head.direction != 'left':
        head.direction = 'right'


def movestop():
    head.direction = 'stop'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


# event
main_Screen.listen()
main_Screen.onkey(moveup, 'Up')
main_Screen.onkey(movedown, 'Down')
main_Screen.onkey(moveleft, 'Left')
main_Screen.onkey(moveright, 'Right')
main_Screen.onkey(movestop, 'space')

# main loop
while True:
    main_Screen.update()

    # check collision with border
    if head.xcor() > 280:
        head.setx(-280)

    if head.xcor() < -280:
        head.setx(280)

    if head.ycor() > 280:
        head.sety(-280)

    if head.ycor() > 280:
        head.sety(-280)

    # check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase the length of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('square')
        body.color('red')
        body.fillcolor('darkred')

        # append ned body
        bodies.append(body)

        # increase the score
        score += 10

        # change delay
        delay -= 0.01

        # update the highest score
        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write('Score: {} | Highest Score: {}'.format(score, highestscore), font=('arial', 15, 'bold'))


    # move the snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            # update score board
            sb.clear()
            sb.write('Score: {} | Highest Score: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

    time.sleep(delay)
main_Screen.mainloop()











